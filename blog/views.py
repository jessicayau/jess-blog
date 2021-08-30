from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Post, Comment
from .forms import CreatePostForm, CommentForm

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    paginate_by = 10


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    extra_context = {"comment_form": CommentForm}

    def post(self, request, *args, **kwargs):
        new_comment = Comment(text=request.POST.get('text'),
                            user=self.request.user,
                            post=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)
    

class BlogCreateView(LoginRequiredMixin, CreateView):
    form_class = CreatePostForm
    template_name = 'post_new.html'

    def form_valid(self, form):
        post = form.save(False)
        post.cover = form.cleaned_data['cover']
        post.save()
        return super().form_valid(form)
   

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'content', 'cover']


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class BlogSearchView(ListView):
    model = Post
    template_name = 'search_results.html'
    context_object_name = 'search_results'

    def get_queryset(self):
        search_text = self.request.GET.get("search", "")
        if search_text:
            search_list = Post.objects.filter(title__icontains=search_text) | Post.objects.filter(content__icontains=search_text) | Post.objects.filter(category__contains=search_text)
        else:
            search_list = None
        return search_list


class AllPostsView(ListView):
    model = Post
    template_name = 'category_template.html'
    context_object_name = 'posts'
    paginate_by = 12


class LifeStyleCategoryView(ListView):
    model = Post
    template_name = 'category_template.html'
    context_object_name = 'posts'
    extra_context = {'category': 'Lifestyle'}
    paginate_by = 18

    def get_queryset(self):
        posts = Post.objects.filter(category="Lifestyle")
        return posts


class TechCategoryView(ListView):
    model = Post
    template_name = 'category_template.html'
    context_object_name = 'posts'
    extra_context = {'category': 'Tech'}
    paginate_by = 18

    def get_queryset(self):
        posts = Post.objects.filter(category="Tech")
        return posts



def error_400(request, exception):
    return render(request, '400.html') 

def error_403(request, exception):
    return render(request, '403.html')

def error_404(request, exception):
    return render(request, '404.html')

def error_500(request):
    return render(request, '500.html')
        
  
from django.urls import path
from .views import AllPostsView, BlogDeleteView, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogSearchView, LifeStyleCategoryView, TechCategoryView
from django.conf.urls import handler400, handler403, handler404, handler500

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('posts/', AllPostsView.as_view(), name='all_posts'),
    path('search/', BlogSearchView.as_view(), name='search'),
    path('lifestyle/', LifeStyleCategoryView.as_view(), name='lifestyle_category'),
    path('tech/', TechCategoryView.as_view(), name='tech_category'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='post_detail'),
]

handler400 = 'blog.views.error_400'
handler403 = 'blog.views.error_403'
handler404 = 'blog.views.error_404'
handler500 = 'blog.views.error_500'
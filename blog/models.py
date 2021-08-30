from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Post(models.Model):

    CATEGORY_CHOICES = {
        ("Lifestyle", "Lifestyle"),
        ("Tech", "Tech"),
    }

    title = models.CharField(max_length=200, unique=True)
    content = RichTextUploadingField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="Lifestyle")
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True, null=True, blank=True)
    cover = models.ImageField(upload_to="post_covers/")
    slug = models.SlugField(editable=False, max_length=200)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date']
    
    def __str__(self):
        return self.text[:20]

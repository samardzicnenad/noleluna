from django.shortcuts import render
from django.views.generic import View

from blog_post.models import BlogPost
from noleluna.settings import MEDIA_URL


class BlogPostView(View):
    @staticmethod
    def get(request):
        data = {'blog_posts': BlogPost.objects.all(), 'media_url': MEDIA_URL}
        return render(request, "blog_post/dashboard.html", data)

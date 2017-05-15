from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from blog_post.models import BlogPost


class BlogPostView(View):
    @staticmethod
    def get(request):
        data = {'blog_posts': BlogPost.objects.all()}
        return render(request, "blog_post/dashboard.html", data)

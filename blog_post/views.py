from django.shortcuts import render
from django.views.generic import View

from blog_post.models import BlogPost
from noleluna.settings import MEDIA_URL
from utils.enums import BLOG_POST_STATE


class IndexBlogPostView(View):
    @staticmethod
    def get(request):
        data = {
            'posts': BlogPost.objects.filter(state=BLOG_POST_STATE.PUBLISHED.value).order_by('-last_edited_on')[:3],
            'media_url': MEDIA_URL,
            'index_page': True}
        return render(request, "blog_post/dashboard.html", data)


class BlogPostView(View):
    @staticmethod
    def get(request):
        data = {'posts': BlogPost.objects.filter(state=BLOG_POST_STATE.PUBLISHED.value).order_by('-last_edited_on'),
                'media_url': MEDIA_URL,
                'index_page': False}
        return render(request, "blog_post/dashboard.html", data)

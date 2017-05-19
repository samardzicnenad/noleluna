from django.shortcuts import render
from django.views.generic import View

from blog_post.models import BlogPost
from noleluna.settings import MEDIA_URL
from utils.enums import BLOG_POST_STATE


class BlogPostView(View):
    @staticmethod
    def get(request, index_page):
        posts = BlogPost.objects.filter(state=BLOG_POST_STATE.PUBLISHED.value).order_by('-last_edited_on')
        if index_page:
            posts = posts[:3]
        data = {'posts': posts,
                'media_url': MEDIA_URL,
                'index_page': index_page}
        return render(request, "blog_post/dashboard.html", data)

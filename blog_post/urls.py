from django.conf.urls import url

from .views import BlogPostView

urlpatterns = [
    url(r'^$', BlogPostView.as_view(), name="blog_posts_view")
]

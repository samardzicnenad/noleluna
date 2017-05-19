from django.conf.urls import url

from .views import BlogPostView

urlpatterns = [
    url(r'^$', BlogPostView.as_view(), {'index_page': False}, name="blog_posts_view")
]

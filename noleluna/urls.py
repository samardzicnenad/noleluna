"""noleluna URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include, static
from django.contrib import admin

from blog_post.views import IndexBlogPostView
from . import views

urlpatterns = [
    url(r'^$', IndexBlogPostView.as_view(), name='index'),
    url(r'^(?P<member_id>[0-9]+)/$', views.family_member, name='family_member'),
    url(r'^(?P<member_id>[0-9]+)/bio/$', views.family_member_bio, name='family_member_bio'),
    url(r'^admin/', admin.site.urls),

    url(r'^posts/', include('blog_post.urls', namespace="blog_posts")),
]
if settings.DEBUG:
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

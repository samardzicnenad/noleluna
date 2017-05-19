from django.contrib import admin

from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'state', 'tag', 'created_on', 'last_edited_on')


admin.site.register(BlogPost, BlogPostAdmin)

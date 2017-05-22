from django.contrib import admin
from django.db import models
from markdownx.widgets import AdminMarkdownxWidget

from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'state', 'tag', 'created_on', 'last_edited_on')
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }


admin.site.register(BlogPost, BlogPostAdmin)

from django.db import models
from multiselectfield import MultiSelectField

from utils.enums import BLOG_POST_STATE, FAMILY_MEMBER


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    state = models.IntegerField(choices=BLOG_POST_STATE.choices(), default=BLOG_POST_STATE.DRAFT.value)
    tags = MultiSelectField(choices=FAMILY_MEMBER.choices(), null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_edited_on = models.DateTimeField(auto_now=True)

    def tag(self):
        return [FAMILY_MEMBER.display_label(tag_key) for tag_key in self.tags]

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

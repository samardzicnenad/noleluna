import markdown
from django.db import models
from markdownx.models import MarkdownxField
from markdownx.settings import MARKDOWNX_MARKDOWN_EXTENSIONS, MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS
from multiselectfield import MultiSelectField
from utils.enums import BLOG_POST_STATE, FAMILY_MEMBER


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = MarkdownxField()
    image = models.ImageField(blank=True)
    state = models.IntegerField(choices=BLOG_POST_STATE.choices(), default=BLOG_POST_STATE.DRAFT.value)
    tags = MultiSelectField(choices=FAMILY_MEMBER.choices(), null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_edited_on = models.DateTimeField(auto_now=True)

    def tag(self):
        return [FAMILY_MEMBER.display_label(tag_key) for tag_key in self.tags]

    def full_tags(self):
        full_tags = {}
        for tag in self.tags:
            full_tags[int(tag)] = FAMILY_MEMBER.display_name(tag)
        return full_tags

    def display_content(self):
        return markdown.markdown(self.content,
                                 extensions=MARKDOWNX_MARKDOWN_EXTENSIONS,
                                 extension_configs=MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

from django.http import Http404
from django.shortcuts import render

from blog_post.models import BlogPost
from noleluna.settings import MEDIA_URL
from utils.enums import FAMILY_MEMBER, BLOG_POST_STATE


def family_member(request, member_id, related):
    if int(member_id) not in FAMILY_MEMBER.keys():
        raise Http404("This Samardzic family member does not exist")
    data = {
        'family_member_id': member_id,
        'family_member_first': FAMILY_MEMBER.display_name(member_id),
        'family_member_nick': FAMILY_MEMBER.display_label(member_id),
        'family_member_date': "{}/{}/{}".format(member_id[4:6], member_id[6:], member_id[:4]),
        'posts': BlogPost.objects.filter(state=BLOG_POST_STATE.PUBLISHED.value, tags__contains=member_id).order_by(
            '-last_edited_on'),
        'media_url': MEDIA_URL
    }
    return render(request, 'noleluna/related.html', data) if related else render(request, 'noleluna/bio.html', data)

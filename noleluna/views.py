from django.shortcuts import render

from utils.enums import FAMILY_MEMBER


def family_member(request, member_id, plus):
    data = {
        'family_member_id': member_id,
        'family_member_first': FAMILY_MEMBER.display_name(member_id).lower(),
        'family_member_nick': FAMILY_MEMBER.display_label(member_id).lower(),
        'family_member_date': "{}/{}/{}".format(member_id[4:6], member_id[6:], member_id[:4]),
    }
    if not plus:
        return render(request, 'noleluna/bio.html', data)
    else:
        return render(request, 'noleluna/plus.html', data)

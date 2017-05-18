from django.shortcuts import render

from . import SAMARDZICI


def family_member(request, member_id):
    data = {
        'family_member_id': member_id,
        'family_member_first': SAMARDZICI.get(member_id).get('name').lower(),
        'family_member_nick': SAMARDZICI.get(member_id).get('nickname').lower(),
        'family_member_date': "{}/{}/{}".format(member_id[4:6], member_id[6:], member_id[:4]),
    }
    return render(request, 'noleluna/bio.html', data)


def family_member_plus(request, member_id):
    data = {
        'family_member_id': member_id,
        'family_member_first': SAMARDZICI.get(member_id).get('name').lower(),
        'family_member_nick': SAMARDZICI.get(member_id).get('nickname').lower(),
        'family_member_date': "{}/{}/{}".format(member_id[4:6], member_id[6:], member_id[:4]),
    }
    return render(request, 'noleluna/plus.html', data)

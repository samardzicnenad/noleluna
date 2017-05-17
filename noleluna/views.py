from django.shortcuts import render

from . import SAMARDZICI


def family_member(request, member_id):
    data = {
        'family_member_id': member_id,
        'family_member_nick': SAMARDZICI.get(member_id).get('nickname').lower(),
    }
    return render(request, 'noleluna/bio.html', data)


def family_member_bio(request, member_id):
    data = {
        'family_member_id': member_id,
        'family_member_nick': SAMARDZICI.get(member_id).get('nickname').lower(),
    }
    return render(request, 'noleluna/bio.html', data)

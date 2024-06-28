from django.shortcuts import redirect
from django.http import HttpResponseRedirect


def change_theme(request, **kwargs):
    dark = request.session.get("is_dark_theme")
    request.session["is_dark_theme"] = not dark if "is_dark_theme" in request.session else True
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))

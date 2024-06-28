def theme(request):
    if "is_dark_theme" in request.session:
        return dict(is_dark_theme=request.session.get("is_dark_theme"))
    return dict(is_dark_theme=False)
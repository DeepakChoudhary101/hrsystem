def profile_name(request):
    if request.user.is_authenticated:
        if request.path == '/login/':  # Adjust the path to your login page
            return {}
        return {'profile_name': request.user}
    return {}

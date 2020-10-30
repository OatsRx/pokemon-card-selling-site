from django.shortcuts import render, get_object_or_404
from .models import UserProfile

def user_profile(request):
    """ A view to display the users profile """

    user_profile = get_object_or_404(UserProfile)
    context = {
        'user_profile': user_profile
    }
    return render(request, 'profiles/user_profile.html', context)


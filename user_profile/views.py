from django.shortcuts import render


def user_profile(request):
    """ A view to display the users profile """

    context = {

    }
    return render(request, 'user_profile/user_profile.html', context)
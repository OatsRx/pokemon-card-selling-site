from django.shortcuts import render

# Create your views here.


def index(request):
    """A view to render the shopping bag"""

    return render(request, 'shoppingbag/shopping_bag.html')


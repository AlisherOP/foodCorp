from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import Profile
from food.models import Item 
# Create your views here.


def register(request):
    if request.method == "POST":# when the username is posted
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()# saving the new account
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"Welcome {username}, you are currently logged in")
            return redirect('login')
    else:
        form = RegisterForm() 
    return render(request, "users/register.html", {'form': form})

@login_required# a decorator to add restrictions
def profilepage(request):
    return render(request, 'users/profiles.html')


@login_required
def favourite_add(request, id):
    post=get_object_or_404(Item, id=id)
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])

@login_required
def favourite_list(request):
    favourites= Item.objects.filter(favourites=request.user)
    tracker=0
    for fav in favourites:
        tracker = tracker+fav.item_cal
    return render(
        request, 'users/favourites.html', 
        {
        "favourites": favourites,
        "tracker":tracker
        }
    ) 

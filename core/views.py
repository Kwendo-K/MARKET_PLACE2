from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import logout


# Create your views here.
def home(request):
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)
    return render(request, "core/Home.html", {"categories": categories, "items": items})

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully")
            return redirect("home")
        messages.success(request, "An error occurred, please check your form and try again")
        form = SignUpForm()
    form = SignUpForm()
    return render(request, "core/Signup.html", {"form":form})

def logout_user(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect("home")



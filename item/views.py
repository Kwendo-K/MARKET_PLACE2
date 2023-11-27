from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from item.models import Item
from item.forms import AddItemForm

# Create your views here.
def view_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, "item/Item.html", {"item":item})

@login_required
def addItem(request):
    if request.method == "POST":
        form = AddItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Item added successfully")
        messages.success(request, "Invalid Data, try and fill the form again")
        form = AddItemForm()
    form = AddItemForm()
    return render(request, "item/AddItem.html", {"form":form})

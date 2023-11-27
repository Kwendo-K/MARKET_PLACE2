from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.view_item, name="viewItem"),
    path("addItem/", views.addItem, name="addItem"),
]
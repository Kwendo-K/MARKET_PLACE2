from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .forms import LoginForm

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", auth_view.LoginView.as_view(template_name="core/Login.html",authentication_form=LoginForm), name="login"),
    path("logout/", views.logout_user, name="logout")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
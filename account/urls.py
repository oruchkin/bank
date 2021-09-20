from django.urls import path
from . import views


urlpatterns = [    
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("login/", views.login_view, name="login"),
    path("profile/", views.profile, name="profile"),
    path("create_account/", views.create_account, name="create_account"),
    
    
]

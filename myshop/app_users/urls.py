from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.AnotherLogoutView.as_view(), name='logout'),
    path('registration/', views.register_view, name='register'),
    path('profile/', views.profile_edit, name='profile'),
]
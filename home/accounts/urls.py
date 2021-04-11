from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('accounts/login', LoginView.as_view(), name='login'),
    path('accounts/logout', LogoutView.as_view(), name='logout')
]
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import register_view, AddUser, UserDetailView, UserList, UserChangeView, UserPasswordChangeView

app_name = 'accounts'

urlpatterns = [
    path('accounts/login', LoginView.as_view(), name='login'),
    path('accounts/logout', LogoutView.as_view(), name='logout'),
    path('add_user_in_project/<int:pk>', AddUser.as_view(), name='add_user'),
    path('delete_user_in_project/<int:pk>', AddUser.as_view(), name='delete_user'),
    path('register/', register_view, name='register'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('users/', UserList.as_view(), name='user_list'),
    path('change/', UserChangeView.as_view(), name='change'),
    path('password_change/', UserPasswordChangeView.as_view(), name='password_change')
]
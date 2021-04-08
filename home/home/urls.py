"""home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views.project import ProjectList, ProjectCreate, ProjectView, ProjectDelete, ProjectEdit
from webapp.views.task import TaskCreate, TaskEdit, TaskView, TaskDelete
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProjectList.as_view(), name='home' ),
    path('create/project/', ProjectCreate.as_view(), name='create'),
    path('view/<int:pk>/project/', ProjectView.as_view(), name='view'),
    path('delete/<int:pk>/project/', ProjectDelete.as_view(), name='delete'),
    path('<int:pk>/create/task/', TaskCreate.as_view(), name='create_task'),
    path('view/task/<int:pk>/', TaskView.as_view(), name='view_task'),
    path('delete/task/<int:pk>/', TaskDelete.as_view(), name='delete_task'),
    path('edit/task/<int:pk>/', TaskEdit.as_view(), name='edit_task'),
    path('edit/<int:pk>/project', ProjectEdit.as_view(), name='edit'),
    path('accounts/login', LoginView.as_view(), name='login'),
    path('accounts/logout', LogoutView.as_view(), name='logout')

]

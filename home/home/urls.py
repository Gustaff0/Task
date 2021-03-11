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
from webapp.views import List_tasks, Create_task, Edit_task, View_task, Delete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', List_tasks.as_view(), name='home' ),
    path('create/', Create_task.as_view(), name='create'),
    path('edit/<int:pk>/', Edit_task.as_view(), name='edit'),
    path('view/<int:pk>/', View_task.as_view(), name='view'),
    path('delete/<int:pk>', Delete_task.as_view(), name='delete')

]

from django.urls import path
from webapp.views.project import ProjectList, ProjectCreate, ProjectView, ProjectDelete, ProjectEdit
from webapp.views.task import TaskCreate, TaskEdit, TaskView, TaskDelete

urlpatterns = [
    path('', ProjectList.as_view(), name='home' ),
    path('create/project/', ProjectCreate.as_view(), name='create'),
    path('view/<int:pk>/project/', ProjectView.as_view(), name='view'),
    path('delete/<int:pk>/project/', ProjectDelete.as_view(), name='delete'),
    path('<int:pk>/create/task/', TaskCreate.as_view(), name='create_task'),
    path('view/task/<int:pk>/', TaskView.as_view(), name='view_task'),
    path('delete/task/<int:pk>/', TaskDelete.as_view(), name='delete_task'),
    path('edit/task/<int:pk>/', TaskEdit.as_view(), name='edit_task'),
    path('edit/<int:pk>/project', ProjectEdit.as_view(), name='edit')

]
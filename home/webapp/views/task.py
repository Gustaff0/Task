from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from webapp.models import Task, Project
from webapp.forms import TaskForm, SearchForm
from webapp.base_views import FormView as CustomFormView
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.utils.http import urlencode
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.

# class TaskList(ListView):
#     template_name = 'task/list.html'
#     model = Task
#     context_object_name = 'tasks'
#     ordering = ('summary', '-created_at')
#     paginate_by = 10
#     paginate_orphans = 2
#
#     def get(self, request, **kwargs):
#         self.form = SearchForm(request.GET)
#         self.search_data = self.get_search_data()
#         return super(List_tasks, self).get(request, **kwargs)
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#
#         if self.search_data:
#             queryset = queryset.filter(
#                 Q(summary__icontains=self.search_data) |
#                 Q(description__icontains=self.search_data)
#             )
#         return queryset
#
#     def get_search_data(self):
#         if self.form.is_valid():
#             return self.form.cleaned_data['search_value']
#         return None
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['search_form'] = self.form
#         if self.search_data:
#             context['query'] = urlencode({'search_value': self.search_data})
#         return context


class TaskCreate(PermissionRequiredMixin, CreateView):
    model = Task
    template_name = 'task/create.html'
    form_class = TaskForm
    permission_required = 'webapp.add_task'

    def has_permission(self):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        return super().has_permission() and self.request.user in project.user.all()

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        form.save_m2m()
        return redirect('webapp:view_task', pk=task.pk)




class TaskEdit(PermissionRequiredMixin, UpdateView):
    model = Task
    template_name = 'task/edit.html'
    form_class = TaskForm
    context_object_name = 'task'
    permission_required = 'webapp.change_task'

    def has_permission(self):
        # task = get_object_or_404(Task, pk=self.kwargs.get('pk'))
        task = self.get_object()
        return super().has_permission() and self.request.user in task.project.user.all()

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:view_task', kwargs={'pk': self.object.pk})



class TaskView(PermissionRequiredMixin, DetailView):
    model = Task
    template_name = 'task/view.html'
    permission_required = 'webapp.view_task'

    def has_permission(self):
        task = self.get_object()
        return super().has_permission() and self.request.user in task.project.user.all()


class TaskDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'task/delete.html'
    model = Task
    context_object_name = 'task'
    permission_required = 'webapp.delete_task'

    def has_permission(self):
        task = self.get_object()
        return super().has_permission() and self.request.user in task.project.user.all()

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:view', kwargs={'pk': self.object.project.pk})


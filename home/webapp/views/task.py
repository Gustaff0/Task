from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from webapp.models import Task, Project
from webapp.forms import TaskForm, SearchForm
from webapp.base_views import FormView as CustomFormView
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.utils.http import urlencode
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


class TaskCreate(CreateView):
    model = Task
    template_name = 'task/create.html'
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        form.save_m2m()
        return redirect('view_task', pk=task.pk)




class TaskEdit(UpdateView):
    model = Task
    template_name = 'task/edit.html'
    form_class = TaskForm
    context_object_name = 'task'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('view_task', kwargs={'pk': self.object.pk})



class TaskView(DetailView):
    model = Task
    template_name = 'task/view.html'


class TaskDelete(DeleteView):
    template_name = 'task/delete.html'
    model = Task
    context_object_name = 'task'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('view', kwargs={'pk': self.object.project.pk})


from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, CreateView, DetailView, UpdateView, DeleteView
from webapp.models import Project
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from webapp.forms import ProjectForm, SearchForm, TaskForm
from webapp.models import Project, Task
from django.db.models import Q
from django.utils.http import urlencode
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import User

class ProjectCreate(PermissionRequiredMixin, CreateView):
    template_name = 'project/create.html'
    form_class = ProjectForm
    model = Project
    permission_required = 'webapp.add_project'

    def form_valid(self, form):
        user = self.request.user
        project = form.save()
        project.user.add(user)
        return redirect('webapp:view', pk=project.pk)


    # def get_success_url(self):
    #     return reverse('webapp:view', kwargs={'pk' : self.object.pk})



class ProjectList(ListView):
    template_name = 'project/list.html'
    model = Project
    context_object_name = 'projects'
    ordering = ('name', '-timestart')
    paginate_by = 10
    paginate_orphans = 2

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(ProjectList, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(name__icontains=self.search_data) |
                Q(description__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})

        return context


class ProjectEdit(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'project/edit.html'
    form_class = ProjectForm
    context_object_name = 'project'
    permission_required = 'webapp.change_project'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:view', kwargs={'pk': self.object.pk})



class ProjectView(DetailView):
    model = Project
    template_name = 'project/view.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)


class ProjectDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'project/delete.html'
    model = Project
    context_object_name = 'project'
    success_url = reverse_lazy('webapp:home')
    permission_required = 'webapp.delete_project'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().user.all()


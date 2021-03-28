from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, CreateView, DetailView
from webapp.models import Project
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from webapp.forms import ProjectForm, SearchForm, TaskForm
from webapp.models import Project, Task
from django.db.models import Q
from django.utils.http import urlencode

class ProjectCreate(CreateView):
    template_name = 'project/create.html'
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse('project/view', kwargs={'pk' : self.kwargs.get('pk')})

    def form_valid(self, form):
        project = get_object_or_404(Project, id=self.kwargs.get('pk'))
        form.instance.project = project
        return super().form_valid(form)

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



class ProjectView(DetailView):
    model = Project
    template_name = 'project/view.html'


class ProjectDelete(View):
    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, id=kwargs.get('pk'))
        return render(request, 'project/delete.html', {'project': project})
    def post(self, request, *args, **kwargs):
        project = get_object_or_404(Project, id=kwargs.get('pk'))
        project.delete()
        return redirect('home')
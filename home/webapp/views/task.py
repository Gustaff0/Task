from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, RedirectView, FormView, ListView
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from webapp.models import Task
from webapp.forms import TaskForm, SearchForm
from webapp.base_views import FormView as CustomFormView
from django.urls import reverse
from django.db.models import Q
from django.utils.http import urlencode
# Create your views here.

class TaskList(ListView):
    template_name = 'task/list.html'
    model = Task
    context_object_name = 'tasks'
    ordering = ('summary', '-created_at')
    paginate_by = 10
    paginate_orphans = 2

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(List_tasks, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(summary__icontains=self.search_data) |
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


class TaskCreate(CustomFormView):
    template_name = 'task/create.html'
    form_class = TaskForm
    redirect_url = 'home'

    def form_valid(self, form):
        type = form.cleaned_data.pop('type')
        task = Task()
        for key, value in form.cleaned_data.items():
            setattr(task, key, value)

        task.save()
        task.type.set(type)

        return super().form_valid(form)


class TaskEdit(FormView):
    template_name = 'task/edit.html'
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.task
        return kwargs

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view', kwargs={'pk': self.task.pk})

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Task, pk=pk)



class TaskView(View):
    def get(self, request, *args, **kwargs):
        try:
            task = get_object_or_404(Task, id=kwargs.get('pk'))
        except:
            raise Http404
        return render(request, 'task/view.html', {'task':task})


class TaskDelete(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs.get('pk'))
        return render(request, 'task/delete.html', {'task': task})
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs.get('pk'))
        task.delete()
        return redirect('home')
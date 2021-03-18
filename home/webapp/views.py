from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, RedirectView, FormView
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from webapp.models import Task
from webapp.forms import TaskForm
from webapp.base_views import FormView as CustomFormView
from django.urls import reverse
# Create your views here.

class List_tasks(TemplateView):
    template_name='list.html'

    def get_context_data(self, **kwargs):
        kwargs['tasks'] = Task.objects.all()
        return super().get_context_data(**kwargs)


class Create_task(CustomFormView):
    template_name = 'create.html'
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


class Edit_task(FormView):
    template_name = 'edit.html'
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



class View_task(View):
    def get(self, request, *args, **kwargs):
        try:
            task = get_object_or_404(Task, id=kwargs.get('pk'))
        except:
            raise Http404
        return render(request, 'view.html', {'task':task})


class Delete_task(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs.get('pk'))
        return render(request, 'delete.html', {'task': task})
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs.get('pk'))
        task.delete()
        return redirect('home')



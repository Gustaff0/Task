from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, RedirectView
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from webapp.models import Task
from webapp.forms import TaskForm
# Create your views here.

class List_tasks(TemplateView):
    template_name='list.html'

    def get_context_data(self, **kwargs):
        kwargs['tasks'] = Task.objects.all()
        return super().get_context_data(**kwargs)


class Create_task(View):
    def get(self, request, *args, **kwargs):
        form= TaskForm()
        return render(request, 'create.html', {'form':form})
    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            summary = form.cleaned_data.get('summary')
            description = form.cleaned_data.get("description")
            status = form.cleaned_data.get('status')
            type = form.cleaned_data.get('type')
            task = Task.objects.create(
                summary=summary,
                description=description,
                status=status
            )
            task.type.set(type)
            return redirect('home')
        else:
            return render(request, 'create.html', {'form': form})


class Edit_task(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs.get('pk'))
        form = TaskForm(initial={
            'summary': task.summary,
            'description': task.description,
            'status': task.status,
            'type': task.type
        })
        return render(request, 'edit.html', context={'form': form, 'task': task})
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs.get('pk'))
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.summary = form.cleaned_data['summary']
            task.description = form.cleaned_data['description']
            task.status = form.cleaned_data['status']
            task.type = form.cleaned_data['type']
            task.save()
            return redirect('home')
        else:
            return render(request, 'edit.html', context={'form': form, 'task': task})


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



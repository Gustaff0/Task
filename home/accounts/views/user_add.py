from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, CreateView, DetailView, UpdateView, DeleteView
from webapp.models import Project
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from accounts.forms import MyUserUpdate
from webapp.models import Project, Task
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User


class AddUser(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'user_add.html'
    form_class = MyUserUpdate
    context_object_name = 'project'
    permission_required = 'webapp.user_add_or_del'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().user.all()


    def get_success_url(self):
        return reverse('webapp:view', kwargs={'pk': self.object.pk})






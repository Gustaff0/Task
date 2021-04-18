from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import MyUserCreationForm
from accounts.models import Profile

# Create your views here.

# def login_view(request):
#     context = {}
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('home')
#         else:
#             context['has_error'] = True
#     return render(request, 'login.html', context=context)
#
#
# def logout_view(request):
#     logout(request)
#     return redirect('home')

def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            user.save()
            Profile.objects.create(user=user)
            return redirect('webapp:home')
    else:
        form = MyUserCreationForm()
    return render(request, 'user_create.html', context={'form': form})





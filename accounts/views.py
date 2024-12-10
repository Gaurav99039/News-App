from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CustomCreationForm
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
# Create your views here.

class SignUpView(CreateView):
    form_class = CustomCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def custom_logout_view(request):
    logout(request)
    return redirect('home')



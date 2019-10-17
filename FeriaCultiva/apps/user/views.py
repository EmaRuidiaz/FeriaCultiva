from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import User

# Create your views here.

class CreateUser(CreateView):
    model = User
    template_name = 'user/registro.html'
    succes_url = reverse_lazy('home.html')
    fields = ['username','password', 'email', 'first_name', 'last_name', 'direccion', 'telefono']

class UpdateUser(UpdateView):
    model = User
    template_name = ''
    fields = ['password', 'email', 'first_name', 'last_name', 'direccion', 'telefono']

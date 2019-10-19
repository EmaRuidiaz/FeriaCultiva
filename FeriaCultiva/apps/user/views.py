from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import User
from apps.user.forms import RegistroForm


# Create your views here.

class CreateUser(CreateView):
    model = User
    template_name = 'user/registro.html'
    #form_class = RegistroForm
    succes_url = reverse_lazy('home.html')
    fields = ['username','first_name','last_name','email','password','direccion']


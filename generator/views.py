from django.shortcuts import render
# from django.http import HttpResponse
from random import choice

# Create your views here.
def about(request):
  return render(request, 'generator/about.html')


def home(request):
  return render(request, 'generator/home.html')


def password(request, *args, **kwargs):

  characters = list('abcdefghijklmnopqrstuvwxyz')
  generated_password = ''

  length = int(request.GET.get('length'))

  if request.GET.get('uppercase'):
    characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

  if request.GET.get('special'):
    characters.extend(list('.-_!¡#$%&/()=?¿*+]~'))
  
  if request.GET.get('numbers'):
    characters.extend(list('0123456789'))
  
  for character in range(length):
    generated_password += choice(characters)

  context={
    'password': generated_password,
  }

  return render(request, 'generator/password.html', context)
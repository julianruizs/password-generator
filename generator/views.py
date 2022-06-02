import numbers
from django.shortcuts import render
from django.http import HttpResponse

import random

# Create your views here.

def home(request):
    return render(request,'generator/index.html')

def password_generator(request):
    
    num_characters = int(request.GET.get('lenght'))

    letters = list('abcdefghijklmnopqrstuvwxyz')
    capital_letters =list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    special_characters = list('|!#$%&/()=?¡¿')
    numbers = list('1234567890')
    password =''

    if request.GET.get('uppercase'):
        letters.extend(capital_letters)
    if request.GET.get('special'):
        letters.extend(special_characters)
    if request.GET.get('numbers'):
        letters.extend(numbers)       

    for c in range(num_characters):
        password += random.choice(letters)

    return render(request,'generator/password.html',{'password':password})



""" def about(request):
    return HttpResponse('Hello world') """


from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method=="post":
        form= UserCreationForm(request.post)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, account created successfully')
            return redirect('home')
    else:
        form=UserCreationForm()
    return render(request , 'users/register.html', {'form': form})
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from .models import Users

def index(request):
    context = {
        "all_users": Users.objects.all()
    }
    return render(request, 'index.html', context)


def add_user(request):
    newUser = Users.objects.create(first_name=request.POST['first_name_input'], last_name=request.POST['last_name_input'], email_address=request.POST['email_input'], age=request.POST['age_input'])
    return redirect('/')
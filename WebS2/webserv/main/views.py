from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def index(request):
    return HttpResponse("<h2>Главная</h2>")


def user(request):
    message = request.GET.get("message")
    name = request.GET.get("name")
    return HttpResponse(f"<h2>Hello: {name},  {message}</h2>"
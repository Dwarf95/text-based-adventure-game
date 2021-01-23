from django.shortcuts import render


def index(request):
    title = "Hello World"
    return render(request, 'index.html')

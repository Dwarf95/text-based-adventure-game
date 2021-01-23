from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def intro(request):
    return render(request, 'intro.html')


def choose_path(request):
    return render(request, 'choose_path.html')


def path_mountain(request):
    return render(request, 'path_mountain.html')


def path_mountain_first_choice(request):
    return render(request, 'path_mountain_first_choice.html')


def path_slow_river(request):
    return render(request, 'path_slow_river.html')
from django.shortcuts import render


def index(request):
    return render(request, "index.html", locals())


def play(request):
    return render(request, "play.html", locals())

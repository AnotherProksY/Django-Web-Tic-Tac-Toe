from django.shortcuts import render

def index(request):
    return render(request, "index.html", locals())

def game(request):
    return render(request, "game.html", locals())

def score(request):
    return render(request, "score.html", locals())

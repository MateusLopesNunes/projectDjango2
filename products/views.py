from django.shortcuts import render
from django.shortcuts import render, get_object_or_404


def index(request):
    render(request, 'index.html')

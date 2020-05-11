from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

def index(request):
    return render(request, 'home_page/index.html')
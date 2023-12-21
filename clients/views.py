from django.shortcuts import render
from django.http import HttpResponse

def clients(request):
    return render (request, 'clients.html')
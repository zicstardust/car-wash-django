from django.shortcuts import render
from django.http import HttpResponse
from .models import Car, Client
import re

def clients(request):
    if request.method == "GET":
        return render (request, 'clients.html')
    elif request.method == "POST":
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')

        cars = request.POST.getlist('car')
        plates = request.POST.getlist('plate')
        years = request.POST.getlist('year')

        client = Client.objects.filter(cpf=cpf)

        if client.exists():
            return render (request, 'clients.html', {'name': name, 'lastname': lastname, 'email': email, 'cars': zip(cars, plates, years)})

        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            return render (request, 'clients.html', {'name': name, 'lastname': lastname, 'cpf': cpf, 'cars': zip(cars, plates, years)})

        client = Client(
            name = name,
            lastname = lastname,
            email = email,
            cpf = cpf
        )
        client.save()

        for car, plate, year in zip(cars, plates, years):
            car = Car(
                car = car,
                plate = plate,
                year = year,
                client = client
            )
            car.save()

        return HttpResponse("Sucessful Register")
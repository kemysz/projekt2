from django.shortcuts import render
from .models import Room, Computer, Parameter

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

def computer_list(request, room_id):
    room = Room.objects.get(id=room_id)
    computers = Computer.objects.filter(room=room)
    return render(request, 'computer_list.html', {'room': room, 'computers': computers})

def parameter_list(request, computer_id):
    computer = Computer.objects.get(id=computer_id)
    parameters = Parameter.objects.filter(computer=computer)
    return render(request, 'parameter_list.html', {'computer': computer, 'parameters': parameters})
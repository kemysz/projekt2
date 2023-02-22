from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Computer(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    num_apps = models.IntegerField()
    status = models.CharField(max_length=100)

class Parameter(models.Model):
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

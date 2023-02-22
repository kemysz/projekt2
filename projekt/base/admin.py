from django.contrib import admin
from .models import Computer
from .models import Parameter
from .models import Room

admin.site.register(Computer)
admin.site.register(Parameter)
admin.site.register(Room)


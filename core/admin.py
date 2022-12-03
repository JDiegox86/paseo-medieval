from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Roles)
admin.site.register(Productos)
admin.site.register(RegistroClienteTienda)
admin.site.register(Tiendas)
admin.site.register(Ventas)

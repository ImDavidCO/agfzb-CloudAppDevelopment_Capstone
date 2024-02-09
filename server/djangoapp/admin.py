from django.contrib import admin
from .models import CarMake, CarModel

class CarModelInline(admin.TabularInline):
    model = CarModel

class CarModelAdmin(admin.ModelAdmin):
    # Configuración adicional para CarModel en la interfaz de administración
    list_display = ['name', 'car_make', 'dealer_id', 'type', 'year']
    search_fields = ['name', 'car_make__name']

class CarMakeAdmin(admin.ModelAdmin):
    # Configuración adicional para CarMake en la interfaz de administración
    list_display = ['name', 'description']
    inlines = [CarModelInline]

# Registra los modelos y las clases administrativas
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)

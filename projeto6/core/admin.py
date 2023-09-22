from django.contrib import admin


# Register your models here.
from .models import Chassi, Carro, Montadora


@admin.register(Montadora)
class MontadoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
    list_display = ('numero',)


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ( 'modelo', 'montadora', 'chassi', 'preco')

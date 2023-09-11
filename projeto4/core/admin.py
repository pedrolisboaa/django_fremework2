from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

# Register your models here.
from .models import Postagem

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor']
    exclude = ['autor',]

    def _autor(self, instance):
        return f'{instance.autor.get_full_name()}'
    
    def get_queryset(self, request):
        qs = super(PostagemAdmin, self).get_queryset(request)
        return qs.filter(autor=request.user)
    
    def save_model(self, request: Any, obj: Any, form: Any, change: Any):
        obj.autor = request.user
        return super().save_model(request, obj, form, change)
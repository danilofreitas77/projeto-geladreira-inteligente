from django.contrib import admin
from .models import item

@admin.register(item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('produto', 'categoria', 'quantidade', 'valor')

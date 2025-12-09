from django.contrib import admin
from django.utils.html import format_html
from .models import Plant

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    # Columnas visibles en la tabla del admin
    list_display = [
        'name',
        'water',
        'light',
        'fertilizer',
        'location',
        'maintenance',
        'mostrar_foto',
    ]
    # Campos por los que se puede buscar
    search_fields = ['name', 'notes']
    # Filtros laterales
    list_filter = ['water', 'light', 'location', 'maintenance']

    # Miniatura de la foto en la tabla
    def mostrar_foto(self, obj):
        if obj.image_file:
            return format_html('<img src="{}" width="50" height="50" />', obj.image_file.url)
        elif obj.image_url:
            return format_html('<img src="{}" width="50" height="50" />', obj.image_url)
        return "Sin foto"
    mostrar_foto.short_description = "Foto"

    # Permisos CRUD (se aplican automáticamente según el usuario)
    def has_add_permission(self, request):
        return request.user.has_perm('planta.add_plant')

    def has_change_permission(self, request, obj=None):
        return request.user.has_perm('planta.change_plant')

    def has_delete_permission(self, request, obj=None):
        return request.user.has_perm('planta.delete_plant')

    def has_view_permission(self, request, obj=None):
        return request.user.has_perm('planta.view_plant')

from django.contrib import admin
from .models import Tarefa


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ("done", "date_time", "usuario")
    exclude = ("usuario",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(usuario=request.user)

    def save_model(self, request, obj, form, change):
        if not getattr(obj, "usuario_id", None):
            obj.usuario = request.user
        super().save_model(request, obj, form, change)

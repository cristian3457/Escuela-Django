from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Carrera, Coordinador

class UsuarioAdmin(UserAdmin):
    UserAdmin.fieldsets = (
        (None,{'fields':('username', 'password')}),
        ('Información del Usuario', {'fields':('email','tipo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username','email', 'tipo')
    # add_fieldsets = (
    #     (None,{
    #     'classes':('wide',),
    #     'fields': ('estatus','tipo')}
    # ),
    # )

class Admin_coordinador(admin.ModelAdmin):
    list_display = ('nombre','apellidos','carrera')

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Carrera)
admin.site.register(Coordinador, Admin_coordinador)
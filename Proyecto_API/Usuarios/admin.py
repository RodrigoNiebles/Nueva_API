from django.contrib import admin
from django.contrib.auth.models import Group
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from  django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from Usuarios.models import Usuario


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)


    class Meta:
        model = Usuario
        fields = ('email',)
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user       



class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = ('email', 'nombres', 'apellidos', 'password', 'is_active', 'is_admin')


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm 

    list_display = ('email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')} ),
        ('pesonal info', {'fields': ('nombres', 'apellidos',)}),
        ('permission', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nombres', 'apellidos', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',) 
    ordering = ('email',)
    filter_horizontal = ()      


admin.site.register(Usuario, UserAdmin)

admin.site.unregister(Group)
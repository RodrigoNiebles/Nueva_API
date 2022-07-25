from email.mime import image
from tkinter import Image
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user (self, email, username, nombres, apellidos, password=None):
        if not email:
            raise ValueError("El usuario debe tener una direccion de correo electronico")

        user = self.model(
            username = username, 
            email= self.normalize_email(email),
            nombres = nombres,
            apellidos = apellidos
        )

        user.set_password(password)
        user.save(using=self._db)
        return user    


    def create_superuser(self, username, email, nombres, apellidos, password):
        user = self.create_user(
            email,
            username=username,
            nombres = nombres,
            apellidos = apellidos,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user



class Usuario(AbstractBaseUser):
    username = models.CharField ("Nombre de usuario", unique=True, max_length=100)
    email = models.EmailField ("Correo electronico", unique=True, max_length= 250)
    nombres = models.CharField ("Nombres", blank=True, max_length=200, null=True)
    apellidos = models.CharField ("Apellidos", blank=True, max_length=200, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos']


    def __str__(self):
        return f'{self.nombres},{self.apellidos}'

    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self, app_label):
        return True         

    @property
    def is_staff(self):
        return self.is_admin    





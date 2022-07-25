from email import message
import json
from django.shortcuts import render
from django.http import JsonResponse
#from django.contrib.auth.forms import UserCreationForm
from django.views import View
from .models import Usuario, MyUserManager
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class Registro(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, username=0):
        if (username>0):
            registro = list(Usuario.objects.filter(username=username).values())
            if len(registro) > 0:
                regist = registro[0]
                datos={'message':"Success", 'registro': regist}
            else:datos={'message':"Usuario not found..."} 
            return JsonResponse(datos)    
        else:
            registro = list(Usuario.objects.values())
            if len(registro)>0:
                datos={'message':"Success", 'registro': registro}
            else:
                datos={'message':"registro not found..."} 
            return JsonResponse(datos)


    def post(self, request):
        jd = json.load(request.body)
        Usuario.objects.create(username=jd['username'], email=jd['email'], nombres=jd['nombres'], apellidos=jd['apellidos'])
        datos={'message':"Success"}
        return JsonResponse(datos)


    def put(self,request,username):
        jd=json.loads(request.body)
        registro=list(Usuario.objects.filter(username=username).values())
        if len(registro) > 0:
            usuario=Usuario.objects.get(username=username)
            usuario.username=jd['username']
            usuario.email=jd['email']
            usuario.nombres=jd['nombres']
            usuario.apellidos=jd['apellidos']
            usuario.save()
            datos={'message':"Success"}
        else:
            datos={'message':"registro not found..."}
        return JsonResponse(datos)     


    def delete(self,request, username):
        registro=list(Usuario.objects.filter(username=username).values())
        if len (registro)>0:
            Usuario.objects.filter(username=username).delete()
            datos={'message':"Success"}
        else:
            datos={'message':"registro not found..."}
        return JsonResponse(datos)











    #def register(request):
    #    if request.method == 'POST':
    #        form = UserCreationForm(request.POST)
    #        if form.is_valid():
    #            username = form.cleaned_data['username']
    #            message.success(request, f'Usuario {username} creado')
    #    else:
    #        form = UserCreationForm()
    #    context = {'form' : form}
    #    return render(request, 'usuarios/register.html', context)           


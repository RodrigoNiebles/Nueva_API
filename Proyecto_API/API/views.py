from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Peliculas
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

# Create your views here.


class PelisView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self,request,ID=0):
        if (ID>0):
            peliss=list(Peliculas.objects.filter(ID=ID).values())
            if len(peliss) > 0:
                peli=peliss[0]
                datos={'message':"Success", 'peliss': peli}
            else:
                datos={'message':"Pelis not found..."} 
            return JsonResponse(datos)
        else:
            peliss=list(Peliculas.objects.values())
            if len(peliss)>0:
                datos={'message':"Success", 'peliss': peliss}
            else:
                datos={'message':"Pelis not found..."} 
            return JsonResponse(datos)
               

    def post(self,request):
        #print(request.body)
        jd=json.loads(request.body)
        Peliculas.objects.create(ID=jd['ID'], Title=jd['Title'], Duration=jd['Duration'], Premiere=jd['Premiere'])
        datos={'message':"Success"}
        return JsonResponse(datos) 

    def put(self,request,ID):
        jd=json.loads(request.body)
        peliss=list(Peliculas.objects.filter(ID=ID).values())
        if len(peliss) > 0:
            peliculas=Peliculas.objects.get(ID=ID)
            peliculas.ID=jd['ID']
            peliculas.Title=jd['Title']
            peliculas.Duration=jd['Duration']
            peliculas.Premiere=jd['Premiere']
            peliculas.save()
            datos={'message':"Success"}
        else:
            datos={'message':"Pelis not found..."}
        return JsonResponse(datos)     

        

    def delete(self,request,ID):
        peliss=list(Peliculas.objects.filter(ID=ID).values())
        if len(peliss) > 0:
            Peliculas.objects.filter(ID=ID).delete()
            datos={'message':"Success"}
        else:
            datos={'message':"Pelis not found..."}
        return JsonResponse(datos)    
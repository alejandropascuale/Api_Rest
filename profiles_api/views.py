from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    # API View de prueba
    def get(self, request, format=None):
        # Retornar lista de caracteristicas del API View
        an_apiview = [
            'Usamos metodos HTTP como funciones (get, post, patch, put, delete',
            'similar a una vista tradicional en Django',
            'Nos da el mayor control sobre la logica de nuestra aplicacion',
            'Esta mapeado manualmentea a las URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
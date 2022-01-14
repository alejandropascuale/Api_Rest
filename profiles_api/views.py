from email import message
import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializer

class HelloApiView(APIView):
    # API View de prueba

    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        # Retornar lista de caracteristicas del API View
        an_apiview = [
            'Usamos metodos HTTP como funciones (get, post, patch, put, delete',
            'similar a una vista tradicional en Django',
            'Nos da el mayor control sobre la logica de nuestra aplicacion',
            'Esta mapeado manualmentea a las URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        # Crea un mensaje con nuestro nombre
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
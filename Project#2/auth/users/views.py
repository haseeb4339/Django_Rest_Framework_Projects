from django.shortcuts import render

from rest_framework.views  import APIView
from .serializers import UserSerializer
from rest_framework.response import Response

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)


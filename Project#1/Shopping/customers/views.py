from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Customer
from .serializers import CustomerSerializer

def custormer_list(request):

    if request.method == "GET":



        customers = Customer.objects.all()

        serializer = CustomerSerializer(customers, many=True)

        return JsonResponse(serializer.data, safe=False)
    
    if request.method == "POST":

        data = JSONParser().parse(request)
        serializer = CustomerSerializer(data=data)

        if serializer.is_valid():

            serializer.save()

            return JsonResponse(serializer.data , status = 201)
        
        return JsonResponse(serializer.errors, status = 400)
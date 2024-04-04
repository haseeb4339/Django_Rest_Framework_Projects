from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Customer
from .serializers import CustomerSerializer

def custormer_list(request):

    customers = Customer.objects.all()

    serializer = CustomerSerializer(customers, many=True)

    return JsonResponse(serializer.data)
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404


class CustomerList(APIView):

    def get(self, request):

        
        customers = Customer.objects.all()

        serializer = CustomerSerializer(customers, many=True)

        return Response(serializer.data)
    

    def put(self, request):

        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data , status = 201)
        
        return Response(serializer.errors, status = 400)



# @api_view(['GET', 'POST'])
# def custormer_list(request):

#     if request.method == "GET":



#         customers = Customer.objects.all()

#         serializer = CustomerSerializer(customers, many=True)

#         return Response(serializer.data)
    
#     if request.method == "POST":

#         # data = JSONParser().parse(request)
#         serializer = CustomerSerializer(data=request.data)

#         if serializer.is_valid():

#             serializer.save()

#             return Response(serializer.data , status = 201)
        
#         return Response(serializer.errors, status = 400)
    


class CustomerDetail(APIView):
    def get_customer(self, pk):
        try:
            return Customer.objects.get(id=pk)
        
        except Customer.DoesNotExist:
            raise Http404
        

    def get(self, request, pk):

        customer = self.get_customer(pk)

        serializer = CustomerSerializer(customer)

        return Response(serializer.data)
    

    def put(self, request, pk):

        customer = self.get_customer(pk)
        serializer = CustomerSerializer(customer, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        

        return Response(serializer.errors, status = 400)
    

    def delete(self, request, pk):
        customer = self.get_customer(pk)
        customer.delete()

        return Response("delete sucssfully", status=204)



        

# @api_view(['GET', 'PUT', 'DELETE'])
# def customer_details(request, pk):

#     try:

#         customer = Customer.objects.get(id=pk)

#     except Customer.DoesNotExist:
#         return Response('not found!')
    
#     if request.method == "GET":

#         serializer = CustomerSerializer(customer)

#         return Response(serializer.data)
    
#     if request.method == "PUT":

#         # data = JSONParser().parse(request)

#         serializer = CustomerSerializer(customer, data=request.data)

#         if serializer.is_valid():

#             serializer.save()

#             return Response(serializer.data)
        
#         return Response(serializer.errors, status=401)
    
#     if request.method == "DELETE":
#         customer.delete()

#         return Response("delete sucssfully", status=204)

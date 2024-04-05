from django.urls import path

# from .views import custormer_list, customer_details
from .views import CustomerList, CustomerDetail


urlpatterns = [
    # path('', custormer_list),
    path('', CustomerList.as_view()),
    # path('<pk>/',customer_details ),
     path('<pk>/',CustomerDetail.as_view()),
]

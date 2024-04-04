from django.urls import path

from .views import custormer_list, customer_details


urlpatterns = [
    path('', custormer_list),
    path('<pk>/',customer_details ),
]

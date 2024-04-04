from django.urls import path

from .views import custormer_list


urlpatterns = [
    path('', custormer_list),
]

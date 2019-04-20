from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {})


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10
    }
    return JsonResponse(data)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
        default_items = [User.objects.all().count(), 2, 12, 2, 9, 1]
        data = {
            'labels': labels,
            "default": default_items
        }
        return Response(data)


# 3 sposoby na wysyłanie danych do frontendu
# najlepszym sposobem jest użycie DRF
# DRF daje nam funkcjonalności taki jak authentication oraz permission
# używając DRF również możemy przesyłać querysety np. User.objects.all()

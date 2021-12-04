import json

from django.views import View
from django.http import JsonResponse

from products.models import (
    Menu,
    Category,
    Product,
    Image,
    Allergy,
)

class MenuView(View):
    def get(self, request):
        menu = list(Menu.objects.values())
        
        return JsonResponse({'data':Menu}, status=200)

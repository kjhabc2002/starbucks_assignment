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
            
        return JsonResponse({'data':menu}, status=200)
    
    def post(self, request):
        data = json.loads(request.body)
        menu_name = data.get('name', None)
        print(menu_name)
        if not menu_name:
            return JsonResponse({'MESSAGE': 'KEY_ERROR'}, status=400)
        
        Menu.objects.create(name=menu_name)
        return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=200)
    
class CategoryView(View):
    def get(self, request):
        category = list(Category.objects.values())
            
        return JsonResponse({'data':category}, status=200)
    
    def post(self, request):
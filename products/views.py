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

        if not menu_name:
            return JsonResponse({'MESSAGE': 'KEY_ERROR'}, status=400)
        
        if Menu.objects.filter(name=data['name']).exists:
            return JsonResponse({'message': 'ALREADY_EXISTS'}, status=409)
        
        Menu.objects.create(name=menu_name)
        return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=200)
    
class CategoryView(View):
    def get(self, request):
            menu= list(Category.objects.values())
            
            return JsonResponse({'data' : menu}, status=200)
    
    def post(self,request):
            data = json.loads(request.body)
            menu_name=data.get('menu_name', None)
            category_name=data.get('name', None)
           
        
            if not (category_name and menu_name):
                return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status=400)
            
            if Category.objects.filter(name=category_name).exists():
                return JsonResponse({'MESSAGE' : 'ALREADY_EXISTS'}, status=400)
            
            if not Menu.objects.filter(name=menu_name).exists():
                return JsonResponse({'MESSAGE':'FOREIGN_KEY_DOES_NOT_EXIST'}, status=404)

            menu = Menu.objects.get(name=menu_name)
            
            Category.objects.create(
                    name=category_name,
                    menu=menu
            )
            return JsonResponse({'MESSAGE':'SUCEESS'}, status=201)
    

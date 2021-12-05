from django.urls import path
from .views      import MenuView,CategoryView

urlpatterns = [
    path('/menu', MenuView.as_view()),
    path('/category', CategoryView.as_view())  
]

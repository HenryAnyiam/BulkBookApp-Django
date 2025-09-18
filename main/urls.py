from django.urls import path
from main.views import index, category

app_name = 'main'

urlpatterns = [
    path('', index, name="home"),
    path('category', category, name="category")
]

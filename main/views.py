from django.shortcuts import render
from main.models import Category

# Create your views here.
def index(request):
    return render(request, 'index.html')

def category(request):
    category_obj = Category.objects.all()
    return render(request, "category.html", context={'categories': category_obj})

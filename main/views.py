from django.shortcuts import render
from main.models import Category

# Create your views here.
def index(request):
    category_obj = Category.objects.all()
    return render(request, "index.html", context={'categories': category_obj})

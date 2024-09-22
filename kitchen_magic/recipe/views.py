from django.shortcuts import render
from .models import Recipe
# Create your views here.

def Home(request):
    recipe_objs = Recipe.objects.all()
    data = {'recipess': recipe_objs}
    return render (request,'index.html',context=data)

def Create(request):
    return render (request,'create.html')

def Edit(request):
    return render (request,'edit.html')
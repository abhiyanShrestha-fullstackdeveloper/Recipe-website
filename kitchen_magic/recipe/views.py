from django.shortcuts import render,redirect
from .models import Recipe
# Create your views here.

def Home(request):
    recipe_objs = Recipe.objects.all()
    data = {'recipess': recipe_objs}
    return render (request,'index.html',context=data)

def Create(request):
    if request.method == "POST":
        picture = request.POST.get('picture')
        name = request.POST.get('name')
        category = request.POST.get('category')
        description =  request.POST.get('description')
        process = request.POST.get('process')
        ingredient =  request.POST.get('ingredient')
        
        Recipe.objects.create(picture=picture,name=name,category=category,description=description,process=process,ingredient=ingredient)
        return redirect('home')
    return render (request,'create.html')

def Edit(request):
    return render (request,'edit.html')
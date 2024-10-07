from django.shortcuts import render, redirect
from .models import Recipes
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import Recipe_Serializer
from .forms import RecipesForm
from django.contrib import messages
import requests
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import get_object_or_404


class RecipeCreate(generics.ListCreateAPIView):

    queryset = Recipes.objects.all()
    serializer_class = Recipe_Serializer
    permission_classes = [AllowAny]

class RecipeDetail(generics.RetrieveAPIView):

    queryset = Recipes.objects.all()
    serializer_class = Recipe_Serializer

class RecipeUpdate(generics.RetrieveUpdateAPIView):

    queryset = Recipes.objects.all()
    serializer_class = Recipe_Serializer

class RecipeDelete(generics.DestroyAPIView):

    queryset = Recipes.objects.all()
    serializer_class = Recipe_Serializer

class RecipeSearch(generics.ListAPIView):

    queryset = Recipes.objects.all()
    serializer_class = Recipe_Serializer

    def get_queryset(self):
        name = self.kwargs.get('Name')
        if name:
            return Recipes.objects.filter(Name__icontains=name)
        return Recipes.objects.none()

def CreateRecipe(request):

    if request.method == 'POST':
        form = RecipesForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                api_url = 'http://127.0.0.1:8000/create/'
                data = form.cleaned_data
                print(data)
                respose = requests.post(api_url, data=data, files={'Recipe_img': request.FILES['Recipe_img']})
                if respose.status_code == 400:
                    messages.success(request,'Recipe created successfully')
                    return redirect('index')
                else:
                    messages.error(request,f'Error!{respose.status_code}')
            except requests.RequestException as e:
                messages.error(request,f'Error during api request {str(e)}')
        else:
            messages.error(request,'Invalid Form')
    else:
        form = RecipesForm()
    return render(request,'create_recipe.html',{'form':form})

def DetailRecipe(request,id):

    api_url = f'http://127.0.0.1:8000/detail/{id}/'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
    return render(request,'detail_recipe.html',{'recipes':data})

def UpdateRecipe(request,id):

    recipe = get_object_or_404(Recipes, id=id)
    if request.method == 'POST':
        name = request.POST.get('Name')
        prep_time = request.POST.get('Prep_time')
        difficulty = request.POST.get('Difficulty')
        vegetarian = request.POST.get('Vegetarian') == 'on'
        recipe_img = request.FILES.get('Recipe_img')
        description = request.POST.get('Description')
        ingredients = request.POST.get('Ingredients')
        instructions = request.POST.get('Instructions')

        api_url = f'http://127.0.0.1:8000/update/{id}/'
        data = {
            'Name': name,
            'Prep_time': prep_time,
            'Difficulty': difficulty,
            'Vegetarian': vegetarian,
            'Description': description,
            'Ingredients': ingredients,
            'Instructions': instructions
        }
        files = {'Recipe_img': recipe_img} if recipe_img else None

        try:
            response = requests.put(api_url, data=data, files=files)
            if response.status_code == 200:
                messages.success(request, 'Recipe updated successfully.')
                return redirect('/')
            else:
                messages.error(request, f'Error submitting recipe {response.status_code}')
        except requests.RequestException as e:
            messages.error(request, f'Error during API request: {str(e)}')
    form = RecipesForm(instance=recipe)
    return render(request, 'update_recipe.html', {'form': form})

def index(request):
    search = request.GET.get('q', None)
    api_url = f'http://127.0.0.1:8000/search/{search}/' if search else 'http://127.0.0.1:8000/create/'
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            print("Fetched Data:", data)
            if search:
                return render(request, 'index.html', {'data': data})
            paginator = Paginator(data, 3)
            page = request.GET.get('page', 1)
            try:
                recipes = paginator.page(page)
            except (EmptyPage, InvalidPage):
                recipes = paginator.page(paginator.num_pages)
            context = {'recipes': recipes}
            return render(request, 'index.html', context)
        else:
            return render(request, 'index.html', {'error_message': f'Error: {response.status_code}'})
    except requests.RequestException as e:
        return render(request, 'index.html', {'error_message': f'Error: {str(e)}'})


def DeleteRecipe(request,id):

    api_url = f'http://127.0.0.1:8000/delete/{id}/'
    response = requests.delete(api_url)
    if response.status_code == 200:
        print(f'Item with id {id} has beendeleted')
    else:
        print(f'Failed to delete item {response.status_code}')
    return redirect('/')






























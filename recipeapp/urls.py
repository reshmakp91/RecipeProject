from django.urls import path
from .views import *
from recipeapp import views

urlpatterns = [
    path('create/', RecipeCreate.as_view(), name='create'),
    path('detail/<int:pk>/', RecipeDetail.as_view(),name='detail'),
    path('update/<int:pk>/', RecipeUpdate.as_view(),name='update'),
    path('delete/<int:pk>/', RecipeDelete.as_view(),name='delete'),
    path('search/<str:Name>/', RecipeSearch.as_view(),name='search'),

    path('', views.index,name='index'),
    path('create_recipe/', views.CreateRecipe, name='create_recipe'),
    path('recipe_detail/<int:id>/', views.DetailRecipe, name='recipe_detail'),
    path('update_recipe/<int:id>/', views.UpdateRecipe, name='update_recipe'),
    path('delete_recipe/<int:id>/',views.DeleteRecipe,name='delete_recipe')
]

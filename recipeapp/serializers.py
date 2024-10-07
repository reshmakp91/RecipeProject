from .models import Recipes
from rest_framework import serializers

class Recipe_Serializer(serializers.ModelSerializer):

    Recipe_img = serializers.ImageField(required=False)
    class Meta:
        model = Recipes
        fields = '__all__'
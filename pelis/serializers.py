# serializers.py
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import HyperlinkedModelSerializer


from .models import Pelicula

class PeliculaSerializer(ModelSerializer):
    class Meta:
        model = Pelicula
        fields = (
            'url', 'title', 'slug', 'rating', 'link', 'year', 'imagen', 'cast', 'generos'
        )

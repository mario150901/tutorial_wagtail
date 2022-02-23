from rest_framework.serializers import ModelSerializer
from .models import Pelicula

class PeliculaSerializer(ModelSerializer):
    class Meta:
        model = Pelicula
        fields = (
            'link', 'title', 'slug', 'rating', 'link', 'year', 'imagen', 'cast', 'generos'
        )
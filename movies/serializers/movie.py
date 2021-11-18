from django.db.models import fields
from rest_framework import serializers
from ..models import Movie, Ott


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title',)

class MovieSerializer(serializers.ModelSerializer):

    class OttSerializer(serializers.ModelSerializer):
        class Meta:
            model = Ott
            fields = ('id', 'name',)
    
    # valid 검사
    title = serializers.CharField(min_length=1, max_length=200)
    otts = OttSerializer(many=True)
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'otts',)


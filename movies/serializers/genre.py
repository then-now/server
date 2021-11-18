from rest_framework import serializers
from ..models import Movie, Track, Genre


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class GenreListSerializer(serializers.ModelSerializer):
    class TrackSerializer(serializers.ModelSerializer):
        class Meta:
            model = Track
            fields = (
                "id",
                "movie_id",
                "title",
                "track_path",
            )

        def to_representation(self, instance):
            response = super().to_representation(instance)
            response["movie_id"] = MovieSerializer(instance.movie_id).data
            return response

    tracks_genre = TrackSerializer(many=True)

    class Meta:
        model = Genre
        fields = (
            "id",
            "title",
            "tracks_genre",
        )

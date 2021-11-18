from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Movie, Movie_Ott, Ott, Track, Genre

# Register your models here.
class MovieAdmin(ImportExportMixin, admin.ModelAdmin):
    pass
admin.site.register(Movie, MovieAdmin)


class OttAdmin(ImportExportMixin, admin.ModelAdmin):
    pass
admin.site.register(Ott, OttAdmin)


class TrackAdmin(ImportExportMixin, admin.ModelAdmin):
    pass
admin.site.register(Track, TrackAdmin)


class Movie_OttAdmin(ImportExportMixin, admin.ModelAdmin):
    pass
admin.site.register(Movie_Ott, Movie_OttAdmin)


class GenreAdmin(ImportExportMixin, admin.ModelAdmin):
    pass
admin.site.register(Genre, GenreAdmin)

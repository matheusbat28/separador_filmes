from django.contrib import admin
from .models import Person, Movie, Average


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)
    
class AverageAdmin(admin.ModelAdmin):
    list_display = ('id_movie', 'id_person', 'average')
    list_display_links = ('id_movie', 'id_person', 'average')
    search_fields = ('id_movie', 'id_person', 'average')
    
admin.site.register(Person, PersonAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Average, AverageAdmin)

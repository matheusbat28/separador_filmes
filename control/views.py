from rest_framework import serializers, viewsets
from .models import Person, Movie, Average

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('name',)

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)
        
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
        
class AverageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Average
        fields = ('id_movie', 'id_person', 'average')
        
class AverageViewSet(viewsets.ModelViewSet):
    queryset = Average.objects.all()
    serializer_class = AverageSerializer
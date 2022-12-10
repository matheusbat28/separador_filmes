from rest_framework import serializers
from .models import Person, Movie, Average


class personSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
class AverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Average
        fields = '__all__'
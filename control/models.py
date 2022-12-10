from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        db_table = 'person'
        verbose_name = 'person'
        verbose_name_plural = 'people'
        
    def __str__(self):
        return self.name
        

class Movie(models.Model):
    title = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'movie'
        verbose_name = 'movie'
        verbose_name_plural = 'movies'
    
    def __str__(self):
        return self.title
    
    
class Average(models.Model):
    id_movie = models.ForeignKey(Movie, on_delete=models.CASCADE, db_column='id_movie', verbose_name='movie')
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE, db_column='id_person', verbose_name='person')
    average = models.FloatField()
    
    class Meta:
        db_table = 'average'
        verbose_name = 'average'
        verbose_name_plural = 'averages'
    
    def __str__(self):
        return self.average
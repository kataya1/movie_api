from django.db import models

# Create your models here.

class Production(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    budget = models.IntegerField(null=True, blank=True, default=0)
    poster = models.ImageField(upload_to="posters", null=True)
    cast = models.ForeignKey("Cast", related_name="productions", on_delete=models.DO_NOTHING, null=True, blank=True)
    category = models.ManyToManyField("Category", related_name="media", blank=True)

    
    def __str__(self):
        return self.title

class Seires(Production):
    num_of_episodes = models.IntegerField(null=True, blank=True)

class Movie(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    budget = models.IntegerField(null=True, blank=True, default=0)
    poster = models.ImageField(upload_to="posters", null=True)
    cast = models.ForeignKey("Cast", related_name="movies", on_delete=models.DO_NOTHING, null=True, blank=True)
    category = models.ManyToManyField("Category", related_name="movie", blank=True)
    
    def __str__(self):
        return self.title

class Cast(models.Model):
    number_of_people = models.IntegerField()
    def __str__(self):
        return f'{self.leader.name}\'s Cast'

class Category(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name
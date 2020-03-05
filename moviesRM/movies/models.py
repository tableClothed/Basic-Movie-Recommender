from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating


class Movie(models.Model):
    
    title = models.CharField(max_length=200)
    length = models.CharField(max_length=4)
    genre = models.CharField(max_length=300)
    homepage = models.CharField(max_length=100)
    overview = models.CharField(max_length=500)
    tagline = models.CharField(max_length=200)
    release_date = models.CharField(max_length=100)
    production_companies = models.CharField(max_length=200)
    ratings = GenericRelation(Rating, related_query_name='object_list')

    def __unicode__(self):
        return self.title


class Review(models.Model):
    RATING_CHOICES = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    pub_date = models.CharField("date published", max_length=20)
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)

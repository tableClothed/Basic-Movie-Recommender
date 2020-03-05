from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating


class Movie(models.Model):
    
    year = models.IntegerField()
    length = models.IntegerField()
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    actress = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    popularity = models.IntegerField()
    awards = models.BooleanField()
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

from django.db import models

# Create your models here.
class Movies(models.Model):
   
    rating = (
        ("G", 'G'),
        ("PG", 'PG'),
        ("PG-13", 'PG-13'),
        ("R", 'R'),
        ("NC-17", "NC-17"),
        ("Unrated", "Unrated")
    )

    mov_id = models.ForeignKey
    mov_name = models.CharField(max_length=100)
    mov_year = models.CharField(max_length=4)
    mov_country = models.CharField(max_length=30)
    mov_director = models.CharField(max_length=100)
    mov_language = models.CharField(max_length=20)
    mov_overview = models.TextField()
    url_movie = models.CharField(max_length=100, blank=True)
    url_trailer = models.CharField(max_length=100, blank=True)
    mov_poster = models.CharField(max_length=100, blank=True)
    mov_streaming = models.CharField(max_length=100, blank=True)
    mov_rating = models.CharField(max_length=10, choices=rating, default="PG")
    
    def __str__(self):
        return self.mov_name

    

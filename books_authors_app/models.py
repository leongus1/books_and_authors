from django.db import models

# Create your models here.
class books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    upddated_at = models.DateTimeField(auto_now_add=True)
    

class authors(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    books = models.ManyToManyField(books, related_name='authors')
    notes = models.TextField()
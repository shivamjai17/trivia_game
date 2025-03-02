from django.db import models
import uuid

class Destination(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    clues = models.JSONField()  # Stores clues as a list
    fun_fact = models.JSONField()  # Stores fun facts as a list
    trivia = models.JSONField() 

    def __str__(self):
        return f"{self.city}, {self.country}"

class UserProfile(models.Model):
    username = models.CharField(max_length=50, unique=True)
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username

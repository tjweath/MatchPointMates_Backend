# models.py

from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    # Assuming player_id is an auto-generated primary key, we'll use AutoField
    player_name = models.CharField(max_length=50)
    player_country = models.CharField(max_length=30)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.player_name

# models.py

from django.db import models

class Player(models.Model):
    # Assuming player_id is an auto-generated primary key, we'll use AutoField
    player_name = models.CharField(max_length=50)
    player_country = models.CharField(max_length=30)
    
    def __str__(self):
        return self.player_name

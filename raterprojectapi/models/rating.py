from django.db import models

class Rating(models.Model):
    
    rating = models.CharField(max_length=50)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)

from django.db import models

class Picture(models.Model):
    
    Picture = models.ImageField(upload_to='raterprojectapi/uploads/')
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)

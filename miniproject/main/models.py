from django.db import models


class Data(models.Model):
    uid = models.AutoField(primary_key=True) 
    place = models.CharField(max_length=100)
    image = models.EmailField(unique=True)  
    season = models.CharField(max_length=128)  
    category = models.TextField(blank=True, null=True) 
    type = models.TextField(blank=True, null=True) 
    stars = models.TextField(blank=True, null=True)
    google_map_link=models.TextField(blank=True,null=True)
    

    

    def __str__(self):
        return self.place

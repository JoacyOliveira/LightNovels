from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Novel(models.Model):
    status_hoices = (
        ("Andamento", "Andamento"),
        ("Concluido", "Concluido")
    )

    name = models.CharField(max_length=120)
    chapter = models.IntegerField(null=True,blank=True)
    link = models.CharField(max_length=120,null=True,blank=True)
    desc = models.TextField()
    image = models.ImageField(upload_to='novels_images')
    status = models.CharField(max_length=10, choices=status_hoices, blank=False, null=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    def __str__(self):
        return self.name
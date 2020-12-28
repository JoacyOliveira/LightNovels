from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


    def create_profile(sender, instance, created, **kwargs):

        if created:
            Profile.objects.create(user=instance)
            print("Perfil foi criado")

    post_save.connect(create_profile, sender=User)

    def update_profile(sender, instance,created , **kwargs):

        if created == False:
            print("Perfil atuzalizado")
            try:
                instance.profile.save()
                print("Perfil foi atualizado")
            except:
                Profile.objects.create(user=instance)
                print("perfil criado para usuario existente")

    post_save.connect(update_profile, sender=User)
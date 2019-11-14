from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from operator import itemgetter
#from evento.models import Evento

# Create your models here.

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=14,blank=True)
    #eventos = models.OneToManyField(Evento, on_delete=models.CASCADE)

    class Meta:
        ordering = ['user__username']

    def __str__(self):
        return "{} {} {} {}".format(self.cnpj, self.user.username, self.user.first_name, self.user.last_name)

    @receiver(post_save, sender=User)
    def create_user_usuario(sender, instance, created, **kwargs):
        if created:
            Usuario.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_usuario(sender, instance, **kwargs):
        instance.usuario.save()

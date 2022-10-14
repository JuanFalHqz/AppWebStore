
from Tienda.settings import MEDIA_URL, STATIC_URL
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    movil=models.PositiveIntegerField(verbose_name='Teléfono',null=True,blank=True)
    image=models.ImageField(upload_to='users/%Y/%m/%d', null=True,blank=True)

    def getImage(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL,self.image)
        return '{}{}'.format('/'+STATIC_URL,'dist/img/AdminLTELogo.png')

    class Meta:
        verbose_name='Usuario'
        verbose_name_plural="Usuarios"


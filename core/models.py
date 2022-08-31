from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

class Marmita(models.Model):
    sabor = models.CharField(max_length=100)
    descricao = models.TextField()
    begin_data = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='marmita')
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Meta:
    bd_table = 'marmita'       
   
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tarefa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=25)
    done = models.BooleanField(default=False)
    date_time = models.DateTimeField(auto_now=True)

from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL



# Create your models here.

class Asistencia(models.Model):
    id = models.AutoField(primary_key=True)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    entry_time = models.TimeField(blank=True, null=True)
    exit_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Asistencias"

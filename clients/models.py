from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=56)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

from django.db import models
from django.core.validators import RegexValidator


class Client(models.Model):
    name = models.CharField(max_length=56, verbose_name='Имя')
    email = models.EmailField(unique=True, verbose_name='Email')
    phone_number = models.CharField(
        max_length=13,
        validators=[
            RegexValidator(
                regex=r'^\+?[0-9]\d{7,14}',
                message='Нужно написать в формате +996555224466'
            )
        ],
        verbose_name='номер телефона'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

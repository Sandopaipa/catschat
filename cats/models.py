from django.db import models
from django.contrib.auth.models import User


#Породы
BREEDS = (
    ('NONE', 'Порода не указана'),
    ('RUSSIAN_BLUE', 'Русская голубая')
)
# Тип шерсти
FUR_TYPES = (
    ('LONG', 'Длинная шерсть'),
    ('MID', 'Средняя длина шерсти'),
    ('SHORT', 'Коротная длина шерсти')
)

class Cat(models.Model):
    owner = models.ForeignKey(
        to=User, on_delete=models.CASCADE
    )
    catname = models.CharField(
        max_length=50, blank=False, unique=False
    )
    cat_birthdate = models.DateField(
        blank=True, null=True, default=None
    )
    breed = models.CharField(
        blank=True, max_length=50, choices=BREEDS
    )
    fur = models.CharField(
        blank=True, max_length=50, choices=FUR_TYPES
    )

    def __str__(self):
        return f'{self.owner}: {self.catname}'

from django.core.exceptions import ValidationError
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    phone_number = PhoneNumberField(blank=True, verbose_name='Телефонный номер')
    code = models.PositiveIntegerField(blank=True, verbose_name='код мобильного оператора')
    tag = models.CharField(max_length=30, verbose_name='тег пользователя')

    def __str__(self):
        return str(self.phone_number)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Entity(models.Model):
    start_date = models.DateTimeField(verbose_name='дата начала рассылки')
    text = models.TextField(verbose_name='текст сообщения')
    client = models.ManyToManyField(Client, related_name='entity')
    end_date = models.DateTimeField(verbose_name='дата окончания рассылки')

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError(
                'Дата начала рассылки не может быть больше даты конца рассылки'
            )

    def __str__(self):
        return self.text[:15]


class Message(models.Model):
    date = models.DateTimeField(verbose_name='дата отправки сообщения')
    entity = models.ForeignKey(Entity, on_delete=models.PROTECT, related_name='messages')
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='messages')

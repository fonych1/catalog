from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from notifications.signals import notify


class Product(models.Model):
    sku = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=255)
    requested = models.IntegerField(default=0)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Product)
def product_post_save(sender, **kwargs):
    notify.send(
        sender=kwargs['instance'],
        verb=f'Product with id {kwargs["instance"].id} was updated',
        target=kwargs['instance'],
        action_object=kwargs['instance'],
        recipient_list=User.objects.filter(is_staff=True)
    )

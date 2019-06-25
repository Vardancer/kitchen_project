from django.db import models
from django.contrib.auth.models import User


class Week(models.Model):
    """
    Модель расписания на неделю
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    day = models.ManyToManyField('Day', related_name='week')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'week'


class Day(models.Model):
    """
    Модель расписания на день
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    dish = models.ManyToManyField('Dish', related_name='dishes')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'day'


class Dish(models.Model):
    """
    Модель жратвы
    """
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300)
    ingredients = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Dish {} with cost {}".format(self.name, self.price)

    class Meta:
        verbose_name = 'dish'


class OrdersTransit(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    is_half = models.BooleanField(default=False)
    cost = models.DecimalField(max_digits=18, decimal_places=2)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ManyToManyField(Dish, related_name='orders', through=OrdersTransit)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    total_cost = models.DecimalField(max_digits=18, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Order of {} on week {}".format(self.user.username, self.week.name)

    class Meta:
        verbose_name = 'order'




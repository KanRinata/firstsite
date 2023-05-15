from django.contrib.auth.models import User
from django.db import models


class AdvUser(models.Model):
    is_activated = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Spare(models.Model):
    name = models.CharField(max_length=30)


class Machine(models.Model):
    name = models.CharField(max_length=30)
    spares = models.ManyToManyField(Spare)


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name="Название")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/{self.pk}/"

    def save(self, *args, **kwargs):
        if True:
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if True:
            super().delete(*args, **kwargs)



    class Meta:
        verbose_name = "Рубрика"
        verbose_name_plural = "Рубрики"
        ordering = ['name']


class Bb(models.Model):
    rubric = models.ForeignKey("Rubric", null=True, on_delete=models.PROTECT, verbose_name="Рубрика")
    title = models.CharField(max_length=50, verbose_name="Товар")
    content = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.FloatField(null=True, blank=True, verbose_name="Цена")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.title

    def title_and_price(self):
        if self.price:
            return '%s (%.2f)' % (self.title, self.price)
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-published', 'title']
        get_latest_by = ['title', 'published']
        db_table = "bboard_bb"


class Human(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    male = models.TextField(blank=True, verbose_name="Пол")
    age = models.SmallIntegerField(blank=True, verbose_name="Возраст")


class Child(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    male = models.TextField(blank=True, verbose_name="Пол")
    age = models.SmallIntegerField(blank=True, verbose_name="Возраст")


class IceCream(models.Model):
    taste = models.CharField(max_length=50, verbose_name="Вкус")
    type = models.TextField(blank=True, verbose_name="Тип")
    quantity = models.SmallIntegerField(blank=True, verbose_name="Количество шариков")


class IceCreamMarket(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")

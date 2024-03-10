from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    model = models.CharField(max_length=100, verbose_name="модель")
    sell_start = models.DateTimeField(verbose_name="дата выхода продукта на рынок")

    def __str__(self):
        return self.title

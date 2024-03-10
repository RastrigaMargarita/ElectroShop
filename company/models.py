from django.db import models
from django.utils import timezone

from company.validators import validate_supplier
from products.models import Product


class Company(models.Model):

    class Category(models.TextChoices):
        Manufactury = 'manufactury', 'Завод'
        Retailer = 'retailer', 'Розничный агент'
        IE = 'entrepreneur', 'Индивидуальный предприниматель'

    category = models.CharField(max_length=12, choices=Category.choices, default=Category.Manufactury,
                                verbose_name='Категория юридического лица')
    title = models.CharField(max_length=100, verbose_name="Название", unique=True)
    email = models.EmailField(verbose_name="эл.адрес")
    country = models.ForeignKey("Country", on_delete=models.CASCADE, verbose_name="cтрана")
    town = models.ForeignKey("Town", on_delete=models.CASCADE, verbose_name="cтрана")
    street = models.CharField(max_length=150, verbose_name="улица")
    building = models.CharField(max_length=10, verbose_name="дом, корпус, квартира")
    products = models.ManyToManyField(Product, verbose_name="продукция")
    supplier = models.ForeignKey("Company", on_delete=models.CASCADE, verbose_name="поставщик", blank=True, null=True)
    debt = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="задолженность", blank=True, null=True)
    created = models.DateTimeField(verbose_name="создан", default=timezone.now)

    def get_products(self):
        return "\n".join([p.title for p in self.products.all()])

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        self.clean()
        return super(Company, self).save(**kwargs)

    def clean(self):
        print("clean active")
        validate_supplier(self.supplier, self.category, Company.Category.Manufactury)


class Country(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название", unique=True)

    def __str__(self):
        return self.title


class Town(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название", unique=True)

    def __str__(self):
        return self.title

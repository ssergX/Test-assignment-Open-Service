from django.db import models


class Price(models.Model):
    currency = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"

    def __str__(self):
        return f"{self.amount} {self.currency}"


class ProductType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Тип товара"
        verbose_name_plural = "Типы товаров"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    barcode = models.CharField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name

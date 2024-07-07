from django.db import models


class Collection(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=64, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True, unique=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    adress = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Fabric(models.Model):
    name = models.CharField(max_length=64, unique=True)
    sku = models.CharField(max_length=64, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_meters = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Second_layer(models.Model):
    name = models.CharField(max_length=64, unique=True)
    sku = models.CharField(max_length=64, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_meters = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Lace(models.Model):
    name = models.CharField(max_length=64, unique=True)
    sku = models.CharField(max_length=64, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_meters = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Accessories(models.Model):
    name = models.CharField(max_length=64, unique=True)
    sku = models.CharField(max_length=64, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_units = models.PositiveIntegerField(default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Glitter(models.Model):
    name = models.CharField(max_length=64, unique=True)
    sku = models.CharField(max_length=64, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_units = models.PositiveIntegerField(default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
from django.db import models

from users.models import User


class Supplier(models.Model):
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    email = models.EmailField(max_length=254, default=None)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Buyer(models.Model):
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    email = models.EmailField(max_length=254, default=None)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Drop(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=24)
    description = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Fabricant(models.Model):
    name = models.CharField(max_length=24)
    description = models.CharField(max_length=120)

    def __str__(self):
        return self.name


# class Tag(models.Model):
#     name = models.CharField(max_length=24)
#     description = models.CharField(max_length=120)

#     def __str__(self):
#         return self.name


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    dosage = models.CharField(max_length=120)
    available_quantity = models.PositiveIntegerField()
    min_quantity = models.PositiveBigIntegerField()
    code = models.CharField(max_length=24, unique=True)
    regsan = models.CharField(max_length=24, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    fabricant = models.ForeignKey(Fabricant, on_delete=models.CASCADE)
    #tag = models.ManyToManyField(Tag)

    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Input(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    batch_number = models.CharField(max_length=24)
    expiracy_date = models.DateField(null=False)
    supplier = supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    created_date = models.DateField(auto_now_add=True)


class Output(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    batch_number = models.CharField(max_length=24)

    created_date = models.DateField(auto_now_add=True)


class Order(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
        ('bulk', 'Bulk'),
    )
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    design = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, null=True)
    drop = models.ForeignKey(Drop, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product.name


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier_name = models.CharField(max_length=120)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.courier_name

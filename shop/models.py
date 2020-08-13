from django.db import models


# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=60, default='')
    phone = models.CharField(max_length=14, default='')
    desc = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=60, default='')
    address = models.CharField(max_length=112, default='')
    phone = models.CharField(max_length=14, default='')
    city = models.CharField(max_length=500, default='')
    state = models.CharField(max_length=500, default='')
    zip_code = models.CharField(max_length=500, default='')
    items_json = models.CharField(max_length=1000, default='')


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=300, default="")
    timeStamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:9] + '...'

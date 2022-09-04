from statistics import mode
from django.db import models

# Create your models here.

class User(models.Model):

    class Meta:

        db_table = 'user'

    idUser = models.IntegerField()
    nick = models.CharField(max_length=200)
    createdAt = models.DateTimeField()

    def __str__(self):
        return 'idUser: ' + self.idUser


class Safety(models.Model):

    class Meta:

        db_table = 'safety'

    idSafety = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return 'idSafety: ' + self.idSafety


class Report(models.Model):

    class Meta:

        db_table = 'report'

    idReport = models.IntegerField()
    filePath = models.CharField(max_length=200)
    createdAt = models.DateTimeField()
    expiredAt = models.DateTimeField()

    def __str__(self):
        return 'idReport: ' + self.idReport


class Brand(models.Model):

    class Meta:

        db_table = 'brand'

    idBrand = models.IntegerField()
    brandName = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    logoPath = models.CharField(max_length=200)

    def __str__(self):
        return 'idBrand: ' + self.idBrand


class Product(models.Model):

    class Meta:

        db_table = 'product'

    barCode = models.IntegerField()
    idBrand = models.ForeignKey('Brand', related_name='products', on_delete=models.CASCADE,default=0)
    idSafety = models.ForeignKey('Safety', related_name='products', on_delete=models.CASCADE,default=0)
    idReport = models.ForeignKey('Report', related_name='products', on_delete=models.CASCADE,default=0)
    productName = models.CharField(max_length=200)
    productCategory = models.CharField(max_length=200)
    picturePath = models.CharField(max_length=200)
    productIngredients = models.CharField(max_length=500)
    createdAt = models.DateTimeField()


    def __str__(self):
        return 'barCode: ' + self.barCode


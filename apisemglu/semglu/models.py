from statistics import mode
from django.db import models

# Create your models here.


class User(models.Model):
    class Meta:

        db_table = "user"

    idUser = models.IntegerField()
    nick = models.CharField(max_length=200)
    createdAt = models.DateTimeField()

    def __str__(self):
        return """
        idUser: {0},
        nickname: {1},
        data de criacao: {2}
        """.format(
            self.idUser, self.nick, self.createdAt
        )


class Safety(models.Model):
    class Meta:

        db_table = "safety"

    idSafety = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return """
        idSafety: {0},
        categoria: {1},
        descricao: {2},
        """.format(
            self.idSafety, self.category, self.description
        )


class Report(models.Model):
    class Meta:

        db_table = "report"

    idReport = models.IntegerField()
    filePath = models.CharField(max_length=200)
    createdAt = models.DateTimeField()
    expiredAt = models.DateTimeField()

    def __str__(self):
        return """
        idReport: {0},
        url: {1},
        data de criacao: {2},
        data de expiracao: {3},
        """.format(
            self.idReport, self.filePath, self.createdAt, self.expiredAt
        )


class Brand(models.Model):
    class Meta:

        db_table = "brand"

    idBrand = models.IntegerField()
    brandName = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    logoPath = models.CharField(max_length=200)

    def __str__(self):
        return """
        idBrand: {0},
        marca: {1},
        contato: {2},
        url da logo: {3},
        """.format(
            self.idBrand, self.brandName, self.contact, self.logoPath
        )


class Product(models.Model):
    class Meta:

        db_table = "product"

    barCode = models.IntegerField()
    idBrand = models.ForeignKey(
        "Brand", related_name="products", on_delete=models.CASCADE, default=1
    )
    idSafety = models.ForeignKey(
        "Safety", related_name="products", on_delete=models.CASCADE, default=1
    )
    idReport = models.ForeignKey(
        "Report", related_name="products", on_delete=models.CASCADE, default=1
    )

    productName = models.CharField(max_length=200)
    productCategory = models.CharField(max_length=200)
    picturePath = models.CharField(max_length=200)
    productIngredients = models.CharField(max_length=500)
    createdAt = models.DateTimeField()

    def __str__(self):
        return """
        barCode: {0},
        id da marca: {1},
        id Safety: {2},
        id Report: {3},
        nome do produto: {4},
        categoria: {5},
        url: {6},
        ingredientes: {7},
        data de criacao: {8},
        """.format(
            self.barCode,
            self.idBrand,
            self.idSafety,
            self.idReport,
            self.productName,
            self.productCategory,
            self.picturePath,
            self.productIngredients,
            self.createdAt,
        )

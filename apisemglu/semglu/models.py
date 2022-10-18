import os
from django.db import models

# Modelo de usuário
class User(models.Model):
    class Meta:  ## Nome da tabela no MariaDB

        db_table = "user"

    # Elementos da tabela, de acordo com o modelo
    idUser = models.BigAutoField(primary_key=True)  ## Chave primária
    nick = models.CharField(max_length=200)
    createdAt = models.DateTimeField(null=True)

    # Como será retornado no json
    def __str__(self):
        return """
        idUser: {0},
        nickname: {1},
        data de criacao: {2}
        """.format(
            self.idUser, self.nick, self.createdAt
        )


# Modelo de safety (perdão pela falta de tradução)
class Safety(models.Model):
    class Meta:  ## Nome da tabela no MariaDB

        db_table = "safety"

    # Elementos da tabela, de acordo com o modelo
    idSafety = models.BigAutoField(primary_key=True)  ## Chave primária
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, null=True)

    # Como será retornado no json
    def __str__(self):
        return """
        idSafety: {0},
        categoria: {1},
        descricao: {2},
        """.format(
            self.idSafety, self.category, self.description
        )


class Report(models.Model):
    class Meta:  ## Nome da tabela no MariaDB

        db_table = "report"

    def update_file_path(instance, filename):
        path = "reports"
        filename = instance.filePath.replace(" ", "_")
        return os.path.join(path, filename)
    # Elementos da tabela, de acordo com o modelo
    idReport = models.BigAutoField(primary_key=True)  ## Chave primária
    filePath = models.FileField(upload_to=update_file_path, max_length=500, null=True)
    createdAt = models.DateTimeField(null=True)
    expiredAt = models.DateTimeField(null=True)

    # Como será retornado no json
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
    class Meta:  ## Nome da tabela no MariaDB

        db_table = "brand"

    def update_file_path(instance, filename):
        path = "logo"
        fmt = instance.brandName.replace(" ", "_")
        ext = filename.split(".")[-1]
        filename = "{}.{}".format(fmt, ext)
        return os.path.join(path, filename)
    # Elementos da tabela, de acordo com o modelo
    idBrand = models.BigAutoField(primary_key=True)  ## Chave primária
    brandName = models.CharField(max_length=200)
    contact = models.CharField(max_length=200, null=True)
    logoPath = models.ImageField(upload_to=update_file_path, max_length=500, null=True)

    # Como será retornado no json
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
    class Meta:  ## Nome da tabela no MariaDB

        db_table = "product"

    # Elementos da tabela, de acordo com o modelo
    barCode = models.BigAutoField(primary_key=True)  ## Chave primária
    idBrand = models.ForeignKey(  ## Chave estrangeira
        "Brand", related_name="products", on_delete=models.CASCADE
    )
    idSafety = models.ForeignKey(  ## Chave estrangeira
        "Safety", related_name="products", on_delete=models.CASCADE
    )
    idReport = models.ForeignKey(  ## Chave estrangeira
        "Report", related_name="products", on_delete=models.CASCADE, null=True
    )

    def update_file_path(instance, filename):
        path = "picture"
        fmt = instance.productName.replace(" ", "_")
        ext = filename.split(".")[-1]
        filename = "{}.{}".format(fmt, ext)
        return os.path.join(path, filename)

    productName = models.CharField(max_length=200)
    productCategory = models.CharField(max_length=200, null=True)
    picturePath = models.ImageField(upload_to=update_file_path, max_length=500, null=True)
    productIngredients = models.TextField(null=True)
    createdAt = models.DateTimeField(null=True)

    # Como será retornado no json
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

class Review(models.Model):
    class Meta:  ## Nome da tabela no MariaDB

        db_table = "review"

    # Elementos da tabela, de acordo com o modelo
    idReview = models.BigAutoField(primary_key=True)  ## Chave primária
    idProduct = models.ForeignKey(  ## Chave estrangeira
        "Product", related_name="reviews", on_delete=models.CASCADE
    )
    idUser = models.ForeignKey(  ## Chave estrangeira
        "User", related_name="reviews", on_delete=models.CASCADE
    )

    text = models.TextField()
    grade = models.FloatField()

    # Como será retornado no json
    def __str__(self):
        return """
        idReview: {0},
        id do produto: {1},
        id do usuário: {2},
        texto: {3},
        avaliacao: {4},
        """.format(
            self.idReview,
            self.idProduct,
            self.idUser,
            self.text,
            self.grade,
        )

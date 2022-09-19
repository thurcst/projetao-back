from django.db import models

# Create your models here.


# Modelo de usuário
class User(models.Model):
    class Meta:  ## Nome da tabela no MariaDB

        db_table = "user"

    # Elementos da tabela, de acordo com o modelo
    idUser = models.BigAutoField(primary_key=True)  ## Chave primária
    nick = models.CharField(max_length=200)
    createdAt = models.DateTimeField()

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
    description = models.CharField(max_length=1000)

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

    # Elementos da tabela, de acordo com o modelo
    idReport = models.BigAutoField(primary_key=True)  ## Chave primária
    filePath = models.CharField(max_length=200)
    createdAt = models.DateTimeField()
    expiredAt = models.DateTimeField()

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

    # Elementos da tabela, de acordo com o modelo
    idBrand = models.BigAutoField(primary_key=True)  ## Chave primária
    brandName = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    logoPath = models.CharField(max_length=200)

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
    barCode = models.IntegerField(primary_key=True)  ## Chave primária
    idBrand = models.ForeignKey(  ## Chave estrangeira
        "Brand", related_name="products", on_delete=models.CASCADE, default=1
    )
    idSafety = models.ForeignKey(  ## Chave estrangeira
        "Safety", related_name="products", on_delete=models.CASCADE, default=1
    )
    idReport = models.ForeignKey(  ## Chave estrangeira
        "Report", related_name="products", on_delete=models.CASCADE, default=1
    )

    productName = models.CharField(max_length=200)
    productCategory = models.CharField(max_length=200)
    picturePath = models.CharField(max_length=200)
    productIngredients = models.CharField(max_length=500)
    createdAt = models.DateTimeField()

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

# Generated by Django 4.1 on 2022-09-22 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semglu', '0004_alter_product_picturepath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picturePath',
            field=models.ImageField(upload_to='picture'),
        ),
    ]

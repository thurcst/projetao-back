# Generated by Django 4.1 on 2022-10-14 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semglu', '0010_alter_brand_contact_alter_brand_logopath_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productIngredients',
            field=models.TextField(null=True),
        ),
    ]

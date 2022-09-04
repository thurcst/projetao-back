# Generated by Django 4.1 on 2022-09-04 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('semglu', '0002_brand_product_report_safety_user_delete_music'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='idBrand',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='semglu.brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='idReport',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='semglu.report'),
        ),
        migrations.AddField(
            model_name='product',
            name='idSafety',
            field=models.ForeignKey(default='x', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='semglu.safety'),
        ),
    ]

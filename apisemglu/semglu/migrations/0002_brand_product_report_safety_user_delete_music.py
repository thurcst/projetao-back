# Generated by Django 4.1 on 2022-09-04 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semglu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idBrand', models.IntegerField()),
                ('brandName', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('logoPath', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'brand',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barCode', models.IntegerField()),
                ('productName', models.CharField(max_length=200)),
                ('productCategory', models.CharField(max_length=200)),
                ('picturePath', models.CharField(max_length=200)),
                ('productIngredients', models.CharField(max_length=500)),
                ('createdAt', models.DateTimeField()),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idReport', models.IntegerField()),
                ('filePath', models.CharField(max_length=200)),
                ('createdAt', models.DateTimeField()),
                ('expiredAt', models.DateTimeField()),
            ],
            options={
                'db_table': 'report',
            },
        ),
        migrations.CreateModel(
            name='Safety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idSafety', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'safety',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUser', models.IntegerField()),
                ('nick', models.CharField(max_length=200)),
                ('createdAt', models.DateTimeField()),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.DeleteModel(
            name='Music',
        ),
    ]

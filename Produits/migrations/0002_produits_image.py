# Generated by Django 5.1.4 on 2024-12-10 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produits',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]

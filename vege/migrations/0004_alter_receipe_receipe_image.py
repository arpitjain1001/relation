# Generated by Django 4.2.1 on 2024-05-07 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0003_alter_receipe_receipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipe',
            name='receipe_image',
            field=models.ImageField(upload_to='static'),
        ),
    ]

# Generated by Django 4.1 on 2022-09-05 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_tees_alter_avatar_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tees',
            name='imagen',
            field=models.CharField(max_length=120),
        ),
    ]

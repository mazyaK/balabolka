# Generated by Django 3.0.4 on 2020-04-27 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200427_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', max_length=200, unique=True),
        ),
    ]
# Generated by Django 3.0.4 on 2020-04-28 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200427_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='media/accounts/avatars/default_no_avatar.png', null=True, upload_to='accounts/avatars/'),
        ),
    ]

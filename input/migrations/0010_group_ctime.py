# Generated by Django 2.1.1 on 2019-05-16 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0009_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='ctime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

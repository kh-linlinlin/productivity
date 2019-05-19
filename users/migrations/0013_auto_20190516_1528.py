# Generated by Django 2.1.1 on 2019-05-16 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0012_auto_20190516_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='ctime',
        ),
        migrations.RemoveField(
            model_name='group',
            name='current_task',
        ),
        migrations.RemoveField(
            model_name='group',
            name='mime',
        ),
        migrations.RemoveField(
            model_name='group',
            name='name',
        ),
        migrations.RemoveField(
            model_name='group',
            name='status',
        ),
        migrations.AddField(
            model_name='group',
            name='curr_grp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='current_grp', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='group',
            name='user',
        ),
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]

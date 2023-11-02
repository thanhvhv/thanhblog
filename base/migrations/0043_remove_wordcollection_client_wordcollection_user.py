# Generated by Django 4.2.6 on 2023-11-01 03:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0042_alter_wordcollection_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wordcollection',
            name='client',
        ),
        migrations.AddField(
            model_name='wordcollection',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
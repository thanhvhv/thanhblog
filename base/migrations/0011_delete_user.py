# Generated by Django 4.2.6 on 2023-10-25 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_blog_created_alter_blog_updated'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-26 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_remove_word_blog_word_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='word',
            name='image',
        ),
        migrations.RemoveField(
            model_name='word',
            name='level',
        ),
        migrations.RemoveField(
            model_name='word',
            name='note',
        ),
        migrations.RemoveField(
            model_name='word',
            name='synonym',
        ),
        migrations.RemoveField(
            model_name='word',
            name='word',
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-26 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0036_word_definition_word_example_word_image_word_level_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='image',
        ),
    ]

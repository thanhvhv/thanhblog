# Generated by Django 4.2.6 on 2023-10-26 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0031_word_blog_word_definition_word_example_word_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='definition',
        ),
        migrations.RemoveField(
            model_name='word',
            name='example',
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
            name='mean',
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

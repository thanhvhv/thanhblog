# Generated by Django 4.2.6 on 2023-10-26 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_remove_word_blog_word_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='blog',
        ),
        migrations.AddField(
            model_name='word',
            name='blog',
            field=models.ManyToManyField(related_name='words', to='base.blog'),
        ),
    ]

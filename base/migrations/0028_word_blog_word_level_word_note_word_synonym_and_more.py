# Generated by Django 4.2.6 on 2023-10-26 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_remove_word_blog_remove_word_image_remove_word_level_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='blog',
            field=models.ManyToManyField(related_name='words', to='base.blog'),
        ),
        migrations.AddField(
            model_name='word',
            name='level',
            field=models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')], default=None, max_length=5),
        ),
        migrations.AddField(
            model_name='word',
            name='note',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='word',
            name='synonym',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='word',
            name='word',
            field=models.CharField(default=None, max_length=50),
        ),
    ]

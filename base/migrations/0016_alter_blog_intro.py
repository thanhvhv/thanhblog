# Generated by Django 4.2.6 on 2023-10-25 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_word_rename_created_blog_published_wordcollection_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='intro',
            field=models.CharField(max_length=500),
        ),
    ]

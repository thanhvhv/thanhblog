# Generated by Django 4.2.6 on 2023-10-25 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_author_dob_user_dob_user_join_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='join_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='join_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]

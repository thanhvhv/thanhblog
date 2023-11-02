# Generated by Django 4.2.6 on 2023-10-31 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0041_remove_wordcollection_user_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordcollection',
            name='level',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], default='Medium', max_length=10),
        ),
    ]

# Generated by Django 5.1.2 on 2024-10-16 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='utilizador',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

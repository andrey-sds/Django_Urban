# Generated by Django 4.2.17 on 2025-01-16 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0006_news_delete_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

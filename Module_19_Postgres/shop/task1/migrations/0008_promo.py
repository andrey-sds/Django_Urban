# Generated by Django 4.2.17 on 2025-01-16 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0007_alter_news_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Акция!', max_length=255)),
                ('createdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

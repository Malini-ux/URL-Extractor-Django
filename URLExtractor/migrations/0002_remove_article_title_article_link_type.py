# Generated by Django 5.0.2 on 2024-02-11 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('URLExtractor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='title',
        ),
        migrations.AddField(
            model_name='article',
            name='link_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

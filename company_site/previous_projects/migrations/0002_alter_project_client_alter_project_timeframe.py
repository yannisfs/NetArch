# Generated by Django 5.1.3 on 2024-12-13 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('previous_projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='project',
            name='timeframe',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
# Generated by Django 5.1.3 on 2024-12-05 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=128)),
                ('text', models.CharField(max_length=2048)),
                ('author', models.CharField(max_length=64)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-18 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vege_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('desc', models.TextField()),
                ('pic', models.ImageField(upload_to='')),
            ],
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-13 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('author', models.CharField(blank=True, max_length=100)),
                ('isbn', models.CharField(blank=True, max_length=100)),
                ('publisher', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]

# Generated by Django 5.1 on 2024-09-28 05:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
        ('genres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('count', models.IntegerField()),
                ('slug', models.SlugField(default='')),
                ('description', models.TextField(default='')),
                ('publishingYear', models.PositiveIntegerField(default=1)),
                ('price', models.CharField(default='0.00', max_length=20)),
                ('publication', models.CharField(default='no_publication', max_length=100)),
                ('binding', models.CharField(default='no_binding', max_length=50)),
                ('authors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authors.authors')),
                ('genres', models.ManyToManyField(to='genres.genres')),
            ],
        ),
    ]

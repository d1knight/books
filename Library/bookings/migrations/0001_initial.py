# Generated by Django 5.1 on 2024-09-28 05:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Books', '0001_initial'),
        ('personal', '0001_initial'),
        ('readers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('getDate', models.DateField()),
                ('returnDate', models.DateField()),
                ('slug', models.SlugField(default='')),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.books')),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.personal')),
                ('readers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readers.readers')),
            ],
        ),
    ]
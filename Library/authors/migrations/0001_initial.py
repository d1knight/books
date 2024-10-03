# Generated by Django 5.1 on 2024-09-28 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(default='No description', max_length=255)),
                ('slug', models.SlugField(default='')),
                ('banner', models.ImageField(blank=True, default='Гоголь.jpg', upload_to='')),
            ],
        ),
    ]

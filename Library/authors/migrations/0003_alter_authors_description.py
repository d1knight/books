# Generated by Django 5.1 on 2024-10-02 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_alter_authors_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='description',
            field=models.CharField(blank=True, default='No description', max_length=255, null=True),
        ),
    ]

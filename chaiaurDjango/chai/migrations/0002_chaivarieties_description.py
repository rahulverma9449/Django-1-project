# Generated by Django 5.1.2 on 2024-10-16 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivarieties',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]

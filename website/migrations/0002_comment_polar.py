# Generated by Django 2.0.3 on 2018-04-06 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='polar',
            field=models.FloatField(default=0, max_length=8),
        ),
    ]

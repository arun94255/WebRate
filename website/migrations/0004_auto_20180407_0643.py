# Generated by Django 2.0.3 on 2018-04-07 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_comment_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='coment',
            field=models.CharField(max_length=2000),
        ),
    ]

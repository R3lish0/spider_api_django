# Generated by Django 4.1.5 on 2023-02-01 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiderapi', '0003_crops'),
    ]

    operations = [
        migrations.AddField(
            model_name='crops',
            name='farmId',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crops',
            name='ownerId',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fields',
            name='ownerId',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

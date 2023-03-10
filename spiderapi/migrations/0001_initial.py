# Generated by Django 4.0.2 on 2022-02-04 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owners',
            fields=[
                ('id', models.AutoField(primary_key=True)),
                ('firstLast', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Farms',
            fields=[
                ('id', models.AutoField(primary_key=True)),
                ('farmName', models.CharField(max_length=500)),
                ('farmLocation', models.CharField(max_length=500)),
                ('farmSize', models.IntegerField(blank=False)),
                ('ownerId', models.IntegerField(blank=False)),
            ],
        ),
        migrations.CreateModel(
            name='Fields',
            fields=[
                ('id', models.AutoField(primary_key=True)),
                ('farmId', models.IntegerField(blank=False)),
                ('fieldName', models.CharField(max_length=500)),
                ('fieldSize', models.IntegerField(blank=False)),
                ('fertilizerType', models.CharField(max_length=500)),
                ('lastFertilized', models.DateField()),
                ('wateredAmount', models.IntegerField(blank=False)),
                ('lastWatered',models.DateField()),
            ],
        ),
    ]

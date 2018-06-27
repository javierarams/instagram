# Generated by Django 2.0.6 on 2018-06-26 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('nickname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=140)),
                ('bio', models.CharField(max_length=500)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=140)),
                ('gender', models.CharField(max_length=1)),
                ('private', models.BooleanField()),
                ('sugest', models.BooleanField()),
            ],
        ),
    ]

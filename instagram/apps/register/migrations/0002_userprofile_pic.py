# Generated by Django 2.0.6 on 2018-06-28 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='pic',
            field=models.ImageField(default='asd', upload_to='profilepics'),
            preserve_default=False,
        ),
    ]

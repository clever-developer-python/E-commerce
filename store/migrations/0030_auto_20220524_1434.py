# Generated by Django 3.1.2 on 2022-05-24 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0029_myaddres'),
    ]

    operations = [
        migrations.AddField(
            model_name='myaddres',
            name='city',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='myaddres',
            name='last',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='myaddres',
            name='name',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='myaddres',
            name='zip',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='myaddres',
            name='address',
            field=models.CharField(max_length=100000, null=True),
        ),
    ]
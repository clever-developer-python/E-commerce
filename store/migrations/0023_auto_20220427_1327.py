# Generated by Django 3.1.2 on 2022-04-27 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_auto_20220427_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guestuser',
            name='user',
        ),
        migrations.AddField(
            model_name='guestuser',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
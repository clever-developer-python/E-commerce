# Generated by Django 3.1.2 on 2022-03-02 07:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_auto_20220301_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=1000, null=True)),
                ('last', models.CharField(max_length=1000, null=True)),
                ('email', models.CharField(max_length=1000, null=True)),
                ('phone', models.CharField(max_length=1000, null=True)),
                ('country', models.CharField(max_length=10, null=True)),
                ('state', models.CharField(max_length=500, null=True)),
                ('zip', models.CharField(max_length=250, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

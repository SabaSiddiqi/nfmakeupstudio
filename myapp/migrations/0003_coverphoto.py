# Generated by Django 2.2.5 on 2020-02-16 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_hotel'),
    ]

    operations = [
        migrations.CreateModel(
            name='coverPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coverPhoto_name', models.CharField(max_length=50)),
                ('coverPhoto_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]

# Generated by Django 3.0.2 on 2020-07-28 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_html_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliophoto_makeup',
            name='portfolioPhoto_makeup_column',
            field=models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default='1', max_length=1),
        ),
    ]

# Generated by Django 3.0.2 on 2020-07-28 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_portfoliophoto_makeup_portfoliophoto_makeup_column'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliophoto_hairdo',
            name='portfolioPhoto_hairdo_column',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default='1', max_length=1),
        ),
        migrations.AddField(
            model_name='portfoliophoto_henna',
            name='portfolioPhoto_henna_column',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='portfoliophoto_makeup',
            name='portfolioPhoto_makeup_column',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default='1', max_length=1),
        ),
    ]

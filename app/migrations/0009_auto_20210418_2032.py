# Generated by Django 3.1.7 on 2021-04-18 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210317_1930'),
    ]

    operations = [
        migrations.DeleteModel(
            name='signup',
        ),
        migrations.AlterField(
            model_name='resource',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]

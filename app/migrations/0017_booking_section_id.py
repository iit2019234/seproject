# Generated by Django 3.1.7 on 2021-04-20 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20210419_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='section_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.section'),
        ),
    ]

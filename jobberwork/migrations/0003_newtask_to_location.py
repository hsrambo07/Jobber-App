# Generated by Django 2.2.9 on 2020-12-26 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobberwork', '0002_auto_20201130_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='newtask',
            name='to_location',
            field=models.TextField(default=-23),
            preserve_default=False,
        ),
    ]
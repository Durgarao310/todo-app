# Generated by Django 3.0.7 on 2020-07-03 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=50),
        ),
    ]
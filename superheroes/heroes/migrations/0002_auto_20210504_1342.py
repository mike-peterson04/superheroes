# Generated by Django 3.1.8 on 2021-05-04 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='catchphrase',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='secondary',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
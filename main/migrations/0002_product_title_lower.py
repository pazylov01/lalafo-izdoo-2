# Generated by Django 3.1.5 on 2021-02-16 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='title_lower',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

# Generated by Django 3.2.3 on 2021-07-20 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='petstagramuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='petstagramuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]

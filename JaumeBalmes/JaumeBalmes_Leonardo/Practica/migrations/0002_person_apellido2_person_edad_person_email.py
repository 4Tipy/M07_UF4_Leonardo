# Generated by Django 4.1.7 on 2023-04-20 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Practica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='apellido2',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='person',
            name='edad',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.5 on 2020-05-06 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0006_empleado_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
    ]

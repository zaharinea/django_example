# Generated by Django 2.0.3 on 2018-04-03 20:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date_from',
            new_name='date_in',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='date_till',
            new_name='date_out',
        ),
        migrations.AddField(
            model_name='client',
            name='date_of_birth',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='smoke',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
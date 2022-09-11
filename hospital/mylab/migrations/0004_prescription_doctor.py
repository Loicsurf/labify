# Generated by Django 4.0.6 on 2022-08-12 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mylab', '0003_doctor_remove_prescription_prescriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='doctor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mylab.doctor'),
            preserve_default=False,
        ),
    ]

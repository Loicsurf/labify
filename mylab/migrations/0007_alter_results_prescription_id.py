# Generated by Django 4.1.1 on 2022-10-14 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mylab', '0006_rename_prescription_results_prescription_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='prescription_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mylab.prescription'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.1 on 2022-10-14 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mylab', '0007_alter_results_prescription_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='prescription_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mylab.prescription'),
        ),
    ]
# Generated by Django 4.1.1 on 2022-10-14 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mylab', '0004_doctor_date_created_doctor_last_updated_doctor_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='prescription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mylab.prescription'),
        ),
    ]
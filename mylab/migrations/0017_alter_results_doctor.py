# Generated by Django 4.1.1 on 2022-10-15 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mylab', '0016_alter_results_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mylab.doctor'),
        ),
    ]
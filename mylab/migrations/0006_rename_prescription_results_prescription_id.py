# Generated by Django 4.1.1 on 2022-10-14 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mylab', '0005_alter_results_prescription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='results',
            old_name='prescription',
            new_name='prescription_id',
        ),
    ]

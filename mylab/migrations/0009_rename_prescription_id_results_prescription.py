# Generated by Django 4.1.1 on 2022-10-14 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mylab', '0008_alter_results_prescription_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='results',
            old_name='prescription_id',
            new_name='prescription',
        ),
    ]
# Generated by Django 4.0.6 on 2022-08-12 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylab', '0010_alter_prescription_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='id',
            field=models.BigAutoField(default='ACCTS-<built-in function id>', editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
# Generated by Django 4.1.1 on 2022-10-14 10:55

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Additives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abbre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Collectors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('abbre', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=255)),
                ('additives', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mylab.additives')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Interval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('interval', models.CharField(max_length=50)),
                ('minimum', models.IntegerField()),
                ('maximum', models.IntegerField()),
                ('fix_value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abbre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('dob', models.DateField(help_text='Please Enter Your Correct Date Of Birth', null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Single', 'Single')], max_length=50)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('emailAddress', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('In Treatement', 'In Treatement'), ('Recovered', 'Recovered'), ('New Patient', 'New Patient')], max_length=20, null=True)),
                ('town', models.CharField(choices=[('Yaounde', 'Yaounde'), ('Douala', 'Douala'), ('Bamenda', 'Bamenda'), ('Buea', 'Buea'), ('Baffoussam', 'Baffoussam'), ('Ngaoundere', 'Ngaoundere'), ('Ebolowa', 'Ebolowa'), ('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ('', '')], max_length=50)),
                ('address', models.CharField(blank=True, max_length=20)),
                ('occupation', models.CharField(blank=True, choices=[('', ''), ('', '')], max_length=50)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mylab.doctor')),
            ],
            options={
                'ordering': ('date_added',),
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientName', models.CharField(blank=True, max_length=200, null=True)),
                ('clientLogo', models.ImageField(default='default_logo.jpg', upload_to='company_logos')),
                ('addressLine1', models.CharField(blank=True, max_length=200, null=True)),
                ('province', models.CharField(blank=True, choices=[('Gauteng', 'Gauteng'), ('Free State', 'Free State'), ('Limpopo', 'Limpopo')], max_length=100)),
                ('postalCode', models.CharField(blank=True, max_length=10, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('emailAddress', models.CharField(blank=True, max_length=100, null=True)),
                ('taxNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Technique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abbr', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('number', models.CharField(blank=True, max_length=100, null=True)),
                ('dueDate', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('CURRENT', 'CURRENT'), ('EMAIL_SENT', 'EMAIL_SENT'), ('OVERDUE', 'OVERDUE'), ('PAID', 'PAID')], default='CURRENT', max_length=100)),
                ('notes', models.TextField(blank=True, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('prescription', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mylab.prescription')),
            ],
        ),
        migrations.CreateModel(
            name='Medicals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analysis_name', models.CharField(max_length=50)),
                ('abbr', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=255)),
                ('unit', models.CharField(choices=[('', '')], max_length=20)),
                ('regular_price', models.FloatField()),
                ('assured_price', models.FloatField()),
                ('collectors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mylab.collectors')),
                ('interval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mylab.interval')),
                ('technique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mylab.technique')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='results',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mylab.results'),
        ),
    ]

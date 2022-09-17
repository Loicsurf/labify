import datetime
from django.db import models


class LabTechnician(models.Model):
    pass


class Prescription(models.Model):
    def ids():
        no = Prescription.objects.count()
        if no == None:
            return 1
        else:
            return no + 1
    emp_id = models.IntegerField(('Code'), default=ids, unique=True, editable=False)


    id = models.CharField(primary_key=True, editable=False, max_length=30)
    def save(self, **kwargs):
        if not self.id:
            self.id = "{}{:02d}".format('Pat - ', self.emp_id)
        super().save(*kwargs)

    CNI = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    dob = models.DateField(null=True,help_text='Please Enter Your Correct Date Of Birth')
    @property
    def age(self):
        if(self.dob != None):
            age = datetime.date.today().year - self.dob.year
            return age

    gender_choices = [('M', 'Male'), ('F', 'Female'), ]
    gender = models.CharField(choices=gender_choices, max_length=50)

    marital_choices = [('Married', 'Married'),('Single', 'Single') ]
    marital_status = models.CharField(choices = marital_choices, max_length=50)
    telephone1 = models.IntegerField(blank=False)
    telephone2 = models.IntegerField(blank=True, null=True)
    status = (
        ('In Treatement', 'In Treatement'),
        ('Recovered', 'Recovered'),
        ('New Patient', 'New Patient'),
    )
    status = models.CharField(max_length=20, null=True, choices = status)

    # 3
    town_choices = [('Yaounde', 'Yaounde'), ('Douala', 'Douala'),
                    ('Bamenda', 'Bamenda'), ('Buea', 'Buea'), ('Baffoussam',
                                                         'Baffoussam'), ('Ngaoundere', 'Ngaoundere'), ('Ebolowa', 'Ebolowa'),
                    ('', ''), ('', ''), ('', ''), ('', ''), ('', ''),
                    ('', ''), ('', ''), ('', ''), ('', ''), ('', ''),
                    ('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ]
    town = models.CharField(choices=town_choices,
                            max_length=50)  # To be added in bulk

    address = models.CharField(max_length=20, blank=True)  # To be added in bulk

    occupation_choices = [('', ''), ('', ''), ]
    occupation = models.CharField(
        choices=occupation_choices, max_length=50, blank=True)  # To be added in bulk

    # physical_state_choices = [('', ''), ('', ''), ]
    # physical_state = models.CharField(
    #     choices=physical_state_choices, max_length=50, blank=True)  # To be added in bulk

    # insurance_choices = [('', ''), ('', ''), ]
    # insurance = models.CharField(
    #     choices=insurance_choices, max_length=50, blank=True)  # To be added in bulk

    # consulting_service_choices = [('', ''), ('', ''), ]
    # consulting_service = models.CharField(
    #     choices=consulting_service_choices, max_length=50, blank=True)  # To be added in bulk

    # private_initial_choices = [('', ''), ('', ''), ]
    # private_initial = models.CharField(
    #     choices=private_initial_choices, max_length=50, blank=True)  # To be added in bulk
    # ###############################################################################

    # clinical_info = models.CharField(max_length=50, blank=True)
    # prescribed_analyses = models.CharField(max_length=50, blank=True)
    # physiological_state = models.CharField(max_length=50, blank=True)
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('date_added',)

class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender_choices = [('M', 'Male'), ('F', 'Female'), ]
    gender = models.CharField(choices=gender_choices, max_length=50)

    def __str__(self):
        return str(self.first_name)


# class Analysis(models.Model):
#     additives = models.ForeignKey('Additives', on_delete=models.CASCADE)
#     collectors = models.ForeignKey('Collectors', on_delete=models.CASCADE)
#     measurement = models.ForeignKey('Measurement', on_delete=models.CASCADE)
#     interval = models.ForeignKey('Interval', on_delete=models.CASCADE)
#     technique = models.ForeignKey('Technique', on_delete=models.CASCADE)
#     observation = models.TextField(max_length=255)

#     paillaise_choices = [('Syrologie', 'Syrologie'), ('HIV', 'HIV'), ]
#     paillaise_noms = models.CharField(choices=paillaise_choices, max_length=50) #Noms de paillaise


class Additives(models.Model):
    name = models.CharField(max_length=50)
    abbre = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Collectors(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    additives = models.ForeignKey('Additives', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Measurement(models.Model):
    name = models.CharField(max_length=50)
    abbre = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Interval(models.Model):
    name = models.CharField(max_length=50)
    interval_choices = [('Max', 'Maximum'), ('Min', 'Minimum')]
    interval = models.CharField(choices=interval_choices, max_length=50)

    def __str__(self):
        return str(self.name)


class Technique(models.Model):
    name_choices = [('Observation', 'Observation'), ('Patience', 'Patience'), ]
    name = models.CharField(choices=name_choices, max_length=50)
    abbr = models.CharField(max_length=50)
    description = models.TextField(max_length=255)

    def __str__(self):
        return str(self.name)


class Medicals(models.Model): #analyse medical
    analysis_name = models.CharField(max_length=50)
    abbr = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    technique = models.ForeignKey('Technique', on_delete=models.CASCADE)
    unit_choices = [('', '')]
    unit = models.CharField(choices=unit_choices, max_length=20)
    interval = models.ForeignKey('Interval', on_delete=models.CASCADE)
    regular_price = models.FloatField()
    assured_price = models.FloatField()
    collectors = models.ForeignKey('Collectors', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.analysis_name)

import datetime
from django.db import models
from django.template.defaultfilters import slugify
from uuid import uuid4
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse


class Prescription(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    dob = models.DateField(null=True,help_text='Please Enter Your Correct Date Of Birth')
    @property
    def age(self):
        if(self.dob != None):
            age = datetime.date.today().year - self.dob.year
            return age

    gender_choices = [('Male', 'Male'), ('Female', 'Female') ]
    gender = models.CharField(choices=gender_choices, max_length=50)

    marital_choices = [('Married', 'Married'),('Single', 'Single') ]
    marital_status = models.CharField(choices = marital_choices, max_length=50)
    phone_number = PhoneNumberField(blank=True)
    emailAddress = models.CharField(null=True, blank=True, max_length=100)
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

    doctor = models.ForeignKey("Doctor", blank=True, null=True, on_delete=models.CASCADE)
    
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.town, self.uniqueId)


    def get_absolute_url(self):
        return reverse('prescription-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {} {}'.format(self.first_name, self.town, self.uniqueId))

        self.slug = slugify('{} {} {}'.format(self.first_name, self.town, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Prescription, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ('date_added',)


class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender_choices = [('M', 'Male'), ('F', 'Female'), ]
    gender = models.CharField(choices=gender_choices, max_length=50)

    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {}'.format(self.first_name, self.uniqueId)


    def get_absolute_url(self):
        return reverse('doctor-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.first_name, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.first_name, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Doctor, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.first_name)

class Results(models.Model):
    TERMS = [
    ('Mouffo Michael', 'Mouffo Michael'),
    ('Mandeng Grace', 'Mandeng Grace'),
    ('Mary Jane', 'Mary Jane'),
    ('Suh Samuel', 'Suh Samuel'),
    ]

    STATUS = [
    ('CURRENT', 'CURRENT'),
    ('EMAIL_SENT', 'EMAIL_SENT'),
    ('OVERDUE', 'OVERDUE'),
    ('PAID', 'PAID'),
    ]

    title = models.CharField(null=True, blank=True, max_length=100)
    paymentTerms = models.CharField(choices=TERMS, max_length=100)
    number = models.CharField(null=True, blank=True, max_length=100)
    dueDate = models.DateField(null=True, blank=True)
    status = models.CharField(choices=STATUS, default='CURRENT', max_length=100)
    notes = models.TextField(null=True, blank=True)

    #RELATED fields
    prescription = models.ForeignKey(Prescription,  blank=True, null=True, on_delete=models.SET_NULL)
    doctor = models.ForeignKey(Doctor, blank=True, null=True, on_delete=models.SET_NULL)

    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {}'.format(self.number, self.uniqueId)


    def get_absolute_url(self):
        return reverse('results-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.number, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.number, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Results, self).save(*args, **kwargs)


class Settings(models.Model):

    PROVINCES = [
    ('Gauteng', 'Gauteng'),
    ('Free State', 'Free State'),
    ('Limpopo', 'Limpopo'),
    ]

    #Basic Fields
    clientName = models.CharField(null=True, blank=True, max_length=200)
    clientLogo = models.ImageField(default='default_logo.jpg', upload_to='company_logos')
    addressLine1 = models.CharField(null=True, blank=True, max_length=200)
    province = models.CharField(choices=PROVINCES, blank=True, max_length=100)
    postalCode = models.CharField(null=True, blank=True, max_length=10)
    phoneNumber = models.CharField(null=True, blank=True, max_length=100)
    emailAddress = models.CharField(null=True, blank=True, max_length=100)
    taxNumber = models.CharField(null=True, blank=True, max_length=100)


    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {} {}'.format(self.clientName, self.province, self.uniqueId)


    def get_absolute_url(self):
        return reverse('settings-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {} {}'.format(self.clientName, self.province, self.uniqueId))

        self.slug = slugify('{} {} {}'.format(self.clientName, self.province, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Settings, self).save(*args, **kwargs)


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
        return str(self.abbre)


class Collectors(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    abbre = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    additives = models.ForeignKey('Additives', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.abbre)


class Measurement(models.Model):
    name = models.CharField(max_length=50)
    abbre = models.CharField(max_length=50)

    def __str__(self):
        return str(self.abbre)


class Interval(models.Model):
    name = models.CharField(max_length=50)
    interval = models.CharField(max_length=50)
    minimum = models.IntegerField()
    maximum = models.IntegerField()
    fix_value = models.IntegerField()

    def __str__(self):
        return str(self.name)


class Technique(models.Model):
    name = models.CharField(max_length=50)
    abbr = models.CharField(max_length=50)
    description = models.TextField(max_length=255)

    def __str__(self):
        return str(self.abbr)


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
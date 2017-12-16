from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.

"""

- firstname
- lastname
- date of birth
- zero or more addresses
- one or more phone numbers
- one or more emails

"""

STATE_CHOICES = (('AL', 'Alabama'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'),
                 ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'),
                 ('GA', 'Georgia'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'),
                 ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'),
                 ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'),
                 ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'),
                 ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'),
                 ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'),
                 ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'),
                 ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'),
                 ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'))


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Address(models.Model):

    street = models.CharField(max_length=250)
    street_2 = models.CharField(max_length=250, blank=True, null=True, default=None)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    zip = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    person = models.ForeignKey(Person, related_name="addresses")

    def __str__(self):
        return self.street + " " + self.street_2 + " " + self.city + " " + self.state + " " + str(self.zip) + " " + str(self.person)


class PhoneNumber(models.Model):
    PHONE_TYPE_CHOICES = (('work', 'Work'), ('home', 'Home'), ('cell', 'Cell'))
    number = models.BigIntegerField()
    type = models.CharField(max_length=10, choices=PHONE_TYPE_CHOICES, default='cell')
    person = models.ForeignKey(Person, related_name="phone_numbers")

class Email(models.Model):
    email = models.EmailField()
    person = models.ForeignKey(Person, related_name="emails")



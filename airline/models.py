from django.db import models

# Create your models here.

class User(models.Model):
    class Civilities(models.TextChoices):
        MR = 'M.'
        MME = 'Mme.'
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.TextField(choices=Civilities.choices)
    date_birth = models.DateField()
    email = models.EmailField(max_length=250)
    
    def __str__(self):
        return self.first_name + " " + self.last_name


class Plane(models.Model):
    model = models.CharField(max_length=50)
    seat_capacity = models.IntegerField(default=500)
    wireless = models.BooleanField()
    entertainment = models.BooleanField()
    restoration = models.BooleanField()
    
    def __str__(self):
        return self.model
 
   
class Airport(models.Model):
    city = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.city

    
class Company(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Flight(models.Model):
    price = models.DecimalField(max_digits=19, decimal_places=2, default='')
    flight_number = models.IntegerField(default=1)
    name = models.CharField(max_length=100, default=flight_number)
    date = models.DateField()
    hour_d = models.TimeField(blank=True, null=True)
    hour_a = models.TimeField(blank=True, null=True)
    duration = models.DurationField(help_text="Duration for flight in hh:mm:ss format")
    departure = models.ForeignKey(Airport, on_delete=models.DO_NOTHING, related_name='departure')
    arrival = models.ForeignKey(Airport, on_delete=models.DO_NOTHING, related_name='arrival')
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
 
   
class Booking(models.Model):
    date_resa = models.DateField(auto_now_add=True, blank=True, null=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    passenger = models.CharField(max_length=100, default=user)
    
    def __str__(self):
        return self.passenger

   
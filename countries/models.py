from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    population = models.IntegerField()
    description = models.TextField()
    independence_day = models.DateField()
    currency = models.CharField(max_length=50)
    continent = models.CharField(max_length=50, choices=[
        ('Africa', 'Africa'),
        ('Asia', 'Asia'),
        ('Europe', 'Europe'),
        ('North America', 'North America'),
        ('South America', 'South America'),
        ('Oceania', 'Oceania'),
        ('Antarctica', 'Antarctica')
    ])
    
    owner = models.CharField(max_length=100, blank=True)
    owner_email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    population = models.IntegerField()
    description = models.TextField()
    established_date = models.DateField()

    def __str__(self):
        return self.name

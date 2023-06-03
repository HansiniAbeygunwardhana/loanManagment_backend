from django.db import models

# Create your models here.

class Staffmember (models.Model):
        
    branch = (
            ('Polonnaruwa', 'Polonnaruwa'),
            ('Hingurakgoda', 'Hingurakgoda'),
            ('Diyasenpura', 'Diyasenpura'),
            ('Sewanapitiya', 'Sewanapitiya'),
            ('Dehiaththakandiya', 'Dehiaththakandiya'),
            ('Mahiyanganaya', 'Mahiyanganaya'),
    )
        
    name = models.CharField(max_length=100 , unique=True)
    address = models.CharField(max_length=100)
    dateofbirth = models.DateField()
    email = models.EmailField()
    branch = models.CharField(max_length=20 , choices=branch , default='Sewanapitiya')
    phone = models.CharField(max_length=10)
    nic = models.CharField(max_length=12)
        
    def __str__(self):
        return self.name
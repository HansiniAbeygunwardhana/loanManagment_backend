from django.db import models
from CustomerProfile.models import CustomerProfile as User
from django.conf import settings

# Create your models here.
class Loan(models.Model):
    
    branches = (
        ('Polonnaruwa' , 'Polonnaruwa'),
        ('Diyasenpura' , 'Diyasenpura'),
        ('Sewanapitiya' , 'Sewanapitiya'),
        ('Dehiaththakandiya' , 'Dehiaththakandiya'),
        ('Mahiyanaganaya' , 'Mahiyanaganaya'),
        )
    
    loan_id = models.AutoField(primary_key=True)
    loan_number = models.CharField(max_length=12, unique=True ,blank=True)
    username = models.ForeignKey(User, on_delete=models.SET_NULL , null=True)
    loaned_date = models.DateField( null=False)
    branch_location = models.CharField(max_length=20, choices=branches)
    loaned_amount = models.FloatField(null=False)
    bike_number = models.CharField(max_length=12)
    first_guarantor = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='first_guarantor', null=True)
    second_guarantor = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='second_guarantor', null=True)
    loan_period = models.IntegerField(null=False)
    
    def save(self, *args, **kwargs):
        
        BRANCH_CODES = {
            'Polonnaruwa': '71',
            'Diyasenpura': '51',
            'Sewanapitiya': '61',
            'Dehiaththakandiya': '12',
            'Mahiyanaganaya': '31',
                }
          
        if not self.loan_number:
                branch_code = BRANCH_CODES.get(self.branch_location)
                last_loan = Loan.objects.filter(loan_number__endswith=f'/{branch_code}').order_by('-loan_id').first()
                if last_loan:
                    last_number = int(last_loan.loan_number.split("-")[1])
                    next_number = last_number + 1
                else:
                    next_number = 1
                self.loan_number = f'2019-{next_number:03d}-{branch_code}'
            
        super().save(*args, **kwargs)


    def __str__(self):
        return self.loan_number
            
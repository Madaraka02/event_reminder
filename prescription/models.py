from django.db import models
from django.contrib.auth .models import User



class Medicine(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'

# deprioritised building this feature but adding to model in case we decide to do it as it's top of the 'stretch' list!
class Doctor(models.Model):
    name = models.CharField(max_length=200)
    url_fragment = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Prescription(models.Model):
    # one user can have many prescriptions, but one prescription can only have one user
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    # medicine can belong to many users, and one user can have many prescriptions, but a prescription can only have one medicine
    medicine = models.ForeignKey(Medicine, related_name='medicine', on_delete=models.CASCADE)
    # enter the DOSAGE the prescription eg "1 tablet of asprin"
    dosage = models.CharField(max_length=300)
    # including optional doctor id in case we get to stretch goals
    # doctor = models.ForeignKey(Doctor, related_name='doctor', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.dosage} of {self.medicine.name}'

class Reminder(models.Model):

    # one user can have many reminders, but one reminder can only have one user
    user = models.ForeignKey(User, related_name='reminder', on_delete=models.CASCADE)
    # one prescription can have many reminders, but one reminder can only have one prescription
    prescription = models.ForeignKey(Prescription, related_name='reminder', on_delete=models.CASCADE)
    # time of the reminder eg "8.00"
    time = models.TimeField()
    # date of the reminder eg "2022-04-01"
    start_of_reminder = models.DateField()
    end_of_reminder = models.DateField(null=True)
    


    def __str__(self):
        return f'{self.time} on {self.date_of_reminder}'

    @property
    def reminder_period(self):
        remaining = (self.end_of_reminder - start_of_reminder).days
        return remaining    
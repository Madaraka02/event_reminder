from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, phone_number, name, password=None):
        if not phone_number:
            raise ValueError('Users Must have a phone number')

        # phone_number =self.normalize_email(phone_number)
        user = self.model(phone_number=phone_number, name=name)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, name, password):
        user = self.create_user(phone_number, name, password)    
        user.is_superuser = True
        user.is_staff = True
        user.save
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    '''creating a custom user user'''
    phone_number = PhoneNumberField(unique=True)
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.phone_number

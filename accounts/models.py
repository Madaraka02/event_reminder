from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserAccountManager(BaseUserManager):
    def create_user(self, phone, name, password=None):
        if not phone:
            raise ValueError('Users Must have a phone number')

        # phone_number =self.normalize_email(phone_number)
        user = self.model(phone=phone, name=name)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, name, password):
        user = self.create_user(phone, name, password)    
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    '''creating a custom user user'''
    phone = PhoneNumberField(unique=True)
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
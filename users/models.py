import re

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'user_id': self.pk})

    def __str__(self):
        return self.email


class IpiNumber(models.Model):
    """
    There are two types of IPI number.
    Base number: A-123456789-1
    Name number: 00123456789
    However we also cater for the older CAE number.
    CAE number: 123456789
    """
    VALID_NUMBER_REGEX = '^[A-Z]-\d{9}-\d$|^\d{11}$|^\d{9}$'

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    number = models.CharField(
        blank=True,
        unique=True,
        max_length=13,
        validators=[
            RegexValidator(
                VALID_NUMBER_REGEX,
                message='Must be a valid IPI Number or CAE Number'
            ),
        ]
    )
    ipi_type = models.CharField(blank=True, max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.ipi_type = self.detect_ipi_type()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'user_id': self.user.pk})

    def __str__(self):
        return self.number

    def detect_ipi_type(self):
        """
        Base Number
        Name Number
        CAE Number
        """
        if self.number[0].isalpha():
            return 'Base'
        elif re.search('^\d{11}$', self.number):
            return 'Name'
        elif re.search('^\d{9}$', self.number):
            return 'CAE'
        else:
            return 'N/A'  # Perhaps raise error here instead?


class Pseudonym(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'user_id': self.user.pk})

    def __str__(self):
        return self.name

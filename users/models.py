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
        max_length=13,
        validators=[
            RegexValidator(
                VALID_NUMBER_REGEX,
                message='Must be a valid IPI Number or CAE Number'
            ),
        ]
    )
    ipi_type = models.CharField(blank=True, max_length=4)

    def __str__(self):
        return self.number


class Pseudonym(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

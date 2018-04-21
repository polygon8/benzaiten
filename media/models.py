from datetime import datetime

from django.db import models
from django.urls import reverse

from users.models import CustomUser


class Media(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(blank=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    duration = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Track(Media):
    bpm = models.PositiveIntegerField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('tracks')


class IsrcNumber(models.Model):
    COUNTRY_CODE = 'GB'
    REGISTRANT_CODE = 'PG8'

    track = models.OneToOneField(Track, on_delete=models.CASCADE)
    number = models.CharField(max_length=12, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.number = self.generate()
        super().save(*args, **kwargs)

    def generate(self):
        """
        ISRC Numbers have the following structure:
        Country Code
        Registrant Code
        Year
        5 digit Designation Code
        e.g GBABC1812345
        """
        return "{}{}{}{}".format(
            self.COUNTRY_CODE,
            self.REGISTRANT_CODE,
            self.this_year(),
            self.designation_code()
        )

    def this_year(self):
        return str(datetime.now().year)[-2:]

    def designation_code(self):
        try:
            latest = IsrcNumber.objects.latest('created_at')
        except IsrcNumber.DoesNotExist:
            latest = None

        if not latest or self.this_year() != latest.number[5:7]:
            next_designation_code = 1
        else:
            next_designation_code = int(latest.number[-5:]) + 1

        return "{:05}".format(next_designation_code)

    def __str__(self):
        return self.number

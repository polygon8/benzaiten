from django.db import models

from users.models import CustomUser
from media.choices import UsageCodes


class CueSheet(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    programme_title = models.CharField(max_length=255)
    production_company = models.CharField(max_length=255, blank=True)
    classification = models.CharField(max_length=255, blank=True)
    catalogue_number = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=4, blank=True)
    programme_duration = models.DurationField(blank=True, null=True)
    music_duration = models.DurationField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Cue(models.Model):
    cue_sheet = models.ForeignKey(CueSheet, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    cue_position = models.IntegerField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    usage_code = models.CharField(
        max_length=2,
        choices=UsageCodes.country_choices('GB'),
        blank=True,
        null=True
    )
    time_in = models.TimeField(blank=True, null=True)
    time_out = models.TimeField(blank=True, null=True)

    def usage_code_description(self):
        return next(
            item.value for item
            in self.UsageCodes.country_choices('GB')
            if item.name == self.usage_code
        )

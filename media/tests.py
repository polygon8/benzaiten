from django.test import TestCase
from mock import patch
from freezegun import freeze_time

from users.models import CustomUser
from .models import IsrcNumber, Track


def create_user():
    CustomUser.objects.create(
        email='rhodey@team-iron-man.com',
        password='WARMACHINEROX'
    )


def create_track():
    Track.objects.create(
        title='Something',
        user=CustomUser.objects.first()
    )


def create_isrc_numbers(tracks):
    for track in tracks:
        IsrcNumber.objects.create(track=track)


class IsrcNumberTest(TestCase):
    def setUp(self):
        create_user()

    def test_generated_isrc_number(self):
        create_track()
        create_isrc_numbers(Track.objects.all())

        self.assertEqual(
            'GBPG81800001',
            IsrcNumber.objects.first().number
        )

    def test_incremented_isrc_number(self):
        create_track()
        create_track()
        create_isrc_numbers(Track.objects.all())

        self.assertEqual(
            'GBPG81800002',
            IsrcNumber.objects.last().number
        )

    @freeze_time('Jan 1st, 2018')
    @patch('media.models.IsrcNumber')
    def test_isrc_number_resets_in_new_year(self, latest_isrc_number):
        create_track()

        number_from_2017 = IsrcNumber(track=Track.objects.first())
        number_from_2017.number = 'GBPG81712345'
        latest_isrc_number.query.latest.return_value = number_from_2017
        create_track()

        self.assertEqual(
            'GBPG81800001',
            IsrcNumber(track=Track.objects.last()).generate()
        )

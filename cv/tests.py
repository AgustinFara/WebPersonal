from django.test import TestCase, Client
from django.conf import settings
from django.urls import reverse
from .models import Work
import datetime
from unittest.mock import patch

# Create your tests here.

class WorkModelTests(TestCase):
    def test_date_started_english(self):
        settings.LANGUAGE_CODE = 'en-US'
        test_date = datetime.datetime(2010,1,3)
        work_english = Work(datestart=test_date,title='test_en',company='django')
        self.assertEqual(work_english.date_started(), 'January 2010')

    def test_date_started_german(self):
        settings.LANGUAGE_CODE = 'de-DE'
        test_date = datetime.datetime(1987,12,7)
        work_german = Work(datestart=test_date,title='test_de',company='django')
        self.assertEqual(work_german.date_started(), 'Dezember 1987')

    def test_date_started_italian(self):
        settings.LANGUAGE_CODE = 'it-IT'
        test_date = datetime.datetime(1950,10,11)
        work_italian = Work(datestart=test_date,title='test_it',company='django')
        self.assertEqual(work_italian.date_started(), 'Ottobre 1950')

    def test_date_finished_french(self):
        settings.LANGUAGE_CODE = 'fr-FR'
        test_date = datetime.datetime(2018,2,9)
        work_french = Work(datefinish=test_date,title='test_fr',company='django')
        self.assertEqual(work_french.date_finished(), 'Février 2018')

    def test_date_finished_portuguese(self):
        settings.LANGUAGE_CODE = 'pt-BR'
        test_date = datetime.datetime(1987,11,25)
        work_portuguese = Work(datefinish=test_date,title='test_br',company='django')
        self.assertEqual(work_portuguese.date_finished(), 'Novembro 1987')

    def test_date_finished_greek(self):
        settings.LANGUAGE_CODE = 'el-EL'
        test_date = datetime.datetime(1920,4,15)
        work_greek = Work(datefinish=test_date,title='test_el',company='django')
        self.assertEqual(work_greek.date_finished(), 'Απριλίου 1920')

    def test_dates_time_worked(self):
        test_date_st = datetime.datetime(1920,4,15)
        test_date_fi = datetime.datetime(1940,6,15)
        work_diff = Work(datestart=test_date_st,datefinish=test_date_fi,title='test_diff')
        self.assertEqual(work_diff.time_worked(), '20 años y 2 meses')

    def test_dates_time_worked_less_than_month(self):
        test_date_st = datetime.datetime(1990,4,15)
        test_date_fi = datetime.datetime(1990,5,10)
        work_diff = Work(datestart=test_date_st,datefinish=test_date_fi,title='test_diff')
        self.assertEqual(work_diff.time_worked(), 'Menos de un mes')

    def test_dates_time_worked_one_month(self):
        test_date_st = datetime.datetime(1989,12,15)
        test_date_fi = datetime.datetime(1990,1,14)
        work_diff = Work(datestart=test_date_st,datefinish=test_date_fi,title='test_diff')
        self.assertEqual(work_diff.time_worked(), '1 mes')

    def test_dates_time_worked_less_than_month_exact(self):
        test_date_st = datetime.datetime(1989,12,15)
        test_date_fi = datetime.datetime(1990,1,13)
        work_diff = Work(datestart=test_date_st,datefinish=test_date_fi,title='test_diff')
        self.assertEqual(work_diff.time_worked(), 'Menos de un mes')

    def test_dates_time_worked_year_and_month(self):
        test_date_st = datetime.datetime(1980,5,1)
        test_date_fi = datetime.datetime(1981,6,1)
        work_diff = Work(datestart=test_date_st,datefinish=test_date_fi,title='test_diff')
        self.assertEqual(work_diff.time_worked(), '1 año y 1 mes')


class TestEdadAbout(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('cv:about')

    @patch('cv.views.date')
    def test_edad_calculada_correctamente_en_cumpleaños(self, mock_datetime):
        """Prueba que si hoy esel cumpleaños de 2024, la edad sea exactamente 40"""
        mock_datetime.today.return_value = datetime.date(2024, 3, 4)
        mock_datetime.side_effect = lambda *args, **kwargs: datetime.date(*args, **kwargs)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['edad'], 40)

    @patch('cv.views.date')
    def test_edad_un_dia_antes_del_cumpleaños(self, mock_datetime):
        """Prueba que si hoy es un día antes de tu cumple en 2024, todavía devuelva 39"""
        mock_datetime.today.return_value = datetime.date(2024, 3, 3)
        mock_datetime.side_effect = lambda *args, **kwargs: datetime.date(*args, **kwargs)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['edad'], 39)

from django.test import TestCase
import unittest
from .models import Author_db, Exhibition_db, Card_db, Organization, Control, Directors, Fund_manager, Users
from django.urls import reverse

class View_Author_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Author_db.objects.create(name='Иванов И.И.', date_of_birth='2017-01-01', country='Россия')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/author/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('author'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('author'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_Author.html')

class View_Exhibition_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Exhibition_db.objects.create(name='Выставка', start_date='2017-01-01', finish_date='2017-01-01')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/exhibition/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('exhibition'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('exhibition'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_Exhibition.html')

class View_Card_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Card_db.objects.create(number='1', name='Ваза', create_date='2017-01-01', accuracy_date='точно')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/card/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('card'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('card'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_Card.html')

class View_Organization_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Organization.objects.create(name='ООО Рога и копыта', address='г. Новый', phone='+79523084233', person='Иванов И.И.')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/organization/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('organization'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('card'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_Organization.html')

class View_Control_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Control.objects.create(add_stor='2020-01-01', off_stor='2020-01-01', trans_ex='2020-01-01', return_ex='2020-01-01')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/control/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('control'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('control'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_Control.html')

class View_Directors_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Directors.objects.create(phone='+79523084233', position='Директор')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/directors/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('directors'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('directors'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_Directors.html')

class View_Fund_manager_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Fund_manager.objects.create(phone='+79523084233', position='Менеджер', fund_name='Художественный фонд')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/fund_manager/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('fund_manager'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('fund_manager'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_Fund_manager.html')

class View_Users_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Users.objects.create(number='1', name='Иванов И.И.')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/users/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('users'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('users'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_Users.html')
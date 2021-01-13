from django.test import TestCase
import unittest
from firstapp.models import Author_db,Exhibition_db,Card_db,Organization, Control, Users, Fund_manager, Directors

class Author_dbModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Author_db.objects.create(name='Иванов И.И.', date_of_birth='2017-01-01', country='Россия')

    def test_name_label(self):
        ad = Author_db.objects.get(id=1)
        field_label = ad._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_date_of_birth_label(self):
        ad = Author_db.objects.get(id=1)
        field_label = ad._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label, 'date_of_birth')

    def test_country_label(self):
        ad = Author_db.objects.get(id=1)
        field_label = ad._meta.get_field('country').verbose_name
        self.assertEquals(field_label, 'country')

    def test_name_max_length(self):
        ad = Author_db.objects.get(id=1)
        max_length = ad._meta.get_field('name').max_length
        self.assertEquals(max_length,120)

    def test_date_of_birth_max_length(self):
        ad = Author_db.objects.get(id=1)
        max_length = ad._meta.get_field('date_of_birth').max_length
        self.assertEquals(max_length,120)

    def test_country_length(self):
        ad = Author_db.objects.get(id=1)
        max_length = ad._meta.get_field('country').max_length
        self.assertEquals(max_length,120)

class Exhibition_dbModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Exhibition_db.objects.create(name='Выставка', start_date='2017-01-01', finish_date='2017-01-01')

    def test_name_label(self):
        ad = Exhibition_db.objects.get(id=1)
        field_label = ad._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_start_date_label(self):
        ad = Exhibition_db.objects.get(id=1)
        field_label = ad._meta.get_field('start_date').verbose_name
        self.assertEquals(field_label, 'start_date')

    def test_finish_date_label(self):
        ad = Exhibition_db.objects.get(id=1)
        field_label = ad._meta.get_field('finish_date').verbose_name
        self.assertEquals(field_label, 'finish_date')

    def test_country_length(self):
        ad = Exhibition_db.objects.get(id=1)
        max_length = ad._meta.get_field('country').max_length
        self.assertEquals(max_length, 120)

    def test_start_date_length(self):
        ad = Exhibition_db.objects.get(id=1)
        max_length = ad._meta.get_field('start_date').max_length
        self.assertEquals(max_length, 120)

    def test_finish_date_length(self):
        ad = Exhibition_db.objects.get(id=1)
        max_length = ad._meta.get_field('finish_date').max_length
        self.assertEquals(max_length, 120)

class Card_dbModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Card_db.objects.create(number='1', name='Ваза', create_date='2017-01-01', accuracy_date='точно')

    def test_number_label(self):
        ad = Card_db.objects.get(id=1)
        field_label = ad._meta.get_field('number').verbose_name
        self.assertEquals(field_label, 'number')

    def test_name_label(self):
        ad = Card_db.objects.get(id=1)
        field_label = ad._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_create_date_label(self):
        ad = Card_db.objects.get(id=1)
        field_label = ad._meta.get_field('create_date').verbose_name
        self.assertEquals(field_label, 'create_date')

    def test_accuracy_date_label(self):
        ad = Card_db.objects.get(id=1)
        field_label = ad._meta.get_field('accuracy_date').verbose_name
        self.assertEquals(field_label, 'accuracy_date')

    def test_number_length(self):
        ad = Card_db.objects.get(id=1)
        max_length = ad._meta.get_field('number').max_length
        self.assertEquals(max_length, 120)

    def test_name_length(self):
        ad = Card_db.objects.get(id=1)
        max_length = ad._meta.get_field('name').max_length
        self.assertEquals(max_length, 120)

    def test_create_date_length(self):
        ad = Card_db.objects.get(id=1)
        max_length = ad._meta.get_field('create_date').max_length
        self.assertEquals(max_length, 120)

    def test_accuracy_date_length(self):
        ad = Card_db.objects.get(id=1)
        max_length = ad._meta.get_field('accuracy_date').max_length
        self.assertEquals(max_length, 120)

class OrganizationModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Organization.objects.create(name='ООО Рога и копыта', address='г. Новый', phone='+79523084233', person='Иванов И.И.')

    def test_name_label(self):
        ad = Organization.objects.get(id=1)
        field_label = ad._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_address_label(self):
        ad = Organization.objects.get(id=1)
        field_label = ad._meta.get_field('address').verbose_name
        self.assertEquals(field_label, 'address')

    def test_phone_label(self):
        ad = Organization.objects.get(id=1)
        field_label = ad._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'phone')

    def test_person_label(self):
        ad = Organization.objects.get(id=1)
        field_label = ad._meta.get_field('person').verbose_name
        self.assertEquals(field_label, 'person')

    def test_name_length(self):
        ad = Organization.objects.get(id=1)
        max_length = ad._meta.get_field('name').max_length
        self.assertEquals(max_length, 120)

    def test_address_length(self):
        ad = Organization.objects.get(id=1)
        max_length = ad._meta.get_field('address').max_length
        self.assertEquals(max_length, 120)

    def test_phone_length(self):
        ad = Organization.objects.get(id=1)
        max_length = ad._meta.get_field('phone').max_length
        self.assertEquals(max_length, 120)

    def test_person_length(self):
        ad = Organization.objects.get(id=1)
        max_length = ad._meta.get_field('person').max_length
        self.assertEquals(max_length, 120)

class ControlModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Control.objects.create(add_stor='2020-01-01', off_stor='2020-01-01', trans_ex='2020-01-01', return_ex='2020-01-01')

    def test_add_stor_label(self):
        ad = Control.objects.get(id=1)
        field_label = ad._meta.get_field('add_stor').verbose_name
        self.assertEquals(field_label, 'add_stor')

    def test_off_stor_label(self):
        ad = Control.objects.get(id=1)
        field_label = ad._meta.get_field('off_stor').verbose_name
        self.assertEquals(field_label, 'off_stor')

    def test_trans_ex_label(self):
        ad = Control.objects.get(id=1)
        field_label = ad._meta.get_field('trans_ex').verbose_name
        self.assertEquals(field_label, 'trans_ex')

    def test_return_ex_label(self):
        ad = Control.objects.get(id=1)
        field_label = ad._meta.get_field('return_ex').verbose_name
        self.assertEquals(field_label, 'return_ex')

    def test_name_max_length(self):
        ad = Control.objects.get(id=1)
        max_length = ad._meta.get_field('name').max_length
        self.assertEquals(max_length,120)

    def test_off_stor_length(self):
        ad = Control.objects.get(id=1)
        max_length = ad._meta.get_field('name').max_length
        self.assertEquals(max_length,120)

    def test_trans_ex_length(self):
        ad = Control.objects.get(id=1)
        max_length = ad._meta.get_field('name').max_length
        self.assertEquals(max_length,120)

    def test_return_ex_length(self):
        ad = Control.objects.get(id=1)
        max_length = ad._meta.get_field('name').max_length
        self.assertEquals(max_length,120)

class Users_dbModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Users.objects.create(number='1', name='Иванов И.И.')

    def test_number_label(self):
        ad = Users.objects.get(id=1)
        field_label = ad._meta.get_field('number').verbose_name
        self.assertEquals(field_label, 'number')

    def test_name_label(self):
        ad = Users.objects.get(id=1)
        field_label = ad._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_number_length(self):
        ad = Users.objects.get(id=1)
        max_length = ad._meta.get_field('number').max_length
        self.assertEquals(max_length,120)

    def test_name_length(self):
        ad = Users.objects.get(id=1)
        max_length = ad._meta.get_field('name').max_length
        self.assertEquals(max_length,120)

class Fund_manager_dbModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Fund_manager.objects.create(phone='+79523084233', position='Менеджер', fund_name='Художественный фонд')

    def test_phone_label(self):
        ad = Fund_manager.objects.get(id=1)
        field_label = ad._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'phone')

    def test_position_label(self):
        ad = Fund_manager.objects.get(id=1)
        field_label = ad._meta.get_field('position').verbose_name
        self.assertEquals(field_label, 'position')

    def test_fund_name_label(self):
        ad = Fund_manager.objects.get(id=1)
        field_label = ad._meta.get_field('fund_name').verbose_name
        self.assertEquals(field_label, 'fund_name')

    def test_phone_length(self):
        ad = Fund_manager.objects.get(id=1)
        max_length = ad._meta.get_field('phone').max_length
        self.assertEquals(max_length, 120)

    def test_position_length(self):
        ad = Fund_manager.objects.get(id=1)
        max_length = ad._meta.get_field('position').max_length
        self.assertEquals(max_length, 120)

    def test_fund_name_length(self):
        ad = Fund_manager.objects.get(id=1)
        max_length = ad._meta.get_field('fund_name').max_length
        self.assertEquals(max_length, 120)

class Directors_dbModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Directors.objects.create(phone='+79523084233', position='Директор')

    def test_phone_label(self):
        ad = Directors.objects.get(id=1)
        field_label = ad._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'phone')

    def test_position_label(self):
        ad = Directors.objects.get(id=1)
        field_label = ad._meta.get_field('position').verbose_name
        self.assertEquals(field_label, 'position')

    def test_phone_length(self):
        ad = Directors.objects.get(id=1)
        max_length = ad._meta.get_field('phone').max_length
        self.assertEquals(max_length, 120)

    def test_position_length(self):
        ad = Directors.objects.get(id=1)
        max_length = ad._meta.get_field('position').max_length
        self.assertEquals(max_length, 120)


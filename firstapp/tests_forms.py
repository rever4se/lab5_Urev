from django.test import TestCase
import unittest
from firstapp.forms import AddUser, AddManager, AddDirector, AddData, AddCard, AddExh, AddOrg, AddControl

class AddDataFormTest(TestCase):

    def test_name_label(self):
        form = AddData()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'Имя')

    def test_date_label(self):
        form = AddData()
        self.assertTrue(form.fields['date_of_birth'].label == None or form.fields['date_of_birth'].label == 'Дата рождения')

    def test_country_label(self):
        form = AddData()
        self.assertTrue(form.fields['country'].label == None or form.fields['country'].label == 'Страна')

    def test_resoult(self):
        form = AddData(data={'name': "Иван Иванович", 'date_of_birth': "2017-03-03", 'country': 'Россия'})
        self.assertTrue(form.is_valid())

class AddExhFormTest(TestCase):

    def test_name_label(self):
        form = AddExh()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'Название выставки')

    def test_start_label(self):
        form = AddExh()
        self.assertTrue(form.fields['start_date'].label == None or form.fields['start_date'].label == 'Дата началы выставки')

    def test_finish_label(self):
        form = AddExh()
        self.assertTrue(form.fields['finish_date'].label == None or form.fields['finish_date'].label == 'Дата окончания выставки')

    def test_resoult(self):
        form = AddExh(data={'name': "Выставка народных ремесел", 'start_date': "2020-01-01", 'finish_date': "2020-06-01"})
        self.assertTrue(form.is_valid())

class AddCardFormTest(TestCase):

    def test_number_label(self):
        form = AddCard()
        self.assertTrue(form.fields['number'].label == None or form.fields['number'].label == 'Номер карты')

    def test_name_label(self):
        form = AddCard()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'Название экспоната')

    def test_create_label(self):
        form = AddCard()
        self.assertTrue(form.fields['create_date'].label == None or form.fields['create_date'].label == 'Дата создания карты')

    def test_accuracy_label(self):
        form = AddCard()
        self.assertTrue(form.fields['accuracy_date'].label == None or form.fields['accuracy_date'].label == 'Точно ли определена дата')

    def test_exh_label(self):
        form = AddCard()
        self.assertTrue(form.fields['exhibition_id'].label == None or form.fields['exhibition_id'].label == 'Выставка')

    def test_auth_label(self):
        form = AddCard()
        self.assertTrue(form.fields['author_id'].label == None or form.fields['author_id'].label == 'Автор')

    def test_resoult(self):
        form = AddCard(data={'number': "1", 'name': "Ваза", 'create_date': "2020-01-01", 'accuracy_date': "2020-05-01", 'exhibition_id': 1, 'author_id': 1})
        self.assertTrue(form.is_valid())

class AddOrgFormTest(TestCase):

    def test_name_label(self):
        form = AddOrg()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'Название орг.')

    def test_address_label(self):
        form = AddOrg()
        self.assertTrue(form.fields['address'].label == None or form.fields['address'].label == 'Адресс орг.')

    def test_phone_label(self):
        form = AddOrg()
        self.assertTrue(form.fields['phone'].label == None or form.fields['phone'].label == 'Телефон орг.')

    def test_person_label(self):
        form = AddOrg()
        self.assertTrue(form.fields['person'].label == None or form.fields['person'].label == 'Контакт. персона')

    def test_exh_label(self):
        form = AddOrg()
        self.assertTrue(form.fields['exhibition_id'].label == None or form.fields['exhibition_id'].label == 'Выставка')

    def test_resoult(self):
        form = AddOrg(data={'name': "ООО Спайдер", 'address': "г. Москва, ул. Ильича, 2", 'phone': "+79523084233", 'person': "Иван И.И.", 'exhibition_id': 1})
        self.assertTrue(form.is_valid())

class AddControlFormTest(TestCase):

    def test_card_label(self):
        form = AddControl()
        self.assertTrue(form.fields['card_id'].label == None or form.fields['card_id'].label == 'Карта')

    def test_author_label(self):
        form = AddControl()
        self.assertTrue(form.fields['author_id'].label == None or form.fields['author_id'].label == 'Автор')

    def test_astore_label(self):
        form = AddControl()
        self.assertTrue(form.fields['add_stor'].label == None or form.fields['add_stor'].label == 'Прием на хранение')

    def test_ostore_label(self):
        form = AddControl()
        self.assertTrue(form.fields['off_stor'].label == None or form.fields['off_stor'].label == 'Списание')

    def test_exh_label(self):
        form = AddControl()
        self.assertTrue(form.fields['exhibition_id'].label == None or form.fields['exhibition_id'].label == 'Выставка')

    def test_org_label(self):
        form = AddControl()
        self.assertTrue(form.fields['organization_id'].label == None or form.fields['organization_id'].label == 'Организация')

    def test_trans_label(self):
        form = AddControl()
        self.assertTrue(form.fields['trans_ex'].label == None or form.fields['trans_ex'].label == 'Передача на выставку')

    def test_return_label(self):
        form = AddControl()
        self.assertTrue(form.fields['return_ex'].label == None or form.fields['return_ex'].label == 'Прием с выставки')

    def test_resoult(self):
        form = AddControl(data={'card_id': 1, 'author_id': 1, 'add_stor': "2020-01-01", 'off_stor': "2020-02-01", 'exhibition_id': 1, 'organization_id': 1, 'trans_ex': "2020-01-01", 'return_ex': "2020-02-01"})
        self.assertTrue(form.is_valid())

class AddUserFormTest(TestCase):

    def test_number_label(self):
        form = AddUser()
        self.assertTrue(form.fields['number'].label == None or form.fields['number'].label == 'Номер пользователя')

    def test_name_label(self):
        form = AddUser()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'ФИО пользователя')

    def test_resoult(self):
        form = AddUser(data={'number': "1", 'name': "Иванов И.И."})
        self.assertTrue(form.is_valid())

class AddDirectorFormTest(TestCase):

    def test_users_label(self):
        form = AddDirector()
        self.assertTrue(form.fields['users_id'].label == None or form.fields['users_id'].label == 'Пользователь')

    def test_phone_label(self):
        form = AddDirector()
        self.assertTrue(form.fields['phone'].label == None or form.fields['phone'].label == 'Номер телефона')

    def test_position_label(self):
        form = AddDirector()
        self.assertTrue(form.fields['position'].label == None or form.fields['position'].label == 'Должность')

    def test_resoult(self):
        form = AddDirector(data={'users_id': 1, 'phone': "+79523084233", 'position': "Директор"})
        self.assertTrue(form.is_valid())

class AddManagerFormTest(TestCase):

    def test_users_label(self):
        form = AddManager()
        self.assertTrue(form.fields['users_id'].label == None or form.fields['users_id'].label == 'Пользователь')

    def test_phone_label(self):
        form = AddManager()
        self.assertTrue(form.fields['phone'].label == None or form.fields['phone'].label == 'Номер телефона')

    def test_position_label(self):
        form = AddManager()
        self.assertTrue(form.fields['position'].label == None or form.fields['position'].label == 'Должность')

    def test_fund_label(self):
        form = AddManager()
        self.assertTrue(form.fields['fund_name'].label == None or form.fields['fund_name'].label == 'Название фонда')

    def test_resoult(self):
        form = AddManager(data={'users_id': 1, 'phone': "+79523084233", 'fund_name': "Художественный фонд", 'position': "Директор"})
        self.assertTrue(form.is_valid())


from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from company.models import Company, Country
from user.models import User


class CompanyTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(email='admin@mail.ru',
                                             password='123',
                                             username='admin',
                                             is_active=True)
        self.client.force_authenticate(user=self.user)

    def test_CRUD_company(self):
        data_product = {'title': 'product', 'model': 'Model', 'sell_start': '2001-01-01:10:10:10-01:00'}
        data_country = {'title': 'country'}
        data_town = {'title': 'town'}

        data_company = {'category': Company.Category.Manufactury,
                        'title': 'Завод',
                        'email': 'zavod@mail.ru',
                        'country': '1',
                        'town': '1',
                        'street': 'улица',
                        'products': ['1', ],
                        'building': 'строение',
                        'supplier': '',
                        'debt': '15',
                        'created': '2024-03-09T22:34:57.531314Z'}

        data_country_response = {'id': 1, 'title': 'country'}
        data_town_response = {'id': 1, 'title': 'town'}

        data_company_response = {'id': 1,
                                 'category': 'manufactury',
                                 'title': 'Завод',
                                 'email': 'zavod@mail.ru',
                                 'street': 'улица',
                                 'building': 'строение',
                                 'debt': None,
                                 'created': '2024-03-09T22:34:57.531314Z',
                                 'country': 1,
                                 'town': 1,
                                 'supplier': None,
                                 'products': [1]
                                 }

        # CREATE
        self.client.post('/products/', data=data_product)
        response = self.client.post('/countries/', data=data_country)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), data_country_response)
        self.assertTrue(Country.objects.all().exists())

        response = self.client.post('/towns/', data=data_town)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), data_town_response)
        self.assertTrue(Country.objects.all().exists())

        response = self.client.post('/companies/', data=data_company)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), data_company_response)
        self.assertTrue(Country.objects.all().exists())

        # UPDATE
        response = self.client.patch('/countries/1/', data={'title': 'country1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.patch('/towns/1/', data={'title': 'town1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.patch('/companies/1/', data={'title': 'company1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # GET
        response = self.client.get('/countries/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/towns/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/companies/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # GET_LIST
        response = self.client.get('/companies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertNumQueries(1)

        response = self.client.get('/companies/?country=1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNumQueries(1)

        response = self.client.get('/companies/?country=2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNumQueries(0)

        # DELETE
        response = self.client.delete('/companies/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.delete('/countries/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.delete('/towns/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

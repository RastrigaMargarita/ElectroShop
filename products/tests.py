from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from user.models import User


class CompanyTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(email='admin@mail.ru',
                                             password='123',
                                             username='admin',
                                             is_active=True)
        self.client.force_authenticate(user=self.user)

    def test_CRUD_product(self):

        data_product = {'title': 'product', 'model': 'Model', 'sell_start': '2001-01-01T11:10:10Z'}
        data_product_response = {'id': 2, 'title': 'product', 'model': 'Model', 'sell_start': '2001-01-01T11:10:10Z'}

        # CREATE
        response = self.client.post('/products/', data=data_product)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), data_product_response)

        # UPDATE
        response = self.client.patch('/products/2/', data={'title': 'country1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # GET
        response = self.client.get('/products/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # GET_LIST
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertNumQueries(1)

        # DELETE
        response = self.client.delete('/products/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

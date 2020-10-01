from rest_framework.test import APITestCase
from rest_framework import status


class OpenAPITestCases(APITestCase):

    def get_token(self):
        url = "http://localhost:8000/token/"
        username = input("enter the username")
        password = input("enter the password")
        data = {
            "username": username,
            "password": password
        }
        response = self.client.post(url, data, format='json')
        print(response)
        if response.status_code == 200:
            token = response.json()
            print("Token: {}".format(token))
        else:
            print("Invalid user, fill the following details to register")
            url = "http://localhost:8000/register/"
            username = input("enter the username")
            password = input("enter the password")
            confirm_password = input("confirm password")
            email = input("enter email")
            data = {
                "username": username,
                "password": password,
                "password2": confirm_password,
                "email": email
            }
            response = self.client.post(url, data, format='json')
            token = response.json()
            print("Token: {}".format(token))
        return token['access']

    def create_contact(self):
        print("***********************Inside create*************************")
        headers = {'HTTP_AUTHORIZATION': "Token " + self.get_token(), 'Content-Type': 'application/json'}
        name = input("enter contact name")
        email = input("enter contact email")
        phone = input("enter contact phone number")
        url = "http://localhost:8000/contact-book/"
        data = {
            "name": name,
            "email": email,
            "phone": phone
        }
        response = self.client.post(url, data, format='json', **headers)
        if response.status_code == 201:
            print(response.status_code, response.data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        else:
            print(response.status_code, response.data)

    def update_contact(self):
        print("***********************Inside update*************************")
        headers = {'HTTP_AUTHORIZATION': "Token " + self.get_token(), 'Content-Type': 'application/json'}
        name = input("enter contact name")
        email = input("enter contact email")
        phone = input("enter contact phone number")
        url = "http://localhost:8000/contact-book/"
        data = {
            "name": name,
            "email": email,
            "phone": phone
        }
        response = self.client.put(url, data, format='json', **headers)
        if response.status_code == 200:
            print(response.status_code, response.data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        else:
            print(response.status_code, response.data)

    def delete_contact(self):
        print("***********************Inside delete*************************")
        headers = {'HTTP_AUTHORIZATION': "Token " + self.get_token(), 'Content-Type': 'application/json'}
        email = input("enter contact email")
        url = "http://localhost:8000/contact-book/"
        response = self.client.delete(url, {"email": email}, format='json', **headers)
        if response.status_code == 204:
            print(response.status_code, response.data)
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        else:
            print(response.status_code, response.data)

    def get_contacts(self):
        print("***********************Inside list*************************")
        headers = {'HTTP_AUTHORIZATION': "Token " + self.get_token(), 'Content-Type': 'application/json'}
        url = "http://localhost:8000/contact-book/"
        response = self.client.get(url, format='json', **headers)
        if response.status_code == 200:
            print(response.data)
        else:
            print(response.status_code, response.data)

    def test_a(self):
        self.get_contacts()
        self.create_contact()
        self.update_contact()
        self.delete_contact()

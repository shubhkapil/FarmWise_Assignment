import unittest
import json
import requests

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://localhost:5000'
        self.auth_header = {
            'Authorization': 'Basic YWRtaW46cGFzc3dvcmQ='
        }

    def test_add_book(self):
        url = f'{self.base_url}/books'
        payload = {
            "title": "Test Book",
            "author": "Test Author",
            "isbn": "123-456-7890",
            "price": 10.0,
            "quantity": 5
        }
        response = requests.post(url, headers=self.auth_header, data=json.dumps(payload))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Book added successfully.'})

    def test_get_books(self):
        url = f'{self.base_url}/books'
        response = requests.get(url, headers=self.auth_header)
        self.assertEqual(response.status_code, 200)

    def test_get_book_by_isbn(self):
        url = f'{self.base_url}/books/123-456-7890'
        response = requests.get(url, headers=self.auth_header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'title': 'Test Book',
            'author': 'Test Author',
            'isbn': '123-456-7890',
            'price': 10.0,
            'quantity': 5
        })

    def test_update_book(self):
        url = f'{self.base_url}/books/123-456-7890'
        payload = {
            "title": "Updated Test Book",
            "author": "Updated Test Author",
            "price": 15.0,
            "quantity": 10
        }
        response = requests.put(url, headers=self.auth_header, data=json.dumps(payload))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Book updated successfully.'})

        url = f'{self.base_url}/books/123-456-7890'
        response = requests.get(url, headers=self.auth_header)
        self.assertEqual(response.json(), {
            'title': 'Updated Test Book',
            'author': 'Updated Test Author',
            'isbn': '123-456-7890',
            'price': 15.0,
            'quantity': 10
        })

    def test_delete_book(self):
        url = f'{self.base_url}/books/123-456-7890'
        response = requests.delete(url, headers=self.auth_header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Book deleted successfully.'})

        url = f'{self.base_url}/books/123-456-7890'
        response = requests.get(url, headers=self.auth_header)
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
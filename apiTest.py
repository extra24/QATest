import requests
import unittest

# API Request 테스트 예제
class TestAPI(unittest.TestCase):

    def test_get_request(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertAlmostEqual(json_response["userId"], 1)
        self.assertEqual(json_response["id"], 1)

    def test_post_request(self):
        headers = {'Content-type': 'application/json'}
        data = '{"title": "testTitle", "body": "testBody", "userId": 1}'
        response = requests.post("https://jsonplaceholder.typicode.com/posts", headers=headers, data=data)
        self.assertEqual(response.status_code, 201)
        json_response = response.json()
        self.assertEqual(json_response["title"], "testTitle")

if __name__ == "__main__":
    unittest.main()


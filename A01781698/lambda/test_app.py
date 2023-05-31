from handler import handler
import unittest

class MainTest(unittest.TestCase):
    def test_handler(self):
        result = handler()
        self.assertEqual(result,{
        'statusCode': 200,
        'body': 'Hello from lambda Uriel'
    })

if __name__ == '__main__':
    unittest.main()

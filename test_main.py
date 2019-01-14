import httpretty
import unittest
import main

class TestCases(unittest.TestCase):

    def setUp(self):
        self.url = "https://creativecommons.org/about/contact/"

        self.emails = [
            'info@creativecommons.org.',
            'info@creativecommons.org.',
            'info@creativecommons.org',
            'info@creativecommons.org',
            'info@creativecommons.org',
            'info@creativecommons.org.',
            'audit@creativecommons.org',
            'audit@creativecommons.org',
            'info@creativecommons.org',
            'info@creativecommons.org'
        ]

        self.unique_emails = [
            "info@creativecommons.org",
            "audit@creativecommons.org"
        ]

        with open("tests/sample_data.txt") as f:
            self.sample_data = f.read()

    @httpretty.activate
    def test_get_website_data_response(self):
        

        httpretty.register_uri(httpretty.GET, self.url, body = self.sample_data)

        # use
        response = main.get_website_data(self.url)
        self.assertEqual(response, self.sample_data)

    def test_find_emails(self):

        self.assertEqual(main.find_emails(self.sample_data), self.emails)

    def test_remove_duplicate_emails(self):

        self.assertEqual(main.remove_duplicate_emails(self.emails), self.unique_emails)

    
if __name__ == "__main__":
    unittest.main()
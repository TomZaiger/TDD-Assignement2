import unittest
from src.Incidents import Incident
from unittest.mock import patch, Mock


class IncidentsFeatureTest(unittest.TestCase):
    sample = {
        "incidents": [
            {
                "id": 114480,
                "title": "Stolen Unknown(black and pink)",
                "description": "",
                "address": "Bedford, Mk401bl, GB",
                "occurred_at": 1584549626,
                "updated_at": 1584554436,
                "url": "https://bikewise.org/api/v1/incidents/114480",
                "source": {
                    "name": "BikeIndex.org",
                    "html_url": "https://bikeindex.org/bikes/701741",
                    "api_url": "https://bikeindex.org/api/v1/bikes/701741"
                },
                "media": {
                    "image_url": "https://files.bikeindex.org/uploads/Pu/228068/large_IMG_20200315_084521.jpg",
                    "image_url_thumb": "https://files.bikeindex.org/uploads/Pu/228068/small_IMG_20200315_084521.jpg"
                },
                "location_type": None,
                "location_description": None,
                "type": "Theft",
                "type_properties": None
            }
        ]
    }

    @patch('src.Incidents.requests.get')
    def test_titles(self, mock_obj):
        mock_obj.return_value = Mock(ok=True)
        mock_obj.return_value.json.return_value = self.sample
        sample2 = Incident({'per_page': 1})

        # Expected
        sample1_image_urls = ["https://files.bikeindex.org/uploads/Pu/228068/large_IMG_20200315_084521.jpg"]
        sample1_image_urls_type = []
        sample1_titles = ["Stolen Unknown(black and pink)"]
        sample1_titles_type = []

        # Run
        sample2_image_urls = sample2.get_image_urls()
        sample2_titles = sample2.get_titles()

        # Assert
        self.assertEqual(sample1_image_urls, sample2_image_urls)
        'self.assertIsInstance(sample1_image_urls_type, sample2_image_urls)'
        self.assertIsNotNone(sample1_image_urls)
        self.assertEqual(sample1_titles, sample2_titles)
        'self.assertIsInstance(sample1_titles_type, sample2_titles)'
        self.assertIsNotNone(sample1_titles)

    @patch('src.Incidents.requests.get')
    def test_image_urls(self, mock_obj):
        mock_obj.return_value = Mock(ok=True)
        mock_obj.return_value.json.return_value = self.sample
        sample2 = Incident({'per_page': 1})

        # Expected
        sample1_image_urls = ["https://files.bikeindex.org/uploads/Pu/228068/large_IMG_20200315_084521.jpg"]
        sample1_image_urls_type = list
        sample1_titles = ["Stolen Unknown(black and pink)"]
        sample1_titles_type = list

        # Run
        sample2_image_urls = sample2.get_image_urls()
        sample2_titles = sample2.get_titles()

        # Assert
        self.assertEqual(sample1_image_urls, sample2_image_urls)
        self.assertIsInstance(sample1_image_urls, sample1_image_urls_type)
        self.assertIsNotNone(sample1_image_urls)
        self.assertEqual(sample2_titles, sample2_titles)
        self.assertIsInstance(sample2_titles, sample1_titles_type)
        self.assertIsNotNone(sample1_titles)

    if __name__ == '__main__':
        unittest.main()

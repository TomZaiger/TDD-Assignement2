import unittest
from src.Locations import Location
from unittest.mock import patch, Mock


class LocationsFeatureTest(unittest.TestCase):
    sample = {
                "type": "FeatureCollection",
                "features": [
                        {
                            "type": "Feature",
                            "properties": {
                                "id": 114480,
                                "type": "Theft",
                                "occurred_at": 1584549626
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -0.4741953,
                                    52.1331768
                                ]
                            }
                        }
                ]
    }

    @patch('src.Locations.requests.get')
    def test_coordinates(self, mock_obj):
        mock_obj.return_value = Mock(ok=True)
        mock_obj.return_value.json.return_value = self.sample
        sample2 = Location({'limit': 1})

        # Expected
        sample1_coordinates = [[-0.4741953, 52.1331768]]
        sample1_coordinates_type = list

        # Run
        sample2_coordinates = sample2.get_coordinates()

        # Assert
        self.assertIsNotNone(sample1_coordinates)
        self.assertIsInstance(sample2_coordinates, sample1_coordinates_type)
        self.assertEqual(sample1_coordinates, sample2_coordinates)

    @patch('src.Locations.requests.get')
    def test_dates(self, mock_obj):
        mock_obj.return_value = Mock(ok=True)
        mock_obj.return_value.json.return_value = self.sample
        sample2 = Location({'limit': 1})

        # Expected
        sample1_dates = ['18/03/20 18:40:26']
        sample1_dates_type = list

        # Run
        sample2_dates = sample2.get_dates()

        # Assert
        self.assertIsNotNone(sample1_dates)
        self.assertIsInstance(sample1_dates, sample1_dates_type)
        self.assertEqual(sample1_dates, sample2_dates)

    if __name__ == '__main__':
        unittest.main()

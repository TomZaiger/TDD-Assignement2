import unittest
from src.Incidents import feature1
from unittest.mock import Mock


class IncidentsFeatureTest(unittest.TestCase):
    @patch('src.feature1.requests.get')
    def test1(self, mock_obj):
        json_sample = {
                        "incidents": [
                            {
                                "id": 114469,
                                "title": "Sidewalk",
                                "description": "Attachment to fire hydrant sticking on to the sidewalk. "
                                               "Appears Dangerous, especially for a little kids riding their bikes by. "
                                               "Please check and maybe twist"
                                               " to the side or put some kind of cones there. "
                                               "Thank you",
                                "address": "283 Countryhaven Rd Encinitas 92024, United States",
                                "occurred_at": 1584503541,
                                "updated_at": 1584533778,
                                "url": "https://bikewise.org/api/v1/incidents/114469",
                                "source": {
                                    "name": "SeeClickFix.com",
                                    "html_url": "https://seeclickfix.com/issues/7561404",
                                    "api_url": "https://seeclickfix.com/api/v2/issues/7561404"
                                },
                                "media": {
                                    "image_url": "https://seeclickfix.com/files/issue_images/0167/0483/image.jpg",
                                    "image_url_thumb":
                                        "https://seeclickfix.com/files/issue_images/0167/0483/image_square.jpg"
                                },
                                "location_type": None,
                                "location_description": None,
                                "type": "Hazard",
                                "type_properties": None
                                }
                            ]
                    }
        mock_obj.return_value = Mock(ok=True)
        mock_obj.return_value.json.return_value = json_sample
        sample1 = feature1()


""" Module test_datetimehelper - Unit test module for testing datetimehelper module"""
import unittest
import datetime 
from unittest.mock import patch 
import datetimehelper


class DateTimeHelperTestCase(unittest.TestCase):
    def setUp(self):
        print("setting up . . .")
        self.obj = datetimehelper.DateTimeHelper()
    def test_date(self):
        """Test date() method"""
        "Put a specific date to test"
        my_date = datetime.datetime(year=2016, month=8, day=16)
        with patch.object(self.obj,'today', return_value=my_date):
            response = self.obj.date() 
            self.assertEqual(response, '16/08/2016')
    def test_weekday(self):
        """ Test weekday() method """
        # Put a specific date to test
        my_date = datetime.datetime(year=2023, month=3, day=6)
        # Patch the 'today' method with a specific return value
        with patch.object(self.obj, 'today', return_value=my_date):
            response = self.obj.weekday()
            self.assertEqual(response, 'Monday')
    def test_us_indonesia_conversion(self):
        """Test us => indonesia date format converstion"""
        #test a few dates 
        d1 = '08/12/16'
        d2 = '09/11/2015'
        d3 = '04/29/00'
        self.assertEqual(self.obj.us_to_indonesia(d1), '12/08/2016')
        self.assertEqual(self.obj.us_to_indonesia(d2), '11/09/2015')
        self.assertEqual(self.obj.us_to_indonesia(d3), '29/04/2000')

if __name__ == '__main__':
    unittest.main()
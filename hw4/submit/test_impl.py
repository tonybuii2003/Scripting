import unittest
import impl  

class TestPhysicalInfo(unittest.TestCase):
    def setUp(self):
        self.physical_info = impl.PhysicalInfo() 

    def test_valid_name(self):
        valid_names = ["John Doe", "Jane-Doe"]
        for name in valid_names:
            with self.subTest(name=name):
                self.physical_info.set_name(name)
                self.assertEqual(self.physical_info.name, name) 

    def test_invalid_name(self):
        invalid_names = ["", "123", "#$%^", "A"]
        for name in invalid_names:
            with self.subTest(name=name):
                with self.assertRaises(ValueError):
                    self.physical_info.set_name(name)

    def test_valid_gender(self):
        valid_genders = ['M', 'F']
        for gender in valid_genders:
            with self.subTest(gender=gender):
                self.physical_info.set_gender(gender)
                self.assertEqual(self.physical_info.gender, gender)

    def test_invalid_gender(self):
        invalid_genders = ['', 'Male', 'Female', 'X', '123']
        for gender in invalid_genders:
            with self.subTest(gender=gender):
                with self.assertRaises(ValueError):
                    self.physical_info.set_gender(gender)
    def test_valid_height(self):
        for height in range(17, 85): 
            with self.subTest(height=height):
                self.physical_info.set_height(height)
                self.assertEqual(self.physical_info.height, height)

    def test_invalid_height(self):
        invalid_heights = [16, 85, 100, 'eighty', -5]
        for height in invalid_heights:
            with self.subTest(height=height):
                with self.assertRaises(ValueError):
                    self.physical_info.set_height(height)
    def test_valid_temperature(self):
        valid_temperatures = [95, 98.6, 104]
        for temp in valid_temperatures:
            with self.subTest(temp=temp):
                self.physical_info.set_temperature(temp)
                self.assertEqual(self.physical_info.temperature, temp)

    def test_invalid_temperature(self):
        invalid_temperatures = [94.9, 104.1, 'fever', -1]
        for temp in invalid_temperatures:
            with self.subTest(temp=temp):
                with self.assertRaises(ValueError):
                    self.physical_info.set_temperature(temp)
    def test_valid_date(self):
        valid_dates = ['01-01-1900', '12-31-2100', '07-04-2000']
        for date in valid_dates:
            with self.subTest(date=date):
                self.physical_info.set_date(date)
                self.assertEqual(self.physical_info.date, date)

    def test_invalid_date(self):
        invalid_dates = ['01-01-1899', '13-31-2000', '02-30-2020', 'abc', '2021-01-01']
        for date in invalid_dates:
            with self.subTest(date=date):
                with self.assertRaises(ValueError):
                    self.physical_info.set_date(date)
if __name__ == '__main__':
    unittest.main()

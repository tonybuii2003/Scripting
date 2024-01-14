import re
from datetime import datetime
class PhysicalInfo:
    def __init__(self):
        self.name = None
        self.gender = None
        self.height = None
        self.temperature = None
        self.date = None

    def set_name(self, name):
        if not isinstance(name, str) or not re.match("^[a-zA-Z0-9 -]*$", name) or len(re.findall("[a-zA-Z]", name)) < 1 or len(re.findall("[a-zA-Z0-9]", name)) < 2:
            raise ValueError("Invalid name")
        self.name = name

    def set_gender(self, gender):
        if gender not in ['M', 'F']:
            raise ValueError("Invalid gender")
        self.gender = gender

    def set_height(self, height):
        if not isinstance(height, int) or not 17 <= height <= 84:
            raise ValueError("Invalid height")
        self.height = height

    def set_temperature(self, temperature):
        if not isinstance(temperature, (float, int)) or not 95 <= temperature <= 104:
            raise ValueError("Invalid temperature")
        self.temperature = temperature

    def set_date(self, date_str):
        try:
            # This will raise a ValueError if the date is invalid
            date = datetime.strptime(date_str, '%m-%d-%Y')

            # Check if the year is within the valid range
            if not 1900 <= date.year <= 2100:
                raise ValueError("Year out of valid range")

            self.date = date_str
        except ValueError:
            raise ValueError("Invalid date format or value")


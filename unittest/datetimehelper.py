"""Module datetime helper - Contains the class DateTimeHelper 
providing some helpful methods for working with date dan datetime objects"""

import datetime 

class DateTimeHelper(object):
    def today(self):
        return datetime.datetime.now()
    def date(self):
        return self.today().strftime("%d/%m/%Y")
    def weekday(self):
        return self.today().strftime("%A")
    def us_to_indonesia(self, date):
        """Convert a U.S style date i.e mm/dd/yy to indonesia style dd/mm/yyyy"""
        mm,dd,yy = date.split('/')
        yy = int(yy)
        #check if year is > 16 else add 2000 to it
        if yy <= 16:
            yy += 2000
        #create a date object from it 
        date_obj = datetime.date(year=yy, month=int(mm), day=int(dd))
        #return it in correct format 
        return date_obj.strftime("%d/%m/%Y")


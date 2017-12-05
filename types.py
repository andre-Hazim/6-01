# Created by: Andre and Raymond
# Created on: Nov 2017
# Created for: ICS3U
# This program is an example of enumerated types

from enum import Enum

# an enumerated type of days
Days = Enum('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')



days_selected = raw_input('Enter the day you like: ')
if days_selected.lower() in Days:
    print(days_selected + ' is a day you like !')
else:
    print('That is not a day')

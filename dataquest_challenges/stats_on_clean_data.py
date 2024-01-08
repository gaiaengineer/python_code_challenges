# dataset https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
# dataquest challenge https://app.dataquest.io/c/54/m/290/boolean-indexing-with-numpy/10/challenge-calculating-statistics-for-trips-on-clean-data?path=2&slug=data-scientist&version=2.4

import numpy as np
taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',')

trip_distance = taxi[:, 7] # trip distance in miles
trip_length = taxi[:, 8] / 3600 # trip length in hours
trip_mph = trip_distance / trip_length # average trip speed in mph

cleaned_taxi = taxi[trip_mph < 100]
mean_distance = taxi[:,7].mean()
mean_length = taxi[:,8].mean()
mean_total_amount = taxi[:,13].mean()
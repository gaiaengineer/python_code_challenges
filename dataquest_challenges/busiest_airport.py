# dataset https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
# dataquest challenge https://app.dataquest.io/c/54/m/290/boolean-indexing-with-numpy/9/challenge-which-is-the-busiest-airport?path=2&slug=data-scientist&version=2.4 

import numpy as np
taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',')

jfk = taxi[taxi[:,5] == 2]
jfk_count = jfk.shape[0]

laguardia = taxi[taxi[:,5] == 3]
laguardia_count = laguardia.shape[0]


newark = taxi[taxi[:,5] == 5]
newark_count = newark.shape[0]

busiest_airport = "laguardia"
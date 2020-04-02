import matplotlib.pyplot as plt
import csv
from datetime import datetime
from operator import add
import sys

countries = dict()
dates = []

# either recovered, deaths, confirmed
choice = sys.argv[1]

# Change to Recovered / Deaths / Confirmed
with open("time_series_covid19_" + choice + "_global.csv", "r") as csvfile:
    data = csv.reader(csvfile, delimiter=",")
    dates = [datetime.strptime(date, '%m/%d/%y') for date in next(data)[4:]]
    for country in data:
        # Add countries you want to visualize
        if country[1] in ["Germany", "Italy", "China", "US"]:
            numbers_in_int = [int(number) for number in country[4:]]
            if country[1] not in countries:
                countries[country[1]] = numbers_in_int
            else:
                countries[country[1]] = list(map(add, countries.get(country[1]), numbers_in_int)) 

# Adding countries to plot
for country in countries:
    plt.plot(dates, countries[country], label=country)

plt.legend(loc='best')
plt.xticks(rotation=90)
plt.grid()
plt.show()

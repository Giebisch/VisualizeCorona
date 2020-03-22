import matplotlib.pyplot as plt
import csv
from datetime import datetime

countries = []
dates = []

# Change to Recovered / Deaths / Confirmed
with open("time_series_19-covid-Confirmed.csv", "r") as csvfile:
    data = csv.reader(csvfile, delimiter=",")
    dates = [datetime.strptime(date, '%m/%d/%y') for date in next(data)[4:]]
    for country in data:
        # Add countries you want to visualize
        if country[1] in ["Germany", "Italy", "Spain"]:
            numbers_in_int = [int(number) for number in country[4:]]
            countries.append((country[1], numbers_in_int))

# Adding countries to plot
for country in countries:
    plt.plot(dates, country[1], label=country[0])

plt.legend(loc='best')
plt.show()

import matplotlib.pyplot as plt
import csv
from datetime import datetime
from operator import add
import sys
import requests

def create_plot(countries):
    plt.figure(figsize=(13,9))
    plt.subplots_adjust(bottom=0.13)

    cc = [x.lower() for x in countries]

    for i, choice in enumerate(["confirmed", "deaths"], 1):
        dates = []
        countries = dict()

        url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_" + choice + "_global.csv"
        r = requests.get(url).content.decode("utf-8")
        data = csv.reader(r.splitlines(), delimiter=',')

        dates = [datetime.strptime(date, '%m/%d/%y') for date in next(data)[4:]]
        for country in data:
            # Add countries you want to visualize
            if country[1].lower() in cc:
                numbers_in_int = [int(number) for number in country[4:]]
                if country[1] not in countries:
                    countries[country[1]] = numbers_in_int
                else:
                    countries[country[1]] = list(map(add, countries.get(country[1]), numbers_in_int))

        # Adding countries to plot
        plt.subplot(120+i)
        for country in countries:
            plt.plot(dates, countries[country], label=country)

        if i == 1:
            plt.title("Infected")
        else:
            plt.title("Deaths")
        plt.legend(loc='best')
        plt.xticks(rotation=90)
        plt.grid()

    plt.savefig("plot.png")
    return True
    # plt.show()

if __name__ == "__main__":
    create_plot(["germany", "us", "italy"])
#playing around with webscrapers

#import requests

#class Scraper():
#
#def __init__(self):
#    self.county_data_source= "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
#    self.state_data_source = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
#    self.US_data_source = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv"
#
#def get_data(self):
#    county_data = requests.get(self.county_data_source, allow_redirects=True)
#    state_data = requests.get(self.state_data_source, allow_redirects=True)
#    us_data = requests.get(self.US_data_source, allow_redirects=True)

#f = open("county_data.csv", "wb")
#f.write(county_data.content)
#f.close()

#f = open("state_data.csv", "wb")
#f.write(state_data.content)
#f.close()

#f = open("us_data.csv", "wb")
#f.write(us_data.content)
#f.close()

#if __name__ == "__main__":
#    s = Scraper()
#    s.get_data()

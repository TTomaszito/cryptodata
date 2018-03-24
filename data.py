
from bs4 import BeautifulSoup
import urllib.request
import csv
import datetime

## Function takes in raw HTML table data and reansforms it to an array that can be written as CSV .

def strip_data(soup):
    data = []
    table_body = soup.find('tbody')
    rows = table_body.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    return data

## Function writes the formated data to a CSV file named based on the ticker name.

def write_data(data,ticker):
    
    file_name = 'coindata/'+ ticker +'.csv'
   
    for day in data:
        date, open_price, high, low , close, volume , marketcap = day[0],day[1],day[2],day[3],day[4],day[5],day[6]
        with open( file_name, 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([date, open_price, high, low, close, volume, marketcap])
    print("DATA FOR " +ticker + " SUCCESFULY SAVED")

def find_data(ticker):

    todayDate = datetime.datetime.today().strftime('%Y%m%d')
    
    url = "https://coinmarketcap.com/currencies/" + ticker+ "/historical-data/?start=20161201&end=" + todayDate

    request = urllib.request.Request(url)
            
    response = urllib.request.urlopen(request)

    soup = BeautifulSoup(response, 'html.parser')

    data = strip_data(soup)

    write_data(data, ticker)
    

## Main function invoked on init.

def main():
    state = True

    while state == True:
        
        
        try:
            ticker = input("input the ticker to aquire data: ")
        except expression as identifier:
            pass
        
        try:
            find_data(ticker)
            
            
        except urllib.error.HTTPError as http:
            print(http, "NO TICKER FOUND IN THE DATABASE")
            
        except error as error:
            print(error, "SOMETHING WENT WRONG ")
    
  

main()


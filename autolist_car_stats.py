"""
Python script to read in saved json file and print is CSV format.
Copy paste results into excel and do data text-to-col conversion.

Setup: curl the autolist api to get relevant car recors.
My example below looks for suburbans.
curl -sk \
"https://www.autolist.com/api/v2/search?ads=false&include_total_price_change=true&include_time_on_market=false&include_relative_price_difference=false&driveline%5B%5D=AWD&driveline%5B%5D=4X4&latitude=30.2672&limit=300&longitude=-97.7431&make=Chevrolet&mileage=80000&model=Suburban&page=1&radius=100&trim%5B%5D=High+Country&trim%5B%5D=Premier&trim%5B%5D=RST&trim%5B%5D=Z71&year_max=2025&year_min=2021&zip=78701" \
-A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:136.0) Gecko/20100101 Firefox/136.0" > cars.json
"""
import json
data_dict_from_file = {}
with open("cars.json", "r") as f:
    data_dict_from_file = json.load(f)
cars = data_dict_from_file["records"]
for car in cars:
    id = car["id"]
    year = car["year"]
    trim = car["trim"]
    price = car["price"]
    condition = car["condition"]
    mileage = car["mileage"]
    print("{}, {}, {}, {}, {}, {}".format(id, year, trim, price, condition, mileage))
  

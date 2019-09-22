import csv
import os

f = open('videos.csv')
csv_f = csv.reader(f)

for row in csv_f:
    print("")
    print("")
    print(f"<<<<<<<<<<<<<<<<<<<<<<<<< DONLOADING ::  {row[0]} >>>>>>>>>>>>>>>>>>>>>>>>>")
    os.system(f'python vimeo-download.py --url "{row[1]}" --output "{row[0]}"')
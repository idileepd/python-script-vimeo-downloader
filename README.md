# Vimeo Downloader

Steps to download :

a. Before downloading first install the requirements by executing this command :: " pip install -r requirements.txt " or manually you can install the dependencies in the requirements.txt file


1. Get the "..master.json?base64_init=1" url of video
open video in google chrome
open developer tools in google chrome (Short-cut :: "ctrl+shift+i")
go to network tab
In case if you don't see traffic there just reload the page and hover mouse on video-player and you will see "...master.json?base64_init=1"
copy its "Request Url"



2. Download Single File 
execute the command :: " python vimeo-download.py --url 'http://...master.json?base64_init=1' --output <optional_name> "

It will download the file into "output folder"

optionally you deleted "temp" folder after file download . "temp" folder the which will be created during downloading the file.

 

3. Download Multiple Video Files
First you need to get all the urls of video and their titles and you have to create the csv file which is similar to "videos.csv" in the project
Note :: please take care that url should be in quotes in csv and also placement of titile and Url should be same as in videos.csv
Replace the videos.csv in project folder with your videos.csv 
Run this command (execute the main.py) :: " python main.py " 

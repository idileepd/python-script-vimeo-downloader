# Vimeo Downloader
<h2>Steps to download :</h2>
<p>a. Before downloading first install the requirements by executing this command :: " pip install -r requirements.txt " or manually you can install the dependencies in the requirements.txt file</p>
<p>&nbsp;</p>
<h3>1. Get the "..master.json?base64_init=1" url of video</h3>
<ul>
<li>open video in google chrome</li>
<li>open developer tools in google chrome (Short-cut :: "ctrl+shift+i")</li>
<li>go to network tab</li>
<li>In case if you don't see traffic there just reload the page and hover mouse on video-player and you will see "...master.json?base64_init=1"</li>
<li>copy its "Request Url"</li>
 <li><a href="https://ibb.co/PYGNy31"><img src="https://i.ibb.co/pPjxTG4/Capture.png" alt="Capture" border="0"></a><br/><br /></li>
</ul>
<p>&nbsp;</p>
<h3>2. Download Single File&nbsp;</h3>
<ul>
<li>
<p>execute the command :: " python vimeo-download.py --url 'http://...master.json?base64_init=1' --output &lt;optional_name&gt; "</p>
</li>
<li>
<p>It will download the file into "output folder"</p>
</li>
<li>
<p>optionally you deleted "temp" folder after file download . "temp" folder the which will be created during downloading the file.</p>
</li>
</ul>
<p>&nbsp;</p>
<h3>3. Download Multiple Video Files</h3>
<ul>
<li>First you need to get all the urls of video and their titles and you have to create the csv file which is similar to "videos.csv" in the project</li>
<li>Note :: please take care that url should be in quotes in csv and also placement of titile and Url should be same as in videos.csv</li>
<li>Replace the videos.csv in project folder with your videos.csv&nbsp;</li>
<li>Run this command (execute the main.py) :: " python main.py "&nbsp;</li>
</ul>

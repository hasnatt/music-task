

<h1 align="center">
	<img
		width="300"
		alt="Logo"
		src="https://user-images.githubusercontent.com/33188934/120667049-06e07580-c485-11eb-8497-2ca7e87dd473.png"
        >
</h1>


<h3 align="center">
	Aire Music- Aire Logic Music Tak
</h3>
<p>This application utilises various music API's and technolgies to learn about artist and reccomended songs</p>




## Tech Overview

### Features 

A client application which can: 
 - Search for artists using [MusicBrainz](https://musicbrainz.org/doc/MusicBrainz_API)
 - Find the average number of words in lyrics for a given artist using [MusicBrainz](https://musicbrainz.org/doc/MusicBrainz_API) & [Lyrics.ovh API](https://lyricsovh.docs.apiary.io/#)
 - Utilise Redis cache server to cache lyrics. This is implemented because Lyrics.ovh can be slow, therefore the client stores requests from Lyrics.ovh into a cache server so we don't need to hit Lyrics.ovh API again for a set period. 
 - Recommend songs using Machine learning and NLP. (detailed below this)

A recommendation engine which: 
- Collects lyrics for each Lyrics.ovh request made.
- Perform Natural Language Processing on lyrics to find sentiment value to the lyrics, such as removing stop words and performing general regular expression. 
- Perform [LDA topic modelling](https://towardsdatascience.com/latent-dirichlet-allocation-lda-9d1cd064ffa2) algorithm on the dataset to group songs into groups/clusters bases on word frequency
- Store the model into AWS Dynamo DB and make a serverless API to interact with the model with query parameter (artist, song, amount)

### Core technologies

| Technolgy | Usage |
|--|--|
| Python | The main language used along with various packages |
| [Flask](https://flask.palletsprojects.com/en/2.0.x/) |  Python-based web microservice used as the client application|
| AWS (Lambda, DynamoDB and S3) | Various cloud technologies utilised for speed and ease |
| [scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html) | a free software machine learning library for the Python programming language. It is used to run the LDA Model on the collected lyrics dataset |




### Techincal Architecture 
![enter image description here](https://user-images.githubusercontent.com/33188934/120669966-dc43ec00-c487-11eb-8d8d-04e33e89078e.png)

## Video demonstration 

youtube link 

## Installation and Usage

### Start local Redis server 
First of all, we need to start the cache server. We will be running Redis on localhost (port 6379).

#### MacOS and Linux:

In the terminal enter the following commands or refer to the [quick start documentation] (https://redis.io/topics/quickstart) to get started:

- `$ wget http://download.redis.io/redis-stable.tar.gz`
- `$ tar xvzf redis-stable.tar.gz`
- `$ cd redis-stable`
- `$ make`
- to start the server enter `redis-server` and the server will start on 127.0.0.1:6379. Now leave this terminal open. 

 #### Windows:
 Redis is not fully supported on Windows but we can hack our way around this. 
 - Go to the [Redis Microsoft archives](https://github.com/microsoftarchive/redis/releases/tag/win-3.2.100)
 - Download the zip file called `Redis-x64-3.2.100.zip`
 - Extract the zip file
 - open the `Redis-x64-3.2.100` folder
 - There will be a file called `redis-server.exe`. Click on this and it will open a Redis server in CMD.
 - Server is ready and leave the command prompt open. 


### Start Flask client application 

#### MacOS & Linux
Prerequsites: Python3 

I have provided two options here. either run the script file called script.py into the terminal as `python3 script.py`. This should install all the packages and started the server. If not follow the commands below: 


Open the terminal in the root direcotry of repo. In the terminal enter:
 - Install virtualenv `pip3 install virtualenv`
 - create a vritualenv `virtualenv env`
 - start the virtual env `source env/bin/activate`
 - Install all required packages
 
```
pip3 install Flask
pip3 install pandas
pip3 install requests
pip3 install nltk
pip3 install musicbrainzngs
pip3 install scikit-learn
pip3 install pyLDAvis
pip3 install redis
```
- go to webapp director `cd webapp/`
- run the flask client `python3 client.py`
- This may take 2/3 minutes to start as it needs to download the NLTK package but after this it should start instantly
- go to http://127.0.0.1:5000/ in your broswee
	

 


## Recommendation API  

To recommend recipes we ran LDA on our lyrics dataset, where a lyric is collected each time we hit the Lyrics.ovh API. we also stored the CSV dataset into an S3 bucket storage which automatically stores the model into a Dynamo DB database. We then use AWS Lambda and API Gateway to create a very simple API to access this dataset. 

### How to interact
We can send a request to the endpoint URL and provide 3 queryparamters:

    <endpoint>/test/transactions?artist=<artist>&song=<song>&amount=<amount to return>
Example endpoint (feel free to interacr)    
https://kxk44df7n2.execute-api.eu-west-2.amazonaws.com/test/transactions?artist=kid%20cudi&song=sad%20people&amount=5

Please note we can only recommend songs that have been fetched by the lyrics.ovh API, executed in the LDA model and stored in AWS. The intention is the system gathers more knowledge over time for a more accurate model. 

### Example JSON Respone

    {
	    "artist":"kid cudi",
	    "song": "sad people",
	    "queried_topic": "1",
	    "amount": 4,
	    "recommended_songs": 
		    [
				{
					"artist": "alabama shakes",
					"song": "don't wanna fight",
					"song_id": "alabama shakes+don't wanna fight",
					"topic": "1"
				},
				{
					"artist": "lorde",
					"song": "royals",
					"song_id": "lorde+royals",
					"topic": "1"
				},
				{
					"artist": "drake",
					"song": "god's plan",
					"song_id": "drake+god's plan",
					"topic": "1"
				},
				{
					"artist": "miguel",
					"song": "adorn",
					"song_id": "miguel+adorn",
					"topic": "1"
				}
			]
	}


## Todo and future work
- Hosting the 	Flask application using EC2 or Elastic Beanstalk, means there would be no installation process.
- Host Redis server in AWS Elasticache with int the same VPC as the client application
- Running the LDA automatically instead of manually. Also, automate the upload to S3.
- Better UI.
- Compare artist page with visualisations.
- **Crazy future work - Make it all serverless!!!**

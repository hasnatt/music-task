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
<p><i>This application utilises various music API's and technolgies to learn about artist and reccomended songs</p>




## Tech Overview

### Features 

A client application which can: 
 - Search for aritst using [MusicBrainz](https://musicbrainz.org/doc/MusicBrainz_API)
 - Find avergae number of words in lyrics for a given artist using [MusicBrainz](https://musicbrainz.org/doc/MusicBrainz_API) & [Lyrics.ovh API](https://lyricsovh.docs.apiary.io/#)
 - Utilise Redis cache server to cahce lyrics. This is implemented because Lyrics.ovh can be really slow, therefore the client stores requests from Lyrics.ovh into a cache server so we dont need to hit Lyrics.ovh API again for a set period of time. 
 - Reccommend songs using Machine learning and NLP. (detailed below this)

A reccommendation engine which: 
- Collects lyrics for each Lyrics.ovh request made.
- perform Natural language Processing on lyrics to find sentiment value to the lyrics, such as removing stop words and perofrming general regular expression. 
- Perform LDA topic modelling on the dataset to group songs into gorups/clusters bases on word frequncy
- Store the model into AWS Dynamo DB and make a serverless API to intereact with the model with query parameter (artist, song, amount)

### Core Technlgies
python
flask
aws lambda
dynamo db
sckit learn 


### Techincal Architecture 
![enter image description here](https://user-images.githubusercontent.com/33188934/120669966-dc43ec00-c487-11eb-8d8d-04e33e89078e.png)

## Video demonstration 

youtube link 

## Installation and Usage

### Start local redis server 


### Start Flask client application 


## Reccommendation API  
What is it

how to interact

example json 

## Todo and future work?
- host flask appliction using elsatic beanstalk or 
- host redis server, talk about same vpc stuff
- automatic LDA and data into S3, cron jobs ?? 
- better UI
- Compare artist
- More data visualisation
- **Crazy future work - Make it all serverless!!!**

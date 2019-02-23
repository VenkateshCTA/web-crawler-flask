# Project Title

A basic python web crawler

## Getting Started

A python Web Crawler which crawls the Seed URL with the depth of the crawl given by the user.
<p><strong>If Depth is 1</strong>: Crawls the seed URL and fetches the URLs related to the Seed URL</p>
<p><strong>If Depth is 2</strong>: Crawls the seed URL and fetches all the images present in the Seed URL</p>
<p><strong>If Depth is 3</strong>: Crawls the seed URL, gets all the links present in the seed URL and fetches all the images present in each of the URL it crawled</p>

### Prerequisites

```
Docker
```
```
Docker compose
```

### Installing

Git clone the code to the local machine

Build the docker image of the app using below command:

```
docker-compose build
```

And run the app by following command 

```
docker-compose up
```

And application will be started, go to the browser and hit 
```
http://0.0.0.0:5000/
```

## Deployment

Deployment will be done in Heroku

## Built With

* [Flask](http://flask.pocoo.org/docs/1.0/) - The web framework used
* [Docker](https://docs.docker.com/) - Containerization
* [HTML](https://dev.w3.org/html5/html-author/) - Used for Templates

## Author

**Venkatesh Prasad R G**

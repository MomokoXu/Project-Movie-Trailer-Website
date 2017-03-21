# Movie Trailer Website
![Image of webpage](https://github.com/MomokoXu/Project-Movie-Trailer-Website/blob/master/project/web_sample.png)
## Introduction
This mini project aims to provide server-side code to store a list of author's favorite movies with box art imagery and a movie trailer URL so that front-end web page (provided by Udacity Full Stack Nano Degree program) uses this data for visitors to review the movies and trailers.
## Dataset
Self-created data of information of author's favorite movies in different category including romance, thriller, comedy, musical, and animation.
## APIs

* `media.py` - contains Movie class to store movie information including movie title, summry of the movie, URL of movie poster, and URL of movie trailer on YouTube.
* `entertainment_center.py` - loads data to create a list of Movie objects and then uses it to create the contents of the web page. 
* `fresh_potatoes.py` - renders a web page to show author's favorite movies for visitors to review (provided by Udacity FSND).

## How to use it
* Make sure download all files in this project
* In Terminal: 
    1. Make sure you switch to the directory for this project
    2. Run `python entertainment_center.py` 

## Author
[Yingtao Xu](https://github.com/MomokoXu)
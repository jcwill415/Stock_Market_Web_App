# STOCK MARKET WEB APP
Web App for Stock Quotes &amp; Live News Stream; Building a Portfolio Using Python &amp; Django

## Purpose
* This is my first big project to develop a full stack app on my own.
* It is a web application for stock market data. Users can get real-time stock data and market news via Alpha Vantage, IEX Cloud, and Stock News APIs.
* Creation of personal stock portfolios and a live streaming news feed are the first features.
* Adding charts visualization and implementing machine learning to analyze stocks will be the second goal, when I expand this app in the near future.

## Demo
For a demo of the code and how the web app works, please see this screen recording: https://www.screencast.com/t/JoT9sT67h.

## Requirements
* Get your own Django secret key
	* Create your own Django app
	* Copy secret key
	* Paste key into this project's secret key location at settings.py or in your own environment.
* API key is required if you want to use data from IEX cloud.
	* Create free account at https://iexcloud.io/.
	* Real-time data is free, however it is limited. You can use unlimited simulated data for free.
* API key is required to receive news (from news.html) via Stock News API.
	* Start a free trial at https://stocknewsapi.com.
	* Or uncomment the url in the "views.py" file for news "https://newsapi.org," and
	* Create free account at https://newsapi.org.
* Use pipenv to install python dependencies for the backend.

## How to Run
* Run backend server with the following command:
* "python manage.py runserver"

## Technical Summary
* Django
* Django Rest Framework
* Back end language: Python (the version used here is Python 3.7.7)
* Bootstrap
* HTML/CSS
* JavaScript
* SQL

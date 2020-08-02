from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

# Browser request for home page, pass in dict
def home(request):
	import requests
	import json

	if request.method == 'POST':
		ticker = request.POST['ticker']
		# pk_61291fb58322416692fb8d084051a126
		# pass in url that calls the api
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=sk_421501c1c18c4b2f912137fced92b414")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."

		return render(request, 'home.html', {'api': api, 
			'error':"Could not access the api"})
	
	else:
	
		return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})

def about(request):
	return render(request, 'about.html', {})


def add_stock(request):
	import requests
	import json

	if request.method == 'POST':
		form = StockForm(request.POST or None)
	
		if form.is_valid():
			form.save()
			messages.success(request, ("Stock has been added to your portfolio!"))				
			return redirect('add_stock')

	else:	
		ticker = Stock.objects.all()
		# save ticker info from api output into python list ('output list')
		output = []
		# modify to pull multiple stock tickers at the same time
		for ticker_item in ticker:
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=sk_421501c1c18c4b2f912137fced92b414")
			try:
				api = json.loads(api_request.content)
				output.append(api)
			except Exception as e:
				api = "Error..."	

		return render(request, 'add_stock.html', {'ticker': ticker, 'output':  output})

def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id) # call database by primary key for id #
	item.delete()
	messages.success(request, ("Stock Has Been Deleted From Portfolio!"))
	return redirect(add_stock)
	
def news(request):
	import requests
	import json
	
	# News API
	#api_request = requests.get('http://newsapi.org/v2/everything?q=stocks&apiKey=7f080596c5bb4443bad7e4557f38c6f7')
	
	# BASIC - Stock News API
	#api_request = requests.get('https://stocknewsapi.com/api/v1/category?section=general&items=50&token=se3rms2q6gvn7xb68yj6b43q0ki9wxqwprloqngg')
	
	# PREMIUM - Stock News API
	api_request = requests.get('https://stocknewsapi.com/api/v1/category?section=alltickers&items=50&token=u3cwpz4irzqp9opf8l8wwvwpzaeowplc3uggxyxe')
	api = json.loads(api_request.content)
	return render(request, 'news.html', {'api': api}) 

#def home(request):
#	import requests
#	import json
#	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
#	api = json.loads(api_request.content)
#	return render(request, 'home.html', {'api': api})

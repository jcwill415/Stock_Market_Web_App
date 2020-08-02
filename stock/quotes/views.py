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
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "</your_api_key>")

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
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=</your_api_key>")
			try:
				api = json.loads(api_request.content)
				output.append(api)
			except Exception as e:
				api = "Error..."	

		return render(request, 'add_stock.html', {'ticker': ticker, 'output':  output})

def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id) # call database by primary key for id #
	item.delete()
	messages.success(request, ("Stock Has Been Deleted"))
	return redirect(add_stock)






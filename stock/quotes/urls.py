from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('about.html', views.about, name="about"),
	path('add_stock.html', views.add_stock, name="add_stock"),
	path('delete/<stock_id>', views.delete, name="delete"),
<<<<<<< HEAD
	path('news.html', views.news, name="news"),
	
=======
>>>>>>> bde18336793f75e64da53d69caee8eeaa48a0844
]

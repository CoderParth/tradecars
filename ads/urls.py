from django.urls import path
from . import views
from .views import CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView

urlpatterns = [
	path('', CarListView.as_view(), name='ads-home'),
	path('car/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
	path('car/<int:pk>/update', CarUpdateView.as_view(), name='car-update'),
	path('car/<int:pk>/delete', CarDeleteView.as_view(), name='car-delete'),
	path('car/new/', CarCreateView.as_view(), name='car-create'),

]

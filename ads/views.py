from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Car

# Create your views here.
# def home(request):
# 	context = {
# 		'cars': Car.objects.all()
# 	}
# 	return render(request, 'ads/home.html', context)

class CarListView(ListView):
	 model = Car
	 template_name  = 'ads/home.html'
	 context_object_name = 'cars'
	 ordering = ['-date_posted']

class CarDetailView(DetailView):
	 model = Car

class CarCreateView(LoginRequiredMixin, CreateView):
	model = Car
	fields = ['name', 'price', 'content', 'photo']

	def form_valid(self, form):
		form.instance.seller = self.request.user
		return super().form_valid(form)

class CarUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Car
	fields = ['name', 'price', 'content', 'photo']

	def form_valid(self, form):
		form.instance.seller = self.request.user
		return super().form_valid(form)

	def test_func(self):
		car = self.get_object()
		if self.request.user == car.seller:
			return True
		return False

class CarDeleteView(LoginRequiredMixin, UserPassesTestMixin,  DeleteView):
	model = Car
	success_url = '/'

	def test_func(self):
		car = self.get_object()
		if self.request.user == car.seller:
			return True
		return False

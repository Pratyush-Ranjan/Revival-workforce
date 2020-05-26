from django.urls import path

from . import views

app_name = 'workforce'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('create/', views.CreateWorker.as_view(), name='create'),
	path('jobsearch/<int:worker_id>/', views.JobSearch.as_view(), name='jobsearch'),
]
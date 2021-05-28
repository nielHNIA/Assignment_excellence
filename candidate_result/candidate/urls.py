from django.urls import path

app_name = 'candidate'

from .import views

urlpatterns = [
     path('', views.HomeView.as_view(), name='home'),
     path('new/', views.NewCandidateView.as_view(), name='add_candidate'),
     path('new_test/', views.AddTestView.as_view(), name='add_test'),
     path('tests/', views.TestView.as_view(), name='tests'),
     path('candidates/', views.CandidateView.as_view(), name='candidates'),
     path('tests/<slug:pk>/update', views.UpdateTestView.as_view(), name="update_test"),
     path('candidates/<slug:pk>/update', views.UpdateCandidateView.as_view(), name="update_candidate"),


]

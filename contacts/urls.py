from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactListView.as_view()),
    path('<str:id>', views.ContactDetailView.as_view())

]
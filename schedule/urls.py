from django.urls import path

from schedule.views.Event.EventsView import EventsView
from schedule.views.HomePageView import HomePageView
from schedule.views.Label.LabelsView import LabelsView

urlpatterns = [
    path('events', EventsView.as_view(), name='event_list'),
    path('labels', LabelsView.as_view(), name='label_list'),
    path('', HomePageView.as_view(), name='homepage'),
]


from django.urls import path
from .views import BusinessList, CampaignList

urlpatterns = [
    path('business/', BusinessList.as_view(), name='business_list'),
    path('campaign/', CampaignList.as_view(), name='campaign_list')
]
from django.urls import path
from .views import BusinessList, CampaignList , BusinessDetail, CampaignDetail

urlpatterns = [
    path('business/', BusinessList.as_view(), name='business_list'),
    path('campaign/', CampaignList.as_view(), name='campaign_list'),
    path('business/<int:pk>', BusinessDetail.as_view(),name='business_detail'),
    path('campaign/<int:pk>',CampaignDetail.as_view(),name='campaign_detail')
]
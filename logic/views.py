import statistics
from typing import Any
from requests import Response
from rest_framework.views import APIView
from logic.models import Business, Campaign
from logic.serializers import BusinessSerializer, CampaignSerializer

# Create your views here.
class BusinessList(APIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.queryset = Business.objects.all()
        self.serializer_class = BusinessSerializer

    def post(self, request, format=None):
        serializer = BusinessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def get(self, request, pk, format=None):
        business = Business.objects.get(pk=pk)
        serializer = BusinessSerializer(business)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        business = Business.objects.get(pk=pk)
        serializer = BusinessSerializer(business, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk, format=None):
        business = Business.objects.get(pk=pk)
        business.delete()
        return Response(status=statistics.HTTP_204_NO_CONTENT) 

class CampaignList(APIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
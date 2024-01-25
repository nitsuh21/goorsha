from requests import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from logic.models import Business, Campaign
from logic.serializers import BusinessSerializer, CampaignSerializer

# Create your views here.
class BusinessList(APIView):
    def get(self, request):
        businesses = Business.objects.all()
        sertalizer = BusinessSerializer(businesses,many=True)
        return Response(sertalizer.data)
    
    def post(self,request):
        serializer = BusinessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BusinessDetail(APIView):
    def get_object(self, pk):
        try:
            return Business.objects.get(pk=pk)
        except Business.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BusinessSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BusinessSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CampaignList(APIView):
     
     def get(self, request):
        campaigns = Campaign.objects.all()
        sertalizer = CampaignSerializer(campaigns,many=True)
        return Response(sertalizer.data)
     
     def post(self,request):
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CampaignDetail(APIView):
    def get_object(self, pk):
        try:
            return Campaign.objects.get(pk=pk)
        except Campaign.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = CampaignSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = CampaignSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


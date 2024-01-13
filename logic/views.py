from rest_framework.views import APIView
from logic.models import Business, Campaign
from logic.serializers import BusinessSerializer, CampaignSerializer

# Create your views here.
class BusinessList(APIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class CampaignList(APIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
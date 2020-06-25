from core.models import TouristSpot
from rest_framework.serializers import ModelSerializer

class TouristSpotSerializer(ModelSerializer):
    class Meta:
        model = TouristSpot
        fields = ('id', 'name', 'description', 'photo')
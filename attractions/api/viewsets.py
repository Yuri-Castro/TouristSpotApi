from rest_framework import viewsets
from attractions.models import Attraction
from attractions.api.serializers import AttractionSerializer

class AttractionViewSet(viewsets.ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
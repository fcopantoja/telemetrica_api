from rest_framework import viewsets

from restaurantes.models import Restaurante
from restaurantes.serializers import RestauranteSerializer


class RestauranteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
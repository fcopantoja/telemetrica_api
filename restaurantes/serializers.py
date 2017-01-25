from django.contrib.auth.models import User, Group
from rest_framework import serializers

from restaurantes.models import Restaurante


class RestauranteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurante
        fields = ('id', 'rating', 'name', 'site', 'email', 'phone', 'street', 'city', 'state', 'lat', 'lng')

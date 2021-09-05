from rest_framework import serializers

from .models import CurveCoffee


class CurveCoffeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'drink', 'description', 'customer', 'created_at')
        model = CurveCoffee
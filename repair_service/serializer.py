from rest_framework import serializers
from .models import OrderModel, UstaModel


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'
    def create(self, validated_data):
        validated_data['foydalanuvchi'] = self.context['request'].user
        return super().create(validated_data)


class UstaSerializers(serializers.ModelSerializer):
    class Meta:
        model = UstaModel
        fields = '__all__'
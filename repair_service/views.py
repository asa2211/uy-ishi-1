from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import UstaModel, OrderModel
from .serializer import OrderSerializers, UstaSerializers
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class OrderAllView(generics.ListAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializers
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return OrderModel.objects.filter(foydalanuvchi=user)


class UstaAllView(generics.ListAPIView):
    queryset = UstaModel.objects.all()
    serializer_class = UstaSerializers


class CreateOrderView(generics.CreateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializers
    permission_classes = [IsAuthenticated]


class CreateUstaView(generics.CreateAPIView):
    queryset = UstaModel.objects.all()
    serializer_class = UstaSerializers


class UpdateOrderView(generics.UpdateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializers


class DeleteOrderView(generics.DestroyAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializers


class UpdateUstaView(generics.UpdateAPIView):
    queryset = UstaModel.objects.all()
    serializer_class = UstaSerializers


class DeleteUstaView(generics.DestroyAPIView):
    queryset = UstaModel.objects.all()
    serializer_class = UstaSerializers


class SearchByUstaView(APIView):
    def get(self, *args, **kwargs):
        usta_id = kwargs['usta_id']
        name = get_object_or_404(UstaModel, id=usta_id)
        orders = OrderModel.objects.filter(usta_id=name.id)
        serializer = OrderSerializers(orders, many=True)
        return Response(serializer.data)

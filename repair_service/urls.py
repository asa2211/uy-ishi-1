from django.urls import path
from .views import SearchByUstaView, DeleteUstaView, UpdateUstaView, DeleteOrderView, UpdateOrderView, CreateUstaView, \
    CreateOrderView, OrderAllView, UstaAllView

urlpatterns = [
    path('all/order/', OrderAllView.as_view()),
    path('all/usta/', UstaAllView.as_view()),
    path('create/order/', CreateOrderView.as_view()),
    path('create/usta/', CreateUstaView.as_view()),
    path('delete/order/<int:pk>', DeleteOrderView.as_view()),
    path('delete/usta/<int:pk>', DeleteUstaView.as_view()),
    path('update/order/<int:pk>', UpdateOrderView.as_view()),
    path('update/usta/<int:pk>', UpdateUstaView.as_view()),
    path('searchbyusta/<int:usta_id>', SearchByUstaView.as_view()),
]

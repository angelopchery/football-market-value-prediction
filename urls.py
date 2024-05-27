from django.contrib import admin
from django.urls import path
from predictor.views import predict_market_value

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', predict_market_value, name='predict_market_value'),
]
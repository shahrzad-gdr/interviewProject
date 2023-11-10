from django.urls import path

from account.views import RateCreateAPIView

urlpatterns = [
    path('add-rank/', RateCreateAPIView.as_view(), name='add_rank'),

]

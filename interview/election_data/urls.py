from django.urls import path
from .views import (
    PollingUnitsList,
    PollingUnitDetailView,
    LGAResultView,
    )

app_name = 'election_data'

urlpatterns = [
    path('polling-units/', PollingUnitsList.as_view(), name='polling-units'),
    path('polling_unit/<int:pk>/', PollingUnitDetailView.as_view(), name='polling_unit_detail'),
    path('lga-result-total/', LGAResultView.as_view(), name='lga-result-total'),
]
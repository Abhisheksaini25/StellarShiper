from django.urls import path
from .views import RFQSubmitView, RFQSuccessView

app_name = 'rfq'

urlpatterns = [
    path('', RFQSubmitView.as_view(), name='submit'),
    path('success/', RFQSuccessView.as_view(), name='success'),
]

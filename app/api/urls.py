from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'clients', views.ClientViewSet)
router.register(r'mailings', views.MailingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('mailings/<int:mailing_id>/messages/', views.MailingMessageListView.as_view({'get': 'list'}),
         name='message-list'),
    path('statistics/total/', views.TotalStatisticsViewSet.as_view({'get': 'list'}),
         name='total-statistics'),
]

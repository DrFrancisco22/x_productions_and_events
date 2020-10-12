from django.urls import path, include
from rest_framework import routers

from .views import EventsViewset, VisitorsViewset, GetVisitors

router = routers.SimpleRouter()
router.register('events', EventsViewset)
router.register('visitors', VisitorsViewset)
router.register('get_visitors', GetVisitors, basename ="get_visitors")


urlpatterns = [
    path('', include(router.urls))
]

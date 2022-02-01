from django.urls import path,include
from .views import CreateFishView, ListFishView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register(r'create',CreateFishView)
router.register(r'list',CreateFishView)

urlpatterns = router.urls

urlpatterns = [ 
    path('', include(router.urls)),
    path('lists/', ListFishView.as_view(), name="lists"),
]

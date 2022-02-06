from django.urls import path,include
from .views import CreateFishView, ListFishView
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from . import views

router=DefaultRouter()

router.register(r'create',CreateFishView)

urlpatterns = router.urls

urlpatterns = [ 
    path('', include(router.urls)),

    path('lists/', ListFishView.as_view(), name="lists"),
    path('image/', views.my_view, name='image'),

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )
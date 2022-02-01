from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import FishDetail
from .serializers import FishSerializer
from rest_framework import generics
from rest_framework import status, viewsets
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

class CreateFishView(viewsets.ModelViewSet):
    queryset = FishDetail.objects.all()
    serializer_class = FishSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)

class ListFishView(generics.ListAPIView):
    model = FishDetail
    serializer_class = FishSerializer
    queryset = FishDetail.objects.all()
    
# listings/views.py
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Listing, Booking, Review
from .serializers import ListingSerializer, BookingSerializer, ReviewSerializer


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["location", "is_active"]
    search_fields = ["title", "description", "location"]
    ordering_fields = ["price_per_night", "created_at"]
    ordering = ["-created_at"]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.select_related("listing", "user").all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["listing", "user", "status"]
    ordering_fields = ["created_at", "check_in"]
    ordering = ["-created_at"]

    def perform_create(self, serializer):
        # auto-assign user if not provided
        serializer.save(user=self.request.user)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.select_related("listing", "user").all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

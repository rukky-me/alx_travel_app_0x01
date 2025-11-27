from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Listing
        fields = [
            'id',
            'title',
            'description',
            'location',
            'price_per_night',
            'capacity',
            'is_active',
            'created_at',
            'updated_at',
            'average_rating',
        ]
        read_only_fields = ['created_at', 'updated_at', 'average_rating']

class BookingSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Booking
        fields = [
            'id',
            'listing',
            'check_in',
            'check_out',
            'guests',
            'status',
            'total_price',
            'created_at',
        ]
        read_only_fields = ['total_price', 'created_at']

    def validate(self, attrs):
        check_in = attrs.get('check_in')
        check_out = attrs.get('check_out')
        listing = attrs.get('listing') or getattr(self.instance, 'listing', None)
        guests = attrs.get('guests')
        if check_in and check_out and check_out <= check_in:
            raise serializers.ValidationError("check_out must be after check_in.")
        if listing and guests and guests > listing.capacity:
            raise serializers.ValidationError("guests may not exceed listing capacity.")
        return attrs

    def create(self, validated_data):
        booking = Booking(**validated_data)
        booking.clean()
        booking.save()
        return booking
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "listing", "user", "rating", "comment", "created_at"]
        read_only_fields = ["id", "created_at"]
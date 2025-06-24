from rest_framework import generics
from .models import Cause, Contribute
from .serializers import CauseSerializer, ContributeSerializer
import cloudinary.uploader
from rest_framework.exceptions import ValidationError

class CauseListCreateView(generics.ListCreateAPIView):
    queryset = Cause.objects.all()
    serializer_class = CauseSerializer

class CauseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cause.objects.all()
    serializer_class = CauseSerializer


    def perform_destroy(self, instance):
        # Delete image from Cloudinary if image_url exists
        if instance.image_url:
            # Extract public_id from the URL
            public_id = f"cause_images/{instance.title}"
            try:
                cloudinary.uploader.destroy(public_id)
            except Exception as e:
                print(f"Error deleting image from Cloudinary: {e}")
                
        super().perform_destroy(instance)


class ContributeListCreateView(generics.ListCreateAPIView):
    serializer_class = ContributeSerializer

    def get_queryset(self):
        cause_id = self.kwargs.get('cause_id')
        return Contribute.objects.filter(cause_id=cause_id)

    def perform_create(self, serializer):
        cause_id = self.kwargs.get('cause_id')
        try:
            cause = Cause.objects.get(id=cause_id)            
        except Cause.DoesNotExist:
            from rest_framework import serializers
            raise serializers.ValidationError("Cause with this ID does not exist.")
        serializer.save(cause=cause)
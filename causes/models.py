from django.db import models
from cloudinary.models import CloudinaryField
import cloudinary.uploader


class Cause(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='temp/', blank=True, null=True)  # Use ImageField for manual upload
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.image:
            # Upload to Cloudinary with custom options
            upload_result = cloudinary.uploader.upload(
                self.image,
                folder="cause_images",
                public_id=self.title,
                overwrite=True,
                resource_type="image"
            )
            self.image_url = upload_result.get('secure_url')
            self.image = None  # clear the local image field

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Contribute(models.Model):
    id = models.AutoField(primary_key=True)
    cause = models.ForeignKey(Cause, related_name='contributions', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.contributor_name} contributed {self.amount} to {self.cause.title}"
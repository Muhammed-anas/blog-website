from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.timezone import now
import uuid
from user.models import Profile


# Create your models here.
class Post(models.Model):
    id = models.UUIDField(primary_key=True, unique=True,
                          editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=200, null=False)
    subtitle =models.CharField(max_length=200)
    content = CKEditor5Field('Content', config_name='extends')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=now, editable=False)
    
    def __str__(self):
        return f'{self.author.user} post'

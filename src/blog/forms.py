from django import forms
from .models import Post

class postForms(forms.ModelForm):
    
    class Meta:
        model = Post
        fields ={'title','subtitle','content','author','image',}
        
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.order_fields(['title','subtitle','content','author','image'])
        
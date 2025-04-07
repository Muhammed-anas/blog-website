from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Post


class postForms(forms.ModelForm):

    class Meta:
        model = Post
        fields ={'title','subtitle','content','image',}
        widgets = {
            "text": CKEditor5Widget(
                attrs={"class":"django_ckeditor_5"},
                config_name="comment"
            )
        }
        
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.order_fields(['title','subtitle','content','image'])
      
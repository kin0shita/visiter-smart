from django import forms
from django.forms import ModelForm
from .models import Reception0

class Reception0Form(forms.ModelForm):
    
    class Meta:
        '''
        Attributes:
            model: モデルのクラス
            fields: フォームで使用するモデルのフィールド指定
        '''
        model = Reception0
        fields = {'purpose','accompany', 'companion_last_name', 'companion_first_name', 'relationship2'}

   
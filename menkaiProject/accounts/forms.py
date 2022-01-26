# UserCreationFormクラスをインポート
from django.contrib.auth.forms import UserCreationForm
# models.pyで定義したカスタムCustomUserモデルをインポート
from .models import CustomUser

from django.core.validators import MinLengthValidator

class CustomUserCreationForm(UserCreationForm):
    '''UserCreationFormのサブクラス
    '''
    class Meta:
        '''UserCreationFormのインナークラス

        Attributes:
            model:連携するUserクラス
            fields:フォームで利用するフィールド
        '''
        # 連携するCustomUserクラスを設定
        model = CustomUser
        # フォームで利用するフィールドを設定
        # 姓、名、ユーザ名→患者名、メールアドレス、パスワード、パスワード(確認用)
        fields = ['email', 'email_2', 'last_name', 'first_name', 'birthday', 'postal_code', 'address', 'tel', 'patient_id', 'patient_name', 'relationship1', 'password1', 'password2']
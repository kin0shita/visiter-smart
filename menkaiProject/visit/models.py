from django.db import models
# accountsアプリのmodelsモジュールからCustomUserをインポート
from accounts.models import CustomUser
from django.utils import timezone
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.validators import UnicodeUsernameValidator


class Reception0(models.Model):
    '''
    # 受付番号自動生成
    reception_id = models.CharField(
        verbose_name='受付番号', 
        primary_key=True,
        max_length=10,
        editable=False,
    )
    '''

    # CustomUserモデル(のuser_id)とReceptionモデルを
    # 1対多の関係で結び付ける
    # CustomUserが親でReceptionが子の関係となる
    user = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='email',
        # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE
        )

    # 来院目的用のフィールド
    P_CHOICES = [
            ("患者様と面会", "患者様と面会"),
            ("荷物の受け渡しのみ", "荷物の受け渡しのみ"),
            ("医師と面談", "医師と面談"),
        ]
    purpose = models.CharField(
        verbose_name='来院目的', # フィールドのタイトル
        max_length=20,
        choices=P_CHOICES
        )
    
    # 同行者の有無boolean
    A_CHOICES = [(True,"はい"), (False,"いいえ")]
    accompany = models.BooleanField(
        verbose_name='同行者はいらっしゃいますか？',
        choices=A_CHOICES,
        default=True,
        )
    
     # 登録日時のフィールド
    visited_at = models.DateTimeField(
        verbose_name='登録日時', # フィールドのタイトル
        auto_now_add=True,      # 日時を自動追加
        blank=True,
        null=True
        )

    # 同行者用のモデル
    companion_last_name = models.CharField(verbose_name='同行者様の姓', max_length=100 , blank=True, null=True)
    companion_first_name = models.CharField(verbose_name='同行者様の名', max_length=100,  blank=True, null=True)

    # 続柄
    R2_CHOICES = [
        ("配偶者", "配偶者"),
        ("子", "子"),
        ("父・母", "父・母"),
        ("兄・弟・姉・妹", "兄・弟・姉・妹"),
        ("兄・弟・姉・妹の配偶者", "兄・弟・姉・妹の配偶者"),
        ("子の配偶者", "子の配偶者"),
        ("子の子", "子の子"),
        ("配偶者の兄・弟・姉・妹", "配偶者の兄・弟・姉・妹"),
        ("その他", "その他"),
    ]
    relationship2 = models.CharField(verbose_name='続柄', max_length=30, choices=R2_CHOICES, blank=True, null=True)
        
   

    class Meta:
        verbose_name ='0面会事前登録情報'
        verbose_name_plural = '0面会事前登録データベース'

    def get_id(self):
        #オブジェクトを文字列に変換して返す
        
        return self.user


class Reception1(models.Model):
    '''
    reception_id = models.OneToOneField(
        Reception0,
        # フィールドのタイトル
        verbose_name='.id',
        # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE
        )
    '''
    user = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='email',
        # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE
        )

    # 体温
    bt1 = models.DecimalField(
        verbose_name='体温',
        max_digits=3,
        decimal_places=1,
        blank=True,
        null=True,
        default=36.0,
        validators=[MinValueValidator(34.0), MaxValueValidator(43.0)]
        )

    # 同行者体温    
    bt2 = models.DecimalField(
        verbose_name='体温',
        max_digits=3,
        decimal_places=1,
        blank=True,
        null=True,
        default=36.0,
        validators=[MinValueValidator(34.0), MaxValueValidator(43.0)]
        )

   
    # 来棟時間のフィールド
    InHospital = models.DateTimeField(
        verbose_name='来棟時間', # フィールドのタイトル
        default=None,
        blank=True,
        null=True
        )

    class Meta:
        verbose_name ='1面会時登録情報'
        verbose_name_plural = '1面会時登録データベース'

    def get_id(self):
        #オブジェクトを文字列に変換して返す
        
        return self.user



class Reception3(models.Model):
    '''
    r_id = models.OneToOneField(
        Reception0,
        # フィールドのタイトル
        verbose_name='id',
        # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE
        )
    '''
    user = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='email',
        # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE
        )
    

    # 帰棟時間のフィールド
    OutHospital = models.DateTimeField(
        verbose_name='帰棟時間', # フィールドのタイトル
        default=None,
        blank=True,
        null=True
        )

    # 受付番号が有効か無効か
    active = models.BooleanField(
        verbose_name='面会番号が有効か無効か',
        default=True,
    )

    # 帰棟時間が入ると無効になる
    def save(self, *args, **kwargs):
        if self.OutHospital is None:
            self.active = True
        elif self.OutHospital is not None:
            self.active = False
        super(Reception3, self).save(*args, **kwargs)

    class Meta:
        verbose_name ='3帰院時刻情報'
        verbose_name_plural = '3帰院時刻データベース'
    
    def get_id(self):
        #オブジェクトを文字列に変換して返す
        
        return self.user

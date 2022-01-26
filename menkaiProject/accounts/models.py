from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
# min_length
from django.core.validators import MinLengthValidator

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(_('メールアドレス'), unique=True) # primarykey
    email_2 = models.CharField(_('メールアドレス（確認用）'), max_length=254, default='') #確認はできていない
    
    last_name = models.CharField(_('面会者本人の姓'), max_length=100)
    first_name = models.CharField(_('面会者本人の名'), max_length=100)

    birthday = models.DateField(
        _('生年月日'),
        blank=True,
        null=True,
        help_text=_('(入力例)2000年1月1日生まれの場合：2000-01-01'),
    )

    # 電話番号
    tel = models.CharField(verbose_name='電話番号（ハイフンなし）', max_length=11, validators=[MinLengthValidator(11)], default='')
    postal_code = models.CharField(_('郵便番号（ハイフンなし）'), max_length=7, validators=[MinLengthValidator(7)], default='')
    # prefecture = models.CharField(_('都道府県'), max_length=5, blank=True, null=True)
    address = models.CharField(_('住所'), max_length=100, default='')
    # building = models.CharField(_('建物名'), max_length=30, blank=True, null=True)
    
    # 患者様情報用のフィールド
    patient_id = models.CharField(
        verbose_name='患者ID',
        # 変更箇所max_length,MinLengthValidator(#)
        max_length=5,
        validators=[MinLengthValidator(5)],
    )
    patient_name = models.CharField(verbose_name='患者様の名前', max_length=100, default='')
    # 続柄
    R_CHOICES = [
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
    relationship1 = models.CharField(verbose_name='続柄', max_length=30, choices=R_CHOICES, default='')

    is_staff = models.BooleanField(
        _('管理者'),
        default=False,
        help_text=_('管理サイトにログインできるかどうか'),
    )
    is_active = models.BooleanField(
        _('ログイン済'),
        default=True,
        help_text=_(
            '無効フラグ'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    # 使えそうだけど未使用メソッド
    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
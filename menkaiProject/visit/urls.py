from django.urls import path
from . import views

# URLパターンを逆引きできるように名前を付ける
app_name = 'visit'

# URLパターンを登録するための変数

urlpatterns = [
    # visitアプリへのアクセスはviewsモジュールのIndexViewにリダイレクトする
    path('', views.IndexView.as_view(), name='index'),
    
    # visitアプリへのアクセスはviewsモジュールのCreateVisitViewにリダイレクトする
    path('regist_visit/', views.CreateVisitView.as_view(), name='regist_visit'), 

    # 登録完了ページへのアクセスはviewsモジュールのRegistSuccessViewを実行
    path('regist_visit_done/', views.RegistSuccessView.as_view(), name='regist_visit_done'),

    # 詳細ページ
    # visit_detail/<Visit registテーブルのid値>にマッチング
    # <int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される
    path('visit_detail/<int:pk>',
        views.DetailView.as_view(),
        name = 'visit_detail'
    ),
   
    # マイページ
    # mypage/へのアクセスはMypageViewを実行
    path('mypage/', views.MypageView.as_view(), name='mypage'),

    # 登録情報の削除
    # visit/<Visit registテーブルのid値>/delete/にマッチング
    # <int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される
    # pkはprimary_keyのこと
    path('visit/<int:pk>/delete/',
         views.Reception0DeleteView.as_view(),
         name='visit_delete'
    ),
]
from django.shortcuts import render
# django.views.genericからTemplateView、ListViewをインポート
from django.views.generic import TemplateView, ListView
# django.views.genericからCreateViewをインポート
from django.views.generic import CreateView
# django.urlsからreverse_lazyをインポート
from django.urls import reverse_lazy
# formsモジュールからReceptionFormをインポート
from .forms import Reception0Form
# method_decoratorをインポート
from django.utils.decorators import method_decorator
# login_requiredをインポート
from django.contrib.auth.decorators import login_required
# modelsモジュールからモデルReceptionをインポート
from .models import Reception0, Reception1
# django.views.genericからDetailViewをインポート
from django.views.generic import DetailView
# django.views.genericからDeleteViewをインポート
from django.views.generic import DeleteView

class IndexView(TemplateView):
    '''トップページのビュー
    '''
    # index.htmlをレンダリングする
    template_name ='index.html'
    # モデルBlogPostのオブジェクトにorder_by()を適用して
    # 投稿日時の降順で並べ替える
    queryset = Reception0.objects.order_by('-visited_at')
   

# デコレーターにより、CreateVisitViewへのアクセスはログインユーザーに限定される
# ログイン状態でなければsettings.pyのLOGIN_URLにリダイレクトされる
@method_decorator(login_required, name='dispatch')
class CreateVisitView(CreateView):
    '''来院ページのビュー
    
    VisitingFormで定義されているモデルとフィールドと連携して
    登録データをデータベースに登録する
    
    Attributes:
      form_class: モデルとフィールドが登録されたフォームクラス
      template_name: レンダリングするテンプレート
      success_url: データベスへの登録完了後のリダイレクト先
    '''
    # forms.pyのReception1Formをフォームクラスとして登録
    form_class = Reception0Form
    # レンダリングするテンプレート
    template_name = "regist_visit.html"
    # フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('visit:regist_visit_done')

    def form_valid(self, form):
        '''CreateViewクラスのform_valid()をオーバーライド
        
        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録をここで行う
        
        parameters:
          form(django.forms.Form):
            form_classに格納されているReceptionFormオブジェクト
        Return:
          HttpResponseRedirectオブジェクト:
            スーパークラスのform_valid()の戻り値を返すことで、
            success_urlで設定されているURLにリダイレクトさせる
        '''
        # commit=FalseにしてPOSTされたデータを取得
        regist_visitdata = form.save(commit=False)
        # 登録ユーザーのidを取得してモデルのuserフィールドに格納
        regist_visitdata.user = self.request.user
        # 登録データをデータベースに登録
        regist_visitdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)
        

    
class RegistSuccessView(TemplateView):
    '''投稿完了ページのビュー
    
    Attributes:
      template_name: レンダリングするテンプレート
    '''
    # index.htmlをレンダリングする
    template_name ='regist_visit_success.html'


class DetailView(DetailView):

    # detail.htmlをレンダリングする
    template_name ='detail.html'
    # クラス変数modelにモデルを設定
    model = Reception0


class MypageView(ListView):
    '''マイページのビュー
    
    Attributes:
      template_name: レンダリングするテンプレート
      paginate_by: 1ページに表示するレコードの件数
    '''
    # mypage.htmlをレンダリングする
    template_name ='mypage.html'
    # クラス変数modelにモデルを設定
    model = Reception0

    def get_queryset(self):
      '''クエリを実行する
      
      self.kwargsの取得が必要なため、クラス変数querysetではなく、
      get_queryset（）のオーバーライドによりクエリを実行する
      
      Returns:
        クエリによって取得されたレコード
      '''
      # 現在ログインしているユーザー名はHttpRequest.userに格納されている
      # filter(userフィールド=userオブジェクト)で絞り込む
      queryset = Reception0.objects.filter(
        user=self.request.user).order_by('-visited_at')
      # クエリによって取得されたレコードを返す
      return queryset

    def get_count(self):
      
      # self.kwargsでキーワードの辞書を取得し、
      # userキーの値(ユーザーテーブルのid)を取得
      #_id = self.kwargs['user']
      # filter(フィールド名=id)で絞り込む
      active_true = Reception0.objects.filter(
        active=True).count()
      # クエリによって取得されたレコードを返す
      return active_true

   
 
    
class Reception0DeleteView(DeleteView):
    '''レコードの削除を行うビュー
    
    Attributes:
      model: モデル
      template_name: レンダリングするテンプレート
      paginate_by: 1ページに表示するレコードの件数
      success_url: 削除完了後のリダイレクト先のURL
    '''
    # 操作の対象はReception0モデル
    model = Reception0
    # mypage.htmlをレンダリングする
    template_name ='visit_delete.html'
    # 処理完了後にマイページにリダイレクト
    success_url = reverse_lazy('visit:mypage')

    def delete(self, request, *args, **kwargs):
      '''レコードの削除を行う
      
      Parameters:
        self: PhotoDeleteViewオブジェクト
        request: WSGIRequest(HttpRequest)オブジェクト
        args: 引数として渡される辞書(dict)
        kwargs: キーワード付きの辞書(dict)
                {'pk': 21}のようにレコードのidが渡される
      
      Returns:
        HttpResponseRedirect(success_url)を返して
        success_urlにリダイレクト
      '''
      # スーパークラスのdelete()を実行
      return super().delete(request, *args, **kwargs)
    
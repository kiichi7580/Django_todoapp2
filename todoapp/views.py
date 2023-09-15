from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Todo
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import SignUpForm

from django.views.generic import TemplateView
from .forms import activate_user


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ActivateView(TemplateView):
    template_name = "registration/activate.html"
    
    def get(self, request, uidb64, token, *args, **kwargs):
        # 認証トークンを検証して、
        result = activate_user(uidb64, token)
        # コンテクストのresultにTrue/Falseの結果を渡します。
        return super().get(request, result=result, **kwargs)
# Create your views here.

#ログインビュー
class CustomLoginView(LoginView):
    success_url = '/todo/'

# HTMLファイルを表示させる
def todoapp(request):
    todo_items = Todo.objects.all()
    return render(request, 'Todo.html', {'todo_items': todo_items})

# 新しいtodoタスクが入力されたら保存
#HTMLにリダイレクト
def todo_post(request):
    todo_task = Todo(content = request.POST['content'])
    todo_task.save()
    return HttpResponseRedirect('/todo/')


# 削除
def todo_delete(request, task_id):
    delete_task = Todo.objects.get(id=task_id)
    delete_task.delete()
    return HttpResponseRedirect('/todo/')
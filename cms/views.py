from django.shortcuts import render
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from cms.forms import BookForm, ImpressionForm, UserForm
from cms.models import Book, Impression, User

# List View for Impressions
from django.views.generic.list import ListView

def book_list(request, book_id=None):
    '''書籍の一覧'''
#    return HttpResponse(u'書籍の一覧')
    books = Book.objects.all().order_by('id')
    return render_to_response('cms/book_list.html',  # 使用するテンプレート
                              {'books': books},       # テンプレートに渡すデータ
                              context_instance=RequestContext(request)) 


def book_edit(request, book_id=None):
    '''書籍の編集'''
#     return HttpResponse(u'書籍の編集')
    if book_id:   # book_id が指定されている (修正時)
        book = get_object_or_404(Book, pk=book_id)
    else:         # book_id が指定されていない (追加時)
        book = Book()

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            book = form.save(commit=False)
            book.save()
            return redirect('cms:book_list')
    else:    # GET の時
        form = BookForm(instance=book)  # book インスタンスからフォームを作成

    return render_to_response('cms/book_edit.html',
                              dict(form=form, book_id=book_id),
                              context_instance=RequestContext(request))    


def book_del(request, book_id):
    '''書籍の削除'''
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('cms:book_list')



class ImpressionList(ListView):
    '''感想の一覧'''
    context_object_name='impressions'
    template_name='cms/impression_list.html'
    paginate_by = 2  # １ページは最大2件ずつでページングする

    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['book_id'])  # 親の書籍を読む
        impressions = book.impressions.all().order_by('id')   # 書籍の子供の、感想を読む
        self.object_list = impressions

        context = self.get_context_data(object_list=self.object_list, book=book)    
        return self.render_to_response(context)

def impression_edit(request, book_id, impression_id=None):
    '''感想の編集'''
    book = get_object_or_404(Book, pk=book_id)  # 親の書籍を読む
    if impression_id:   # impression_id が指定されている (修正時)
        impression = get_object_or_404(Impression, pk=impression_id)
    else:               # impression_id が指定されていない (追加時)
        impression = Impression()

    if request.method == 'POST':
        form = ImpressionForm(request.POST, instance=impression)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            impression = form.save(commit=False)
            impression.book = book  # この感想の、親の書籍をセット
            impression.save()
            return redirect('cms:impression_list', book_id=book_id)
    else:    # GET の時
        form = ImpressionForm(instance=impression)  # impression インスタンスからフォームを作成

    return render_to_response('cms/impression_edit.html',
                              dict(form=form, book_id=book_id, impression_id=impression_id),
                              context_instance=RequestContext(request))

def impression_del(request, book_id, impression_id):
    '''感想の削除'''
    impression = get_object_or_404(Impression, pk=impression_id)
    impression.delete()
    return redirect('cms:impression_list', book_id=book_id)

def user_list(request, user_id=None):
    '''書籍の一覧'''
#    return HttpResponse(u'書籍の一覧')
    users = User.objects.all().order_by('id')
    return render_to_response('cms/user_list.html',  # 使用するテンプレート
                              {'users': users},       # テンプレートに渡すデータ
                              context_instance=RequestContext(request))


def user_edit(request, user_id=None):
    '''書籍の編集'''
#     return HttpResponse(u'書籍の編集')
    if user_id:   # user_id が指定されている (修正時)
        user = get_object_or_404(User, pk=user_id)
    else:         # user_id が指定されていない (追加時)
        user = User()

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            user = form.save(commit=False)
            user.save()
            return redirect('cms:user_list')
    else:    # GET の時
        form = UserForm(instance=user)  # user インスタンスからフォームを作成

    return render_to_response('cms/user_edit.html',
                              dict(form=form, user_id=user_id),
                              context_instance=RequestContext(request))


def user_del(request, user_id):
    '''書籍の削除'''
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return redirect('cms:user_list')

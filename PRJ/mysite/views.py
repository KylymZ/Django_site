from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from .models import NEWS,Comment
from django.urls import reverse
from .forms import PostForm,UserRegForm,UserLogForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import login,logout
from django.utils.translation import gettext as _
def site(request):
    return render(request,'index3.html')


def st(request):
    return render(request,'index4.html')

def reg(request):
    return render(request,'reg.html')

def post_detail(request, pk):
    post = get_object_or_404(Comment, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def Register(request):
    if request.method == "POST":
        form=UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Успешная регистрация!")
            return redirect('/site')
        else:
            messages.error(request,"Ошибка регистрации!")
    else:
        form=UserRegForm()
    return render(request,'register.html',{'form':form})

def UserLogin(request):
    if request.method == "POST":
        form=UserLogForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('/site')
        else:
            messages.error(request,"Ошибка регистрации!")
    else:
        form=UserLogForm()
    return render(request,'login.html',{'form':form})

def UserLogout(request):
    logout(request)
    return redirect('/login')

def st2(request):
    form = PostForm()
    obj=NEWS.objects.all()
    obj2=Comment.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            send_mail("Комментарий","Новый комментарий",'j.j.k.04.2001@gmail.com',['zenisbekovk04@gmail.com'])
            return redirect('/site3')
    else:
        form = PostForm()
    return render(request, 'news.html', {'form': form,'NEWS':obj,'Comment':obj2})



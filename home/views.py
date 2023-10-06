from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as d_login, logout as d_logout

def index(request):
    return render(request, 'index.html', context={'title': '메인 페이지', 'data': '환영합니다.'})

def main(request):
    return HttpResponse('<h1>Hello</h1>')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:  # authenticate 함수에 의해 인증됨
            d_login(request, user) # 로그인 세션 생성
            return redirect('index')
        else:
            context = {
                'error': '로그인 인증 실패!'
            }
            return render(request, 'login.html', context=context)
    elif request.method == 'GET':
        return render(request, 'login.html')

def logout(request):
    d_logout(request)
    return redirect('index')

def join(request):
    return render(request, 'join.html')
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as d_login, logout as d_logout
from random import randint

def index(request):
    if request.user.is_authenticated:
        # 데이터베이스에서 dataset 조회 로직 필요
        context = {
            'dataset': []
        }
        dataset = context.get('dataset')
        for data in range(7):
            dataset.append(randint(10000, 99999))
        
        return render(request, 'index.html', context=context)
    else:
        return redirect('login')

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

def mypage(request):
    if request.method == 'GET':
        return render(request, 'setting.html')
    elif request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        user = request.user
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        context = {
            'message': '업데이트가 되었습니다. 정보를 확인하세요.'
        }

        return render(request, 'setting.html',  context=context)
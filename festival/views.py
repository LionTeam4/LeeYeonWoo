from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from .models import *
from .forms import *

#Read
def homelist(request):
    #infos가 html 내부 변수명과 일치
    infos = Info.objects.order_by('school')
    #게시물 커뮤 추가
    posts = Post.objects.order_by('-created')
    return render (request, 'read_homelist.html', {'infos': infos, 'posts':posts})
def detail(request, info_id):
    #info_detail이 html 내부 변수명과 일치
    info_festival=get_object_or_404(Info, id=info_id)
    return render(request, 'read_festival.html', {'info': info_festival})
#Create
def new(request):
    return render (request, 'create.html')

def create(request):
    new_info=Info()
    if 'image' in request.FILES:
        new_info.image=request.FILES['image']
    new_info.school=request.POST['school']
    new_info.region=request.POST['region']
    new_info.date=request.POST['date']
    new_info.fes_location=request.POST['fes_location']
    new_info.lineup=request.POST['lineup']
    new_info.save()
    #앞 내용 실행 후 다시 돌아갈 위치
    return redirect('festival:home')

def delete(request, info_id):
    delete_info = get_object_or_404(Info, id=info_id)
    delete_info.delete()
    return redirect('festival:home')

def update_page(request, info_id):
    update_info=get_object_or_404(Info, id=info_id)
    return render(request, 'update.html',{'update_info': update_info})

def update_info(request, info_id):
    update_info=get_object_or_404(Info, id=info_id)
    if 'image' in request.FILES:
        update_info.image=request.FILES['image']
    update_info.school=request.POST['school']
    update_info.region=request.POST['region']
    update_info.date=request.POST['date']
    update_info.fes_location=request.POST['fes_location']
    update_info.lineup=request.POST['lineup']
    update_info.save()
    #앞 내용 실행 후 다시 돌아갈 위치
    return redirect('festival:home')

User = get_user_model()

# 게시물 추가 (유저 로그인 설정 후 유저 추가 설정)
def add_post(request):
    # get_object_or_404는 원래 있던 객체 조회용 create에서는 안돼
    # user = get_object_or_404(Info, id=user_id)
    # 이미지도 추가할 땐 매개로 request.FILES 추가
    if request.method == 'POST':
        form = Postform(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # 나중에 로그인 붙이면
            # post.user = user
            post.save()
            return redirect('festival:read_post', post.id)
    else:
        form = Postform()

    return render(request, 'add_post.html', {'form': form})
   
def read_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'read_post.html', {'post': post})

def add_review(request, info_id):
    info = get_object_or_404(Info, id = info_id)

    if request.method == 'POST':
        form = Reviewform(request.POST)
    
        if form.is_valid():
            review = form.save(commit=False)
            review.info = info
            review.save()
            return redirect('festival:detail', info_id)
    else:
        form = Reviewform()
    return render(request, 'add_review.html', {'form': form})
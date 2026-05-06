from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import *
from .models import *
from .forms import *

#Read
def homelist(request):
    # 축제 정보 나열 + 즐겨찾기 여부 저장
    if request.method == 'POST' and request.POST.get('action') == 'toggle_favorite':
        if request.user.is_authenticated:
            info_id = request.POST.get('info_id')
            info = get_object_or_404(Info, id=info_id)

            if info.favorite_users.filter(id=request.user.id).exists():
                info.favorite_users.remove(request.user)
            else:
                info.favorite_users.add(request.user)

    infos = list(Info.objects.all())
    posts = Post.objects.all()

    if request.user.is_authenticated:
        favorite_ids = set(request.user.favorite_users.values_list('id', flat=True))
    else:
        favorite_ids = set()

    for info in infos:
        info.is_favorite = info.id in favorite_ids

    infos.sort(key=lambda x: (not x.is_favorite, x.school))
    return render (request, 'read_homelist.html', {'infos': infos, 'posts':posts})

def detail(request, info_id):
    #info_detail이 html 내부 변수명과 일치
    info=get_object_or_404(Info, id=info_id)
    # 즐겨찾기 기능 추가
    if request.method == 'POST' and request.POST.get('action') == 'toggle_favorite':
        if request.user.is_authenticated:
            if info.favorite_users.filter(id=request.user.id).exists():
                info.favorite_users.remove(request.user)
            else:
                info.favorite_users.add(request.user)

    if request.user.is_authenticated:
        info.is_favorite = info.favorite_users.filter(id=request.user.id).exists()
    else:
        info.is_favorite = False
    return render(request, 'read_festival.html', {'info': info})

#Create
def new(request):
    return render (request, 'create.html')

def create(request):
    new_info=Info()
    if 'image' in request.FILES:
        new_info.image=request.FILES['image']
    if 'poster' in request.FILES:
        new_info.poster=request.FILES['poster']
    new_info.school=request.POST['school']
    new_info.region=request.POST['region']
    new_info.start_date=request.POST['start_date']
    new_info.end_date=request.POST['start_date']
    new_info.fes_location=request.POST['fes_location']
    new_info.lineup=request.POST['lineup']
    new_info.save()
    #앞 내용 실행 후 다시 돌아갈 위치
    return redirect('festival:homelist')

def delete(request, info_id):
    delete_info = get_object_or_404(Info, id=info_id)
    delete_info.delete()
    return redirect('festival:homelist')

def update_page(request, info_id):
    update_info=get_object_or_404(Info, id=info_id)
    return render(request, 'update.html',{'update_info': update_info})

def update_info(request, info_id):
    update_info=get_object_or_404(Info, id=info_id)
    if 'image' in request.FILES:
        update_info.image=request.FILES['image']
    if 'poster' in request.FILES:
        update_info.poster=request.FILES['poster']    
    update_info.school=request.POST['school']
    update_info.region=request.POST['region']
    update_info.start_date=request.POST['start_date']
    update_info.end_date=request.POST['start_date']
    update_info.fes_location=request.POST['fes_location']
    update_info.lineup=request.POST['lineup']
    update_info.save()
    #앞 내용 실행 후 다시 돌아갈 위치
    return redirect('festival:homelist')

# 게시물 추가
@login_required
def add_post(request):
    # 이미지도 추가할 땐 매개로 request.FILES 추가
    if request.method == 'POST':
        form = Postform(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # 나중에 로그인 붙이면
            post.user = request.user
            post.save()
            return redirect('festival:read_post', post.id)
    else:
        form = Postform()

    return render(request, 'add_post.html', {'form': form})
   
def read_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'read_post.html', {'post': post})

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id = post_id)

    if request.method == 'POST':
        form = Commentform(request.POST)
    
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('festival:read_post', post_id)
    else:
        form = Commentform()
    return render(request, 'add_comment.html', {'form': form})

@login_required
def add_review(request, info_id):
    info = get_object_or_404(Info, id = info_id)

    if request.method == 'POST':
        form = Reviewform(request.POST)
    
        if form.is_valid():
            review = form.save(commit=False)
            review.info = info
            review.user = request.user
            review.save()
            return redirect('festival:detail', info_id)
    else:
        form = Reviewform()
    return render(request, 'add_review.html', {'form': form})
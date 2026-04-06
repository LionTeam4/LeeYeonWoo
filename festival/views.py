from django.shortcuts import render, get_object_or_404, redirect
from .models import Info
from .models import Review

#Read
def homelist(request):
    #infos가 html 내부 변수명과 일치
    infos = Info.objects.order_by('school')
    return render (request, 'read_homelist.html', {'infos': infos})
def detail(request, info_id):
    #info_detail이 html 내부 변수명과 일치
    info_detail=get_object_or_404(Info, id=info_id)
    return render(request, 'read_detail.html', {'info': info_detail})
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
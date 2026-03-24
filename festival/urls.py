from django.urls import path
from .views import *

app_name = 'festival'
urlpatterns = [
    #path(엔드포인트,요청 view 함수, url이름)
    # festival/ -> home
    path('', homelist, name='home'),
    # festival/info/1 -> detail
    path('info/<int:info_id>',detail, name='detail'),
    # festival/new -> create 창
    path('new/',new,name="new"),
    # festival/create -> 생성
    path('create/',create,name="create"),
    # festival/delete/1 -> delete
    path('delete/<int:info_id>', delete, name="delete"),
    # festival/update_page/1
    path('update_page/<int:info_id>', update_page, name="update_page"),
    # festival/update_info/1
    path('update_info/<int:info_id>', update_info, name="update_info"),
]   
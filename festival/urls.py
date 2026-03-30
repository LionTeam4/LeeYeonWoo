from django.urls import path
from .views import *

app_name = 'festival'
urlpatterns = [
    #path(엔드포인트,요청 view 함수, url이름)
    # festival/ -> home
    path('', homelist, name='homelist'),
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
    # fesival/post/new -> post 생성
    path('post/new',add_post,name='add_post'),
    # festival/post/1 -> post:1 read
    path('post/<int:post_id>/', read_post, name='read_post'),
    # 1/review -> info:1 에 review 생성
    path('<int:info_id>/review', add_review, name = 'add_review'),

    
]   
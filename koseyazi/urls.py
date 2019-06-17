from django.urls import path
from . import views

urlpatterns=[
    path('',views.gazete_list,name='gazete_list'),
    path('gazete/hurriyet_yazilar',views.hurriyet_yazilar,name='hurriyet_yazilar'),
    path('gazete/milliyet_yazilar',views.milliyet_yazilar,name='milliyet_yazilar'),
    path('gazete/cumhuriyet_yazilar',views.cumhuriyet_yazilar,name='cumhuriyet_yazilar'),
    path('gazete/birgun_yazilar',views.birgun_yazilar,name='birgun_yazilar'),
]
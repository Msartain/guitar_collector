from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('guitars/', views.guitars_index, name='index'),
    path('guitars/<int:guitar_id>/', views.guitars_detail, name='detail'),
    path('guitars/create/', views.GuitarCreate.as_view(), name='guitars_create'),
    path('guitars/<int:pk>/update/', views.GuitarUpdate.as_view(), name='guitars_update'),
    path('guitars/<int:pk>/delete', views.GuitarDelete.as_view(), name='guitars_delete'),
    path('guitars/<int:guitar_id>/add_restring/', views.add_restring, name='add_restring'),

    path('guitars/<int:guitar_id>/assoc_amp/<int:amp_id>/', views.assoc_amp, name='assoc_amp'),
    
    path('guitars/<int:guitar_id>/unassoc_amp/<int:amp_id>/', views.unassoc_amp, name='unassoc_amp'),
    path('guitar/<int:guitar_id>/add_photo/', views.add_photo, name='add_photo'),
    path('amps/', views.AmpList.as_view(), name='amps_index'),
    path('amps/<int:pk>/', views.AmpDetail.as_view(), name='amps_detail'),
    path('amps/create/', views.AmpCreate.as_view(), name='amps_create'),
    path('amps/<int:pk>/update/', views.AmpUpdate.as_view(), name='amps_update'),
    path('amps/<int:pk>/delete/', views.AmpDelete.as_view(), name='amps_delete'),
    path('accounts/signup', views.signup, name='signup'),
]
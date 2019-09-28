from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name='app'
urlpatterns=[
            path('others/<int:pk>/',views.others,name='others'),
            path('other_view/<int:pk>/<int:id>/',views.other_view,name='other_view'),
            path('',views.home,name='home'),
            path('login/',views.ulogin,name='ulogin'),
            path('logout/',views.ulogout,name='ulogout'),
            path('about/',views.about,name='about'),
            path('events/',views.events,name='events'),
            path('gallery/',views.gallery,name="gallery"),
            path('contact/',views.contact,name="contact"),
            path('profile/<int:pk>/',views.profile,name='profile'),
            path('exform/<int:pk>/',views.exform,name="exform"),
            path('register/<int:pk>/',views.register,name='register'),
            ]

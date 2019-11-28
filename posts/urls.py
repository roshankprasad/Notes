from django.urls import path
from posts.views import index,view
urlpatterns = [
    path('',index, name='index'),
    path('view/',view , name = 'view')
 ]
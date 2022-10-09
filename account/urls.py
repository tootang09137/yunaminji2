from django.urls import URLPattern, path
from account import views
from django.conf import settings
from django.conf.urls.static import static
import account.views
from cashbookapp.models import Cashbook
from .views import CustomUser

urlpatterns = [
    path('signup/',account.views.signup, name= 'signup'),
    path('login/',account.views.login, name= 'login'),
    path('logout/',account.views.logout, name= 'logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('mypage/<str:id>',account.views.mypage, name='mypage'),
    path('user_change/', account.views.user_change, name='user_change'),
    path('signup_yuna/', account.views.signup_yuna, name='signup_yuna'),
    path('profile/', account.views.profile, name='users-profile'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
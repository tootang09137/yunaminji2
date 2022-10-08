from django.urls import URLPattern, path
from account import views
from django.conf import settings
from django.conf.urls.static import static
import account.views

urlpatterns = [
    path('signup/',account.views.signup, name= 'signup'),
    path('login/',account.views.login, name= 'login'),
    path('logout/',account.views.logout, name= 'logout'),
    path('change_password/', views.change_password, name='change_password'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
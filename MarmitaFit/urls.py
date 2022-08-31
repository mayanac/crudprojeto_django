"""MarmitaFit URL Configuration
  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings

urlpatterns = [

    path('admin/', admin.site.urls),
    path('marmita/all/',views.list_all_marmitas),
    path('marmita/user/', views.list_user_marmitas),
    path('marmita/detail/<id>/', views.marmita_detail),
    path('login/',views.login_user),
    path('login/submit',views.submit_login),
    path('/logout/',views.logout_user),
    path('marmita/register/', views.register_marmita),
    path('marmita/register/submit', views.set_marmita),
    path('', RedirectView.as_view(url='marmita/all/'))
    
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,)
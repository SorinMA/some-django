from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

from .views import home_page, stock_page

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'home$', home_page, name="home_page"),
    url(r'login$', LoginView.as_view(template_name='sm_user/login_form.html'), name='sm_login'),
    url(r'logout$', LogoutView.as_view(), name='sm_logout'),
    url(r'stock_page$', stock_page, name="stock_page"),
]

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

from .views import home_page, stock_page, sm_register, stock_page_api, stock_page_api_recive, retrieve_strock_hist_db, stock_hist

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'home$', home_page, name="home_page"),
    url(r'login$', LoginView.as_view(template_name='sm_user/login_form.html'), name='sm_login'),
    url(r'logout$', LogoutView.as_view(), name='sm_logout'),
    url(r'stock_page$', stock_page, name="stock_page"),
    url(r'register$', sm_register, name="sm_register"),
    url(r'stock_page_api$', stock_page_api, name="stock_page_api"),
    url(r'stock_page_api_recive$', stock_page_api_recive, name="stock_page_api_recive"),
    url(r'retrieve_strock_hist_db$', retrieve_strock_hist_db, name="retrieve_strock_hist_db"),
    url(r'stock_hist$', stock_hist, name="stock_hist"),
]

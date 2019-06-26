from django.conf.urls import url
from django.contrib import admin


from .views import home_page

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'home$', home_page, name="home_page")
]

from django.contrib import admin
from django.urls import path, include
from allauth.account.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('journal.urls'))
]

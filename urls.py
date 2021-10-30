#プロジェクトディレクトリのurls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('djangofirst/', include('djangofirst.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/djangofirst/')),
]

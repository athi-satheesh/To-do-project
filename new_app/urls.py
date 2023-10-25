from django.urls import path, include

from new_app import views

urlpatterns = [
    path('', views.new, name="new"),
    path('create', views.create, name="create"),
    path('readuser', views.readuser, name="readuser"),
    path('delts/<int:id>/', views.delete, name="delt"),
    path('updt/<int:id>/', views.update, name="update")
]



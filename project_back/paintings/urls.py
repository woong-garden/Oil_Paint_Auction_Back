from django.urls import path

from paintings import views

urlpatterns = [
    path('style/', views.PaintingStyleSelectView.as_view(), name='styleselect_view'),
    path('img/', views.PaintingCreateView.as_view(), name='paintingcreate_view'),
    path('img/<int:painting_id>/', views.PaintingCreateView.as_view(), name='paintingcreate_view'),
]


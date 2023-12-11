from django.urls import path
from .views import CatListCreateView, CatChangeView, CatDeleteView, CatView

urlpatterns = [
    path('list/', CatListCreateView.as_view(), name='cat_list_create'),
    path('<int:pk>/update/', CatChangeView.as_view(), name='cat_update'),
    path('<int:pk>/delete/', CatDeleteView.as_view(), name='cat_delete'),
    path('<int:pk>/', CatView.as_view(), name='cat_detail')

]
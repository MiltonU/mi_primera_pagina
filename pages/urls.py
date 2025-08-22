from django.urls import path
from .views import (
    VinoListView, VinoDetailView, VinoCreateView, VinoUpdateView, VinoDeleteView,
    PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView
)

app_name = 'pages'

urlpatterns = [
    # 🧩 Vistas para Vino
    path('vinos/', VinoListView.as_view(), name='vino_list'),
    path('vinos/create/', VinoCreateView.as_view(), name='vino_create'),
    path('vinos/<slug:slug>/', VinoDetailView.as_view(), name='vino_detail'),
    path('vinos/update/<slug:slug>/', VinoUpdateView.as_view(), name='vino_update'),
    path('vinos/delete/<slug:slug>/', VinoDeleteView.as_view(), name='vino_delete'),
        


    # 📄 Vistas para Page
    path('', PageListView.as_view(), name='page_list'),
    path('create/', PageCreateView.as_view(), name='page_create'),
    path('<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('update/<int:pk>/', PageUpdateView.as_view(), name='page_update'),
    path('delete/<int:pk>/', PageDeleteView.as_view(), name='page_delete'),
]
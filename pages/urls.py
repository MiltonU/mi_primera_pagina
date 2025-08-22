from django.urls import path
from .views import PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView

app_name = 'pages'

urlpatterns = [
    # 🗂 Listado de páginas
    path('', PageListView.as_view(), name='page_list'),

    # 🔍 Detalle de una página
    path('<int:pk>/', PageDetailView.as_view(), name='page_detail'),

    # ➕ Crear nueva página
    path('crear/', PageCreateView.as_view(), name='page_create'),

    # ✏️ Editar página existente
    path('<int:pk>/editar/', PageUpdateView.as_view(), name='page_update'),

    # 🗑 Eliminar página
    path('<int:pk>/borrar/', PageDeleteView.as_view(), name='page_delete'),
]
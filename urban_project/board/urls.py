from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('advertisement/<int:pk>/', views.advertisement_detail, name='advertisement_detail'),
    path('add/', views.add_advertisement, name='add_advertisement'),
    path('edit/<int:pk>/', views.edit_advertisement, name='edit_advertisement'),
    # path('delete/<int:pk>/', views.delete_advertisement, name='delete_advertisement'),
    # path('like/<int:pk>/', views.post_like, name='post_like'),
]
# path('<pk>/module/',
#     views.CourseModuleUpdateView.as_view(),
#     name='course_module_update'),

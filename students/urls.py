from django.urls import path
from . import views
urlpatterns = [
    path('list',views.get_student_info),
    path('create',views.create_student),
    path('get/<int:id>',views.get_student_by_id),
    path('delete/<int:id>',views.delete_student),
]
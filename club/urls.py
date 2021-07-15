from club.views import member_create, member_delete, member_list, member_read, member_update
from django.urls import path

app_name = 'club'

urlpatterns = [
    path('members/', view=member_list, name='member_list'),
    path('members/create/', view=member_create, name='member_create'),
    path('members/<int:pk>/', view=member_read, name='member_read'),
    path('members/<int:pk>/update/', view=member_update, name='member_update'),
    path('members/<int:pk>/delete/', view=member_delete, name='member_delete'),
]

from django import path
from users.views import UserList, UserDetail


urlpatterns = [
    path("users/", UserList.as_view(), name="users"),
    path('users/<int:id>/<str:name>', UserDetail.as_view(), name="user"), 
]


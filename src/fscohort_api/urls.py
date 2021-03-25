from django.urls import path
# from .views import home_api, student_list_api, student_create_api
# from .views import home_api, student_list_create_api, student_get_update_delete_api
# from .views import home_api, StudentList, StudentGetUpdateDelete
from .views import home_api, StudentListCreate, StudentGetUpdateDelete


urlpatterns = [
    path("home-api/", home_api),
    # path("list-api/", student_list_api),
    # path("create-api/", student_create_api),
    # path("list-create-api/", student_list_create_api),
    # path("<int:id>/", student_get_update_delete_api),
    path("list-create-api/", StudentListCreate.as_view()),
    path("<int:id>/", StudentGetUpdateDelete.as_view(), name="detail"),
]
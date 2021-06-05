from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet


router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls



## Different approach using multiple urls for each view instead of routers for different viewsets 
# from django.urls import path
# from .views import PostList, PostDetail, UserList, UserDetail


# urlpatterns = [
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
#     path('', PostList.as_view()),
#     path('<int:pk>/', PostDetail.as_view()),
# ]
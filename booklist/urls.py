from django.urls import path 
from.views import UserCreate,BookListCreateView,BookRetrievUpdateDestroyView,Bookslist
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView 


urlpatterns = [
    path("",Bookslist.as_view(),name="book_list"),
    path("bookcreate/",BookListCreateView.as_view(),name="List_create_view"), 
    path('book/<int:pk>/',BookRetrievUpdateDestroyView.as_view(),name="update_delete_view"),
    path('registration/',UserCreate.as_view(),name="registration"),
    path("api/token",TokenObtainPairView.as_view(),name="token_obtain_view"),
    path("api/token/refresh/",TokenRefreshView.as_view(),name="token_refresh_view")
]

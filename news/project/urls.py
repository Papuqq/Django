from django.urls import path
from .views import (PostList, PostDetail, PostCreate, PostUpdate, PostDelete, subscriptions, IndexView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView)
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('<int:pk>/', cache_page(60 * 10)(PostDetailView.as_view()), name='product_detail'),
    # добавим кэширование на детали товара. Раз в 10 минут товар будет записываться в кэш для экономии ресурсов.

    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
    path('', IndexView.as_view()),

]

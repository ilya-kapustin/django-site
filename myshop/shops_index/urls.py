from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.AllGroup.as_view(), name='shops_index'),
    # path('shops', views.AllShopIndex.as_view(), name='shops_index'),
    path('about/', views.About.as_view(), name='about'),
    path('add_shops', views.add_shops, name='add_shops'),
    path('add_group', views.add_group, name='add_group'),
    path('contacts/', views.Contacts.as_view(), name='contacts'),
    # path('group', views.AllGroup.as_view(), name='group'),
    path('shops/<int:pk>/', views.ShopIndexDetailView.as_view(), name='shops'),
    path('group_update/<int:pk>', views.GroupUpdate.as_view(), name='group_update'),
    path('shops_update/<int:pk>', views.ShopsUpdate.as_view(), name='shops_update'),
    path('group/<int:pk>', views.GroupDetailView.as_view(), name='group'),
    path('tag/', views.tags_list, name='tag'),
    path('tag/<int:pk>', views.tags_detail, name='tag'),
    path('get_group_in_custom_format/', views.get_group_in_custom_format, name='get_group_in_custom_format'),
    path('get_shops_in_custom_format/', views.get_shops_in_custom_format, name='get_shops_in_custom_format'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

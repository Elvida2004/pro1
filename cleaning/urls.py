from django.urls import path


from cleaning.views import OrderListView, OrderCreateView, OrderUpdateView, OrderDeleteView, home_view

app_name = 'cleaning'
urlpatterns = [
    path('', home_view, name='home'),
    path('list/',OrderListView.as_view(), name='order_list'),
    path('create/',OrderCreateView.as_view(), name='order_create'),
    path('update/<int:pk>',OrderUpdateView.as_view(), name='order_update'),
    path('delete/<int:pk>',OrderDeleteView.as_view(), name='order_delete'),

]
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from cleaning.forms import OrderCreateForm, OrderUpdateForm
from cleaning.models import Order

def home_view(request):
    return render(request, 'home.html')
class OrderListView (ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderCreateView (CreateView):
    model = Order
    form_class = OrderCreateForm
    success_url = reverse_lazy('cleaning:order_list')
    login_url = reverse_lazy('users:login')  # URL страницы входа

    def form_valid(self, form):
        form.instance.user = self.request.user  # присваиваем текущего пользователя
        return super().form_valid(form)

class OrderUpdateView (UpdateView):
    model = Order
    form_class = OrderUpdateForm
    success_url = reverse_lazy('cleaning:order_list')

class OrderDeleteView (DeleteView):
    model = Order
    success_url = reverse_lazy('cleaning:order_list')
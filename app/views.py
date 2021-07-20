from app.models import Marca
from django.contrib.auth import login
from django.contrib.messages import success
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.urls import reverse_lazy
from .forms import LoginForm, MarcaForm

from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

# Create your views here.

class LoginView(FormView):
    template_name = 'views/auth/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('app:marca_list')

    @method_decorator(never_cache)
    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super(FormView,self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class MarcaList(ListView):
    model = Marca
    template_name = 'views/marca/marcas.html'
    queryset = Marca.objects.all()
    context_object_name = 'marcas'

class MarcaCreate(CreateView):
    form_class = MarcaForm
    template_name = 'views/marca/forms/createMarca.html'
    success_url = reverse_lazy('app:marca_list')

    def form_valid(self, form):
        success(self.request, 'Se registro la marca con exito')
        return super().form_valid(form)

class MarcaUpdate(UpdateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'views/marca/forms/updateMarca.html'
    success_url = reverse_lazy('app:marca_list')

    def form_valid(self, form):
        success(self.request, 'Se actualizo la Marca correctamente')
        return super().form_valid(form)

class MarcaDelete(DeleteView):
    model = Marca
    template_name = 'views/marca/forms/deleteMarca.html'
    success_url = reverse_lazy('app:marca_list')

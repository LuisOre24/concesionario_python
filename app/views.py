from app.models import Marca, Transmision, Auto, Tipo
from django.contrib.auth import login
from django.contrib.messages import success
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.urls import reverse_lazy
from .forms import LoginForm, MarcaForm, TransmisionForm, TipoForm, AutoForm

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


#VIEWS MARCA


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


# VIEWS TRANSMISION

class TransmisionList(ListView):
    model = Transmision
    template_name = 'views/transmision/transmisiones.html'
    queryset = Transmision.objects.all()
    context_object_name = 'transmisiones'

class TransmisionCreate(CreateView):
    form_class = TransmisionForm
    template_name = 'views/transmision/forms/createTransmision.html'
    success_url = reverse_lazy('app:transmision_list')

    def form_valid(self, form):
        success(self.request, 'Se registro la transmision con exito')
        return super().form_valid(form)

class TransmisionUpdate(UpdateView):
    model = Transmision
    form_class = TransmisionForm
    template_name = 'views/transmision/forms/updateTransmision.html'
    success_url = reverse_lazy('app:transmision_list')

    def form_valid(self, form):
        success(self.request, 'Se actualizo la Transmision correctamente')
        return super().form_valid(form)

class TransmisionDelete(DeleteView):
    model = Transmision
    template_name = 'views/transmision/forms/deleteTransmision.html'
    success_url = reverse_lazy('app:transmision_list')


# VIEWS TIPO

class TipoList(ListView):
    model = Tipo
    template_name = 'views/tipo/tipos.html'
    queryset = Tipo.objects.all()
    context_object_name = 'tipos'

class TipoCreate(CreateView):
    form_class = TipoForm
    template_name = 'views/tipo/forms/createTipo.html'
    success_url = reverse_lazy('app:tipo_list')

    def form_valid(self, form):
        success(self.request, 'Se registro el tipo de vehiculo con exito')
        return super().form_valid(form)

class TipoUpdate(UpdateView):
    model = Tipo
    form_class = TipoForm
    template_name = 'views/tipo/forms/updateTipo.html'
    success_url = reverse_lazy('app:tipo_list')

    def form_valid(self, form):
        success(self.request, 'Se actualizo el tipo de Auto correctamente')
        return super().form_valid(form)

class TipoDelete(DeleteView):
    model = Tipo
    template_name = 'views/tipo/forms/deleteTipo.html'
    success_url = reverse_lazy('app:tipo_list')


# VIEWS AUTO


class AutoList(ListView):
    model = Auto
    template_name = 'views/autos/autos.html'
    queryset = Auto.objects.all()
    context_object_name = 'autos'

class AutoCreate(CreateView):
    form_class = AutoForm
    template_name = 'views/autos/forms/createAuto.html'
    success_url = reverse_lazy('app:auto_list')

    def form_valid(self, form):
        success(self.request, 'Se registro el auto con exito')
        return super().form_valid(form)

class AutoUpdate(UpdateView):
    model = Auto
    form_class = AutoForm
    template_name = 'views/autos/forms/updateAuto.html'
    success_url = reverse_lazy('app:auto_list')

    def form_valid(self, form):
        success(self.request, 'Se actualizo el auto correctamente')
        return super().form_valid(form)

class AutoDelete(DeleteView):
    model = Auto
    template_name = 'views/autos/forms/deleteAuto.html'
    success_url = reverse_lazy('app:auto_list')

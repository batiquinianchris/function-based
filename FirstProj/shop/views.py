from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from shop.models import Job, Supplier, Customer, Parts, Technician, Vehicle
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = "shop/index.html"

class ProfileView(generic.TemplateView):
    template_name = "shop/profile.html"

class Technician(ModelForm):
    class Meta:
        model = Technician
        fields = ['last_name', 'first_name', 'mid_name', 'gender', 'birth_date', 'address', 'spec_area']

    def technician_list(request, template_name='shop/technician.html'):
        all_tech = Technician.objects.all()
        data = {}
        data['object_list'] = all_tech
        return render(request, template_name, {'all_tech': all_tech})

    def technician_create(request, template_name='servers/technician_form.html'):
        form = Technician(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('technician_list')
        return render(request, template_name, {'form': form})

    def technician_update(request, pk, template_name='shop/technician_form.html'):
        technician = get_object_or_404(Technician, pk=pk)
        form = Technician(request.POST or None, instance=technician)
        if form.is_valid():
            form.save()
            return redirect('server_list')
        return render(request, template_name, {'form': form})

    def technician_delete(request, pk, template_name='shop/technician.html'):
        technician = get_object_or_404(Technician, pk=pk)
        if request.method == 'POST':
            technician.delete()
            return redirect('tech_list')
        return render(request, template_name, {'object': technician})



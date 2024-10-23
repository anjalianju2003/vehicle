from django.shortcuts import render

# Create your views here.

from django.views.generic import View

from store.forms import VehicleForm

from store.models import Vehicle

class VehicleView(View):

    template_name="vehicle.html"

    form_class=VehicleForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():
            
            data=form_instance.cleaned_data

            print(data)

            Vehicle.objects.create(**data)

        return render(request,self.template_name,{"form":form_instance})

class VehicleListView(View):

    template_name="vehicle_list.html"

    def get(self,request,*args,**kwargs):
        qs=Vehicle.objects.all()
        return render(request,self.template_name,{"data":qs})


        

        


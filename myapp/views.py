from django.shortcuts import render,redirect

from django.views.generic import View

from myapp.forms import EmployeeForm

from myapp.models import Employee

# Create your views here.

class EmployeeCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=EmployeeForm()

        return render(request,"employee_add.html",{"form":form_instance})

    def post(self,request,*args,**kwargs):

        form_instance=EmployeeForm(request.POST)  

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Employee.objects.create(**data)

            return redirect('employee-list')

        else:
            return render(request,"employee_add.html",{"form":form_instance})



class EmployeeListView(View):

        def get(self,request,*args,**kwargs):            

            qs=Employee.objects.all()

            return render(request,"employee_list.html",{"employee":qs})


class EmployeeDetailsView(View):

        def get(self,request,*args,**kwargs): 

            id=kwargs.get("pk")

            qs=Employee.objects.get(id=id)

            return render(request,"employee_details.html",{"employee":qs})


class EmployeeDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Employee.objects.get(id=id).delete()
        return redirect("employee-list")


class EmployeeUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        emp_obj=Employee.objects.get(id=id)

        emp_dict={
            
            "name":emp_obj.name,
            "designation":emp_obj.designation,
            "department":emp_obj.department,
            "contact":emp_obj.contact,
            "salary":emp_obj.salary,
            "address":emp_obj.address
        }

        form_instance=EmployeeForm(initial=emp_dict)

        return render(request,'employee_edit.html',{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=EmployeeForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            id=kwargs.get("pk")

            Employee.objects.filter(id=id).update(**data)

            return redirect("employee-list")

        else:
            return render(request,'employee_edit.html',{"form":form_instance})

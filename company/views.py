from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
# Create your views here.
from .models import Branches,Departments
from .forms import newDepartmentForm,newDepartmentToBrancheForm,editBrancheForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

def AllBranches(req):
    # print("++++++++++++++++++++++++++++")
    # print(Branches.objects.filter(id = 1,name__contains="mansoura").query)
    # b = Branches.objects.filter(id = 1,name__contains="mansoura").get()
    # print(Departments.objects.filter(dept_branch = Branches.objects.filter(id = 1 ).get()).query)
    # return HttpResponse(b.name)
    MyBranches = Branches.objects.all()
    return render(req,'company/Branches.html',{'Branches':MyBranches})

def BranchesDetails(req,branch_id):
    # try:
    #     branche = Branches.objects.get(pk=branch_id)
    # except Branches.DoesNotExist :
    #     raise Http404
    # branche = get_object_or_404(Branches,pk=branch_id)
    # branche = Branches.objects.filter(pk=branch_id).first()
    branche = Branches.objects.get(pk=branch_id)
    # departments = Departments.objects.filter(dept_branch=branche)
    departments = branche.Dept_Branch.all()
    print(departments)
    return render(req,'company/BrancheDetails.html',{'branche':branche,'departments':departments})

class newDepartmentToBranche(CreateView):
    # model = 'Departments'
    form_class = newDepartmentToBrancheForm
    template_name = "company/newDepartmentsToBranhe.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        related_id = self.kwargs.get('branch_id')
        related_branch = Branches.objects.get(id=related_id)
        kwargs['related_branch'] = related_branch
        return kwargs
  
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        if  Departments.objects.filter(name=form.cleaned_data['name'], dept_branch= form.related_branch).exists():
            form.add_error('name', 'department with this name already exists in branche')
            return self.form_invalid(form)
        obj = form.save(commit=False)
        obj.dept_branch_id = self.kwargs['branch_id']
        obj.save()
        # self.object = form.save()
        return redirect('BrancheDetails',self.kwargs['branch_id'])









# @login_required(login_url='/login/',redirect_field_name="next")
def newBranche(req):
    if req.method == 'POST':
        brancheName = req.POST['brancheName']
        brancheAdress = req.POST['brancheAdress']
        branchePhone = req.POST['branchePhone']
        # newBranche = Branches(name=brancheName,address=brancheAdress,phone=branchePhone)
        # newBranche.save()
        newBranche = Branches.objects.create(name=brancheName,address=brancheAdress,phone=branchePhone)
        print(newBranche.pk)
        return redirect('BrancheDetails',branch_id=newBranche.pk)
    return render(req,'company/newBranche.html')

def editBranche(req,branch_id):
    branche = Branches.objects.get(pk=branch_id)
    form = editBrancheForm()
    form.fields['name'].initial = branche.name
    form.fields['address'].initial = branche.address
    form.fields['phone'].initial = branche.phone
    if req.method == 'POST':
        form = editBrancheForm(req.POST)
        if form.is_valid():
            branche = form.save(commit=False)
            branche.save()
            return render (req,'company/BrancheDetails.html',{'branche':branche,'departments':branche.Dept_Branch.all()})
    return render(req,'company/editBranche.html',{'form':form,'branche':branche}) 

def AllDepartments(req):
    departments = Departments.objects.all()
    return render(req,'company/Departments.html',{'Departments':departments})

def DepartmentDetails(req,Department_id):
    department = Departments.objects.filter(pk=Department_id).first()
    return render(req,'company/DepartmentDetails.html',{'Department':department})

def newDepartment(req):
    form = newDepartmentForm()
    
    if req.method == 'POST':
        form = newDepartmentForm(req.POST)
        
        if form.is_valid():
            
            if  Departments.objects.filter(name=form.cleaned_data['name'], dept_branch= Branches.objects.filter(name = form.cleaned_data['branches']).get()).exists():
                form.add_error('name', 'department with this name already exists in branche')
                return render(req,'company/newDepartments.html',{'form':form})
            
            
            department = form.save(commit=False)
            department.dept_branch = Branches.objects.filter(name = form.cleaned_data['branches']).get()
            department.save()
            # d = Departments.objects.create(name = department.name,dept_branch = department.dept_branch , description = department.description)
            return redirect('DepartmentDetails',Department_id = department.id)
    return render(req,'company/newDepartments.html',{'form':form})
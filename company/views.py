from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
# Create your views here.
from .models import Branches,Departments
from .forms import newDepartmentForm
from django.contrib.auth.decorators import login_required

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
    branche = Branches.objects.filter(pk=branch_id).first()
    return render(req,'company/BrancheDetails.html',{'branche':branche})

@login_required(login_url='/login/',redirect_field_name="next")
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
        # print(DepartmentForm.data['branches'][0])
        if form.is_valid():
            department = form.save(commit=False)
            # print( form.cleaned_data['branches'])
            department.dept_branch = Branches.objects.filter(name = form.cleaned_data['branches']).get()
            department.save()
            # d = Departments.objects.create(name = department.name,dept_branch = department.dept_branch , description = department.description)
            return redirect('DepartmentDetails',Department_id = department.id)
    return render(req,'company/newDepartments.html',{'form':form})
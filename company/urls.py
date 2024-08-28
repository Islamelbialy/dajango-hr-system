from django.urls import path,include
from . import views
urlpatterns = [
    path('branches/', views.AllBranches,name='Branches'),
    path('branche/<int:branch_id>/', views.BranchesDetails,name='BrancheDetails'),
    path('branches/new', views.newBranche,name='newBranche'),
    # path('branche/<int:branch_id>/newDepartment', views.addDepartmentToBranche,name='addDepartmentToBranche'),
    path('branche/<int:branch_id>/newDepartment', views.newDepartmentToBranche.as_view(),name='newDepartmentToBranche'),
    path('department/<int:Department_id>/', views.DepartmentDetails,name='DepartmentDetails'),
    path('departments/', views.AllDepartments,name='Departments'),
    path('departments/new', views.newDepartment,name='newDepartments'),
]

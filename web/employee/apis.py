from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields
from .models import Employee


class EmployeeResource(ModelResource):
    """
    Employee Resource
    """
    
    class Meta:

        queryset = Employee.objects.all()
        resource_name = 'employee'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            'first_name': ALL,
            'email' : ALL,
            'birthday': ['lte', 'gte', 'range'],
        }

        ordering = ['birthday', 'first_name', 'last_name']
       
        include_resource_uri = False
    
    def dehydrate(self, bundle):
        bundle.data['fullname'] = ' '.join([bundle.obj.first_name, bundle.obj.last_name]).strip()
        return bundle

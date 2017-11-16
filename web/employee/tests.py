from django.test import TestCase
from tastypie.test import ResourceTestCaseMixin
from django.shortcuts import get_object_or_404

from .models import Employee
from .apis import EmployeeResource


class EmployeeTest(TestCase):
    """Test cases for employee"""
    
    def setUp(self):
        
        self.first_name = 'Huy'
        self.last_name = 'Chau'
        self.birthday = '2000-01-01'
        self.fullname = 'Huy Chau'

        # Create employee
        self.test_emp = Employee.objects.create(
            first_name=self.first_name,
            last_name=self.last_name,
            birthday=self.birthday,
            gender='M',
            status=1
        )

        self.test_emp_2 = Employee.objects.create(
            first_name='John',
            last_name='Doe',
            birthday='1990-05-05',
            gender='M',
            status=0
        )

    def test_employee_list(self):
        self.assertEqual(len(Employee.objects.all()), 2)

    
    def test_employee_email(self):
        self.assertEqual(self.test_emp.email, '')

    def test_employee_gender(self):
        self.assertEqual(self.test_emp.get_gender_display(), 'Male')

    def test_employee_active(self):
        self.assertEqual(self.test_emp.get_status_display(), 'Active')

    def test_employee_fullname(self):
        self.assertEqual(self.test_emp.fullname(), self.fullname)

    def test_str(self):
        self.assertEqual(self.test_emp.__str__(), self.fullname)


class EmployeeResourceTest(ResourceTestCaseMixin, TestCase):
    def setUp(self):
        super(EmployeeResourceTest, self).setUp()

        # Create employee
        self.test_emp = Employee.objects.create(
            first_name='Huy',
            last_name='Chau',
            birthday='2000-05-05',
            gender='M',
            status=1
        )
    
        self.api_url = '/api/v1/employee/'
    
    def test_init(self):
        resource = EmployeeResource()

        self.assertEqual(len(resource.fields), 7)
        self.assertEqual(resource._meta.resource_name, 'employee')
        self.assertEqual(resource._meta.include_resource_uri, False)

    def test_get_list_json(self):

        resp = self.api_client.get(
            self.api_url, 
            format='json'
        )

        self.assertValidJSONResponse(resp)

        employee_list_objects = self.deserialize(resp)['objects']
        
        # Scope out the data for correctness.
        self.assertEqual(len(employee_list_objects), 1)
    
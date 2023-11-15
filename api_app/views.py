from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.

def student_details(request, pk):
    stu = Student.objects.get(id = pk)
    # print(stu) ----this line prints the student model object
    # converting complex data converted into python data
    serializer = StudentSerializer(stu)
    # print(serializer) ---this line prints the StudentSerializer object and its field
    # print(serializer.data) ----this line prints the serialized data in the dict format
    # after converting python data we have to covert that to json data 
    json_data = JSONRenderer().render(serializer.data)
    # print(json_data) -----this line prints the json data with the dict format in the double quotation
    #Now we need to send the json data as response to the client
    # we also need to define content_type because it does not set by default,
    # so then it will be know that json data is going 
    return HttpResponse(json_data, content_type = 'application/json')
    # instead of writting those two line json_data and httpresponse we can simply write as jsonResponse
    # return JsonResponse(serializer.data)

# Query Set  - All Student Data
def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many = True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')
    # return JsonResponse(serializer.data,safe=False)
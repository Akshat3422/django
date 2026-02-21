from .models import Student
from employees.models import Employee
from .serializer import StudentSerializer,Student_DATA,EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins,generics

# ek hi api se serializers use krke get and post request bna skte h 
@api_view(['GET','POST'])
def students(request):
    if request.method=='GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT','DELETE'])
def get_student_detail(request, id):

    st = Student.objects.filter(student_id=id).first()

    if not st:
        return Response({"error": "Student not found"},
                        status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Student_DATA(st)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = Student_DATA(st, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_200_OK)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        st.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





# class Employees(APIView):

#     def get(self, request, pk=None):

#         # Detail view
#         if pk:
#             employee = Employee.objects.get(id=pk)
#             if not employee:
#                 return Response(
#                     {"error": "Employee not found"},
#                     status=status.HTTP_404_NOT_FOUND
#                 )

#             serializer = EmployeeSerializer(employee)
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         # List view
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,
#                             status=status.HTTP_201_CREATED)

#         return Response(serializer.errors,
#                         status=status.HTTP_400_BAD_REQUEST)


#     def put(self, request, pk):
#         employee = Employee.objects.filter(id=pk).first()
#         if not employee:
#             return Response(
#                 {"error": "Employee not found"},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()   # 🔥 IMPORTANT
#             return Response(serializer.data,
#                             status=status.HTTP_200_OK)

#         return Response(serializer.errors,
#                         status=status.HTTP_400_BAD_REQUEST)


#     def delete(self, request, pk):
#         employee = Employee.objects.filter(id=pk).first()
#         if not employee:
#             return Response(
#                 {"error": "Employee not found"},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




class Employees(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

    def get(self,request,pk=None):
        if pk:
            return self.retrieve(request,pk)
        else:
            return self.list(request)
    
    def post(self,request):
        return self.create(request)
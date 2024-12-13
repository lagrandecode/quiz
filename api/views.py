from django.shortcuts import render
from rest_framework import status 
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .models import Question, Responses, Result
from .serializers import QuestionSerializer,ResultSerializer, ResponseSerializer,RegisterSerializer


# Create your views here.


class QuestionList(APIView):
    def get(self, request, format=None):
        student = Question.objects.all()
        serializer = QuestionSerializer(student, many = True)
        return Response(serializer.data)
    def post(self,request, format=None):
        student = Question.objects.all()
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    

class QuestionDetail(APIView):
    def get_pk(self,pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return Http404
    def get(self,pk,request,format=None):
        student= self.get_pk(pk=pk)
        serializer = QuestionSerializer(student)
        return Response(serializer.data)
    def put(self,pk,request,format=None):
        student = self.get_pk(pk=pk)
        serialializer = QuestionSerializer(student, data=request.data)
        if serialializer.is_valid():
            serialializer.save()
            return Response(serialializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serialializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,pk,request,format=None):
        student = self.get_pk(pk=pk)
        serializer = QuestionSerializer(student, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status)
    def delete(self,pk, request,format=None):
        student = self.get_pk(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
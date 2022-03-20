from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
import testtask.all_def as af
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework import serializers



class API(GenericAPIView):
    def get(self, request):
        answer = {"data" : af.request_all_orders()}
        return Response(answer)

    def post(self, request):
        data = request.GET['id']
        answer = {"data" : af.request_order(data)}
        return Response(answer)

    def delete(self, request):
        serializer = CommentSerializer(request)
        data = serializer.data
        answer = {"data" : af.request_customer(data[data.keys[0]])}
        return Response(answer)

    def patch(self, request):
        serializer = CommentSerializer(request)
        data = serializer.data
        answer = {"data" : af.request_manager(data['id'])}
        return Response(answer)

    def put(self, request):
        serializer1 = CommentSerializer(request)
        serializer2 = CommentSerializer(request)
        serializer3 = CommentSerializer(request)
        serializer4 = CommentSerializer(request)
        answer = {"data" : af.request_manager(serializer1['c_id'], serializer2['m_id'], serializer3['price'], serializer4['date'])}
        return Response({'new_data' : 'load'})


from django.shortcuts import render

from rest_framework import generics

from core import serializers


# Create your views here.
class EntryListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.EntrySerializer
    queryset = serializers.EntrySerializer.Meta.model.objects.all()


class EntryRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.EntrySerializer
    queryset = serializers.EntrySerializer.Meta.model.objects.all()


class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.CommentSerializer
    queryset = serializers.CommentSerializer.Meta.model.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"extras": self.kwargs})
        return context


class CommentRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.CommentSerializer
    queryset = serializers.CommentSerializer.Meta.model.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"extras": self.kwargs})
        return context


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from notesapp.serializers import NotesSerializer
from notesapp.models import NotesModel

class NotesCRUDView(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            qs=NotesModel.objects.filter(id=id)
            if qs:
                serializer=NotesSerializer(qs,many=True)
                return Response(serializer.data)
        qs=NotesModel.objects.all()
        serializer=NotesSerializer(qs,many=True)
        return Response(serializer.data)
    def post(self, request,format=None):
        serializer=NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Note created"},status=status.HTTP_201_CREATED)
        #return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk,format=None):
        note=NotesModel.objects.get(id=pk)
        serializer=NotesSerializer(note,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Note updated"})
        #return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        qs=NotesModel.objects.filter(id=pk).delete()
        if qs[0]==1:
            return Response({"msg":"Note deleted"})

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import BookModel
from .serializers import BookModelSerializer

from moviepy.editor import VideoFileClip

# Create your views here.

def index(request):
    context = {'msg': 'Hello, Django!'}
    
    return render(request, 'index.html', context)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_all_books(request):
    books = BookModel.objects.all()
    serializer = BookModelSerializer(books, many=True)
    
    return Response(serializer.data)


# api to add book to database
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_book(request):
    serializer = BookModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# api to get particular book to database
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_book(request):
    
    book_id = request.GET.get('book_id')
    try:
        book = BookModel.objects.get(pk=book_id)
    except BookModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BookModelSerializer(book)
    
    return Response(serializer.data)


# api to update book to database
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_book(request):
    book_id = request.data.get('book_id')
    print(book_id)
    try:
        book = BookModel.objects.get(pk=book_id)
    except BookModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BookModelSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# api to delete particular book to database
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_book(request):
    book_id = request.GET.get('book_id')
    try:
        book = BookModel.objects.get(pk=book_id)
    except BookModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    book.delete()
    
    return Response(status=status.HTTP_204_NO_CONTENT)


# api to process video using MoviePy
@api_view(['POST'])
def process_video(request):
    try:
        video_file = request.FILES['video_file']
        
        input_file_path = f'media/{video_file.name}'
        output_file_path = f'media/processed_{video_file.name}'

        with open(input_file_path, 'wb+') as destination:
            for chunk in video_file.chunks():
                destination.write(chunk)

        clip = VideoFileClip(input_file_path)
        rotated_clip = clip.rotate(90)

        rotated_clip.write_videofile(output_file_path, codec='libx264')

        return Response({'message': 'Video processed successfully', 'output_file': output_file_path})
    
    except Exception as e:
        return Response({'error': str(e)}, status=400)

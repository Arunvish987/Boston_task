# Django Video Processing API
This Django project provides a basic API endpoint to process video files using the MoviePy library and provides a minimal REST API for managing a collection of books..

## Setup
1. Clone the repository:
   git clone https://github.com/your-username/django-video-processing.git

# Install dependencies:
pip install -r requirements.txt

# Run the development server:
python manage.py runserver

# EndPoints
1. Get All Books
Endpoint: /books/
Method: GET
Description: Retrieve a list of all books.

2. Add a New Book
Endpoint: /books/add/
Method: POST
Description: Add a new book to the collection.

3. Retrieve a Book
Endpoint: /books/get/
Method: GET
Description: Retrieve details for a specific book.

4. Update a Book
Endpoint: /books/update/
Method: PUT
Description: Update details for a specific book.

5. Delete a Book
Endpoint: /books/delete/
Method: DELETE
Description: Delete a specific book from the collection.

6. Process Video Endpoint
Endpoint: /process_video/
Method: POST
Request: Upload a video file using the 'video_file' key in the form data.






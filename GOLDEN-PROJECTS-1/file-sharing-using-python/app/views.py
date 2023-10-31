from django.shortcuts import render
from .models import myfile
import uuid

# Create your views here.
def home(request):
    if request.method == 'POST':
        userfile = request.FILES.get("userfile")  # Use request.FILES to get uploaded files

        if userfile:
            id = uuid.uuid4()
            uploaded_file = myfile(id=id, file=userfile)
            uploaded_file.save()  # Save the uploaded file to the database
            link = f"http://127.0.0.1:8000/{str(id)}/"  # Construct the URL correctly
            return render(request, 'index.html', {'link': link})

    return render(request, 'index.html')

def downloadfile(request, id):
    print(id)
    get_file = myfile.objects.get(id=id)  # Correct the method name
    return render(request, "donload.html", {"get_file": get_file})

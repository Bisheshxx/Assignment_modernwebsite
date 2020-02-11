from datetime import datetime

from django.shortcuts import render, redirect

# Create your views here.
from Reviews.models import Review


def Reviews(request):
    return render(request, 'Reviews.html')


def bikereviews(request):
    review = Review.objects.all()
    if request.method == "POST":
        User_email = request.POST['User_email']
        User_review = request.POST.get('User_review')
        # user_date = datetime.now()
        review = Review(user=User_email, message=User_review)
        review.save()
        return redirect('/Reviews')
    return render(request, "Reviews.html", {'review': review})

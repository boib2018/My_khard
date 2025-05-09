from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .forms import ContactForm
from .models import CustomUser, Course, Event, GalleryItem, ContactMessage,AboutUs

 

def home(request):
    gallery_items = GalleryItem.objects.order_by('-created_at')[:3]  # or use any filter
    return render(request, 'khard/home.html', {'gallery_items': gallery_items})

def about(request):
    return render(request, 'khard/about.html')

def courses(request):
    courses = Course.objects.all()
    return render(request, 'khard/course.html', {'courses': courses})

def events(request):
    events = Event.objects.all()
    return render(request, 'khard/events.html', {'events': events})

def gallery(request):
    gallery_items = GalleryItem.objects.order_by('-created_at')
    return render(request, 'khard/gallery.html', {'gallery_items': gallery_items})


def gallery_detail(request, pk):
    item = get_object_or_404(GalleryItem, pk=pk)
    return render(request, 'khard/gallery_details.html', {'item': item})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Here you could send an email or save the data
            messages.success(request, 'Thank you for your message!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'khard/contact.html', {'form': form})




def home_view(request):
    about = AboutUs.objects.first()
    return render(request, 'home.html', {'about': about})



from django.shortcuts import render
from django.db.models import Q
from .models import Course, Event, GalleryItem

def search_view(request):
    query = request.GET.get('q', '')
    courses = Course.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    events = Event.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    gallery_items = GalleryItem.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    context = {
        'query': query,
        'courses': courses,
        'events': events,
        'gallery_items': gallery_items,
    }
    return render(request, 'khard/search_bar.html', context)

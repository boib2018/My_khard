from .models import AboutUs

def about_us_context(request):
    about = AboutUs.objects.first()
    return {'about': about}

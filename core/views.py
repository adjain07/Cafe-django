from django.shortcuts import render, redirect
from django.contrib import messages
from .models import GalleryCategory, GalleryImage, ContactMessage


def home(request):
    return render(request,'core/home.html')
def about(request):
    return render(request,'core/about.html')
def gallery(request):
    categories = GalleryCategory.objects.all()
    selected_category = request.GET.get('category')
    images = GalleryImage.objects.filter(is_active=True)

    if selected_category:
        images = images.filter(category__slug=selected_category)

    context = {'categories': categories,'images': images,'selected_category': selected_category,}
    return render(request,'core/gallery.html',context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message,
        )

        messages.success(request,'Your message has been sent successfully!')

        return redirect('contact')
    return render(request, 'core/contact.html')
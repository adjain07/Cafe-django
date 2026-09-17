from django.db import models


class GalleryCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class GalleryImage(models.Model):

    category = models.ForeignKey(GalleryCategory,on_delete=models.CASCADE,related_name='images',null=True,blank=True)

    title = models.CharField(max_length=200)

    image = models.ImageField(upload_to='gallery/')

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):

    name = models.CharField(max_length=150)

    email = models.EmailField()

    phone = models.CharField(max_length=20,blank=True)

    subject = models.CharField(max_length=200,blank=True)

    message = models.TextField()

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject or 'No Subject'}"
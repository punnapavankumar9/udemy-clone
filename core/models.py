from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

CourseCategories = (
    ('Web Development', 'Web Development'),
    ('IT software', 'IT software'),
    ('computers', 'computers'),
    ('Marketing', 'Marketing'),
    ('Personal Development', 'Personal Development'),
    ('Photograpy', 'Photograpy'),
    ('Business', 'Business'),
    ('Painting', 'Painting'),
    ('Design', 'Design')
)


class CourseCategory(models.Model):
    category = models.CharField(max_length=20, choices=CourseCategories)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Course categories'

class Course(models.Model):
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)
    course_img = models.ImageField(upload_to='course/main_images/',blank=False, null=False)
    title = models.CharField(max_length=60, blank=False, null=False)
    info = models.TextField(max_length=250, validators=[MinLengthValidator(100)])
    d_price = models.FloatField(validators=[MaxValueValidator(15000), MinValueValidator(199)])
    o_price = models.FloatField(validators=[MaxValueValidator(15000), MinValueValidator(199)])
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


    # def get_image(self, *args, **kwargs):
    #     img = Image.open(self.course_img.path)
    #     if img.width>300 or img.height>300 :
    #         new_img = (300,300)
    #         img.thumbnail(new_img)
    #     return img
    def save(self, *args, **kwargs):
        super(Course, self).save()

        img = Image.open(self.course_img.path)
        if img.width>300 or img.height>300 :
            new_img = (300,300)
            img.thumbnail(new_img)
            img.save(self.course_img.path)
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import BaseModel
from autoslug import AutoSlugField
from apps.accounts.models import User


class Subject(BaseModel):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from=title, unique=True, always_update=True)

    def __str__(self):
        return self.title
    
class Course(BaseModel):
    owner = models.ForeignKey(User,related_name='courses_owned', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='courses' ,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from=title, unique=True, always_update=True)
    overview = models.TextField()

    class Meta:
        ordering= ['-title']

    def __str__(self):
        return self.title
    
class Module(BaseModel):
    course = models.ForeignKey(Course, related_name='modules' ,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    desc = models.TextField(_('description'),blank=True)

    def __str__(self):
        return self.title



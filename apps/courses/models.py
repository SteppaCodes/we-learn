from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import BaseModel
from autoslug import AutoSlugField
from apps.accounts.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


from . fields import OrderField

class Subject(BaseModel):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title", unique=True, always_update=True)

    def __str__(self):
        return self.title
    
class Course(BaseModel):
    owner = models.ForeignKey(User,related_name='courses_owned', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='courses' ,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True, always_update=True)
    overview = models.TextField()
    

    class Meta:
        ordering= ['-title']

    def __str__(self):
        return self.title
class Module(BaseModel):
    course = models.ForeignKey(Course, related_name='modules' ,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    desc = models.TextField(_('description'),blank=True)
    order = OrderField(blank=True,for_fields=['course'])

    class Meta:
        ordering= ['order']

    def __str__(self):
        return f"{self.order}.{self.title}"

class Content(BaseModel):
    module= models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,  limit_choices_to={
        'model__in':(
            'Text',
            'image',
            'file',
            'video'
        )
    } , on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrdeField(blank=True,for_fields=['module'])

    class Meta:
        ordering= ['order']

    def __str__(self):
        return self.owner.fullname

class ItemBase(models.Model): 
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.title
    
class Text(ItemBase):
    content = models.TextField()

class Image(ItemBase):
    file = models.FileField(upload_to='images/')

class File(ItemBase):
    file = models.FileField(upload_to='files/')

class Video(ItemBase):
    url = models.URLField()
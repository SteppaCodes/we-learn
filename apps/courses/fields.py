from django.db import models
from django.core.exceptions import ObjectDoesNotExist

#This creates an ordering for objects with similar fields
class OrderField(models.PositiveIntegerField):
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields=for_fields
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        #check if the current value of the field in the model instance is None
        if getattr(model_instance, self.attname) is None:
            try:
                #retrieve objects in the model
                qs = self.model.objects.all()
                if self.for_fields:
                    # retrieves objects with similar fields and 
                    # creates a dictionary with the fields in self.for_fields
                    query = {field:getattr(model_instance, field) for field in self.for_fields}
                    print(query)
                    qs = qs.filter(**query)
                    last_item = qs.latest(self.attname)
                    value = last_item.order + 1

            except ObjectDoesNotExist:
                value= 0
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)

from django.db import models



class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.OneToOneField('Address', related_name='customer', on_delete=models.SET_NULL, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['-date_joined']
        get_latest_by = 'date_joined'

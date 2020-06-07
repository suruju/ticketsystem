from django.contrib.auth.models import User
from django.db.models.signals import post_save
#from django.dispatch import receiver
from .models import VehicleCompany
from django.contrib.auth.models import Group


# #CREATING VEHICLE COMPANY AS WELL WHEN THE USER WAS CREATED FROM DJANGO BACKEND
# @receiver(post_save, sender=User)
# def create_vehiclecompany(sender, instance, created, **kwargs):
#     if created:
#         VehicleCompany.objects.create(user=instance)
#         print('Vehicle Company created.')


# #CONNECTING DJANGO USER AND VEHICLE COMPANY IN THE ADMIN SEGMENT USING POST_SAVE
# #post_save.connect(create_vehiclecompany, sender=User)
# @receiver(post_save, sender=User)
# def update_vehiclecompany(sender, instance, created, **kwargs):
#     if created==False:
#         instance.vehiclecompany.save()
#         print('Vehicle Company Updated')
# #CONNECTING DJANGO USER AND VEHICLE COMPANY IN THE ADMIN SEGMENT USING POST_SAVE        
# #post_save.connect(update_vehiclecompany,sender=User)


def create_vehiclecompanyprofile(sender, instance, created, **kwargs):
    if created:
        group=Group.objects.get(name='Vendor')
        instance.groups.add(group)

        VehicleCompany.objects.create(
            user_auth=instance,
            authorizedperson=instance.first_name +' '+instance.last_name,
        )
        print('Vehicle Company Created.')
post_save.connect(create_vehiclecompanyprofile,sender=User)     
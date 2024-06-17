from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("Profile created!")


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()
        print("Profile updted!")
        # try:
        #     instance.profile.save()
        #     print("Profile updted!")
        # except:
        #     Profile.objects.create(user=instance)
        #     print("Profile created for existing user!")

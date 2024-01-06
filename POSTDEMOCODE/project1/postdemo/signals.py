from django.db.models.signals import *
from django.dispatch import receiver
from .models import *
from django.utils.text import slugify
import uuid

@receiver(pre_save, sender=Artist)
# @receiver(pre_save, sender=Post)
def post_pre_save_slug(sender, instance, *args, **kwargs):
    # print("instamcd uuid ",instance.uuid)
    if not instance.slug:
        instance.slug = slugify(instance.name)
        instance.save()


# @receiver(m2m_changed, sender=Song.artists.through)
# @receiver(m2m_changed, sender=Song.albums.through)
# def song_relationship_changed(sender, instance, action, reverse, model, pk_set, **kwargs):
#     if action in ["post_add", "post_remove"]:
#         related_model = Artist if model == Artist else Album
#         action_str = "added to" if action == "post_add" else "removed from"

#         for related_id in pk_set:
#             related_object = related_model.objects.get(pk=related_id)
#             if isinstance(related_object, Artist):
#                 attribute_name = "name"
#             elif isinstance(related_object, Album):
#                 attribute_name = "title"
#             else:
#                 attribute_name = "unknown"  # Handle other cases as needed

#             attribute_value = getattr(related_object, attribute_name)
#             print(f"Song '{instance.title}' {action_str} {related_model.__name__}: {attribute_value}")




















# from django.db.models.signals import m2m_changed
# from django.dispatch import receiver
# from .models import Song, Artist, Album

# @receiver(m2m_changed, sender=Song.artists.through)
# @receiver(m2m_changed, sender=Song.albums.through)
# def song_relationship_changed(sender, instance, action, reverse, model, pk_set, **kwargs):
#     if action == "post_add":
#         if model == Artist:
#             # The song was associated with one or more artists
#             for artist_id in pk_set:
#                 artist = Artist.objects.get(pk=artist_id)
#                 print(f"Song '{instance.title}' added to Artist: {artist.name}")
#         elif model == Album:
#             # The song was associated with one or more albums
#             for album_id in pk_set:
#                 album = Album.objects.get(pk=album_id)
#                 print(f"Song  added to Album: {album.title}")
#     elif action == "post_remove":
#         if model == Artist:
#             # The song was disassociated from one or more artists
#             for artist_id in pk_set:
#                 artist = Artist.objects.get(pk=artist_id)
#                 print(f"Song '{instance.title}' removed from Artist: {artist.name}")
#         elif model == Album:
#             # The song was disassociated from one or more albums
#             for album_id in pk_set:
#                 album = Album.objects.get(pk=album_id)
#                 print(f"Song removed from Album: {album.title}")



# @receiver(m2m_changed, sender=Song.artists.through)
# @receiver(m2m_changed, sender=Song.albums.through)
# def song_relationship_changed(sender, instance, action, reverse, model, pk_set, **kwargs):
#     if action in ["post_add", "post_remove"]:
#         related_model = Artist if model == Artist else Album
#         action_str = "added to" if action == "post_add" else "removed from"

#         for related_id in pk_set:
#             related_object = related_model.objects.get(pk=related_id)
#             print(f"Song '{instance.title}' {action_str} {related_model.__name__}: {related_object.name}")















from django.db import models
from django.db.models.signals import post_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import *
from django.dispatch import Signal
from django.db.models.signals import m2m_changed



# Define a signal to notify about song rating updates
# song_rating_updated = Signal()

# Your SongRating rating and unrating here...
@receiver(post_save, sender=SongRating)
def song_rated(sender, instance, created, **kwargs):
    """ Signal handler for when a new rating is added for a SongRating """
    if created:
        song_rating = instance
        song_rating.song.rating_count += 1
        song_rating.song.total_rating += song_rating.rating
        song_rating.song.save()

# Signal handler for when a rating is removed from a SongRating
@receiver(pre_delete, sender=SongRating)
def song_unrated(sender, instance, **kwargs):
    """ Signal handler for when a rating is removed from a SongRating """
    song_rating = instance
    song = song_rating.song
    if song.rating_count > 0:
        song.rating_count -= 1
        song.total_rating -= song_rating.rating
        song.save()

 # Your Song like and unlike here...
@receiver(post_save, sender=LikedSong)
def song_like_added(sender, instance, **kwargs):
    """
    Signal handler for when a new like is added for a song.
    Update the song's like count.
    """
    instance.song.like_count += 1
    instance.song.save()

@receiver(post_delete, sender=LikedSong)
def song_like_removed(sender, instance, **kwargs):
    """
    Signal handler for when a like is removed from a song.
    Update the song's like count.
    """
    instance.song.like_count -= 1
    instance.song.save()


# Your Album  save and unsave here...
@receiver(post_save, sender=SavedAlbum)
def album_saved(sender, instance, created, **kwargs):
    """ Signal handler for when a new save is added for an album """
    if created:
        album = instance.album
        album.save_count += 1
        album.save()

@receiver(pre_delete, sender=SavedAlbum)
def album_unsaved(sender, instance, **kwargs):
    """ Signal handler for when a save is removed from an album """
    album = instance.album
    if album.save_count > 0:
        album.save_count -= 1
        album.save()

# Your Album  rating and unrating here...
@receiver(post_save, sender=AlbumReview)
def album_rated(sender, instance, created, **kwargs):
    """ Signal handler for when a new rating is added for an album """
    if created:
        album = instance.album
        album.rating_count += 1
        album.total_rating += instance.rating
        album.save()

@receiver(pre_delete, sender=AlbumReview)
def album_unrated(sender, instance, **kwargs):
    """ Signal handler for when a rating is removed from an album """
    album = instance.album
    if album.rating_count > 0:
        album.rating_count -= 1
        album.total_rating -= instance.rating
        album.save()


# Signal handler for when a new FollowedArtist is created
@receiver(post_save, sender=FollowedArtist)
def artist_followed(sender, instance, created, **kwargs):
    if created:
        # Handle actions when an artist is followed, e.g., update artist's follower count
        artist = instance.artist
        artist.followers_count += 1
        artist.save()

# Signal handler for when a FollowedArtist is deleted
@receiver(pre_delete, sender=FollowedArtist)
def artist_unfollowed(sender, instance, **kwargs):
    # Handle actions when an artist is unfollowed, e.g., update artist's follower count
    artist = instance.artist
    if artist.followers_count > 0:
        artist.followers_count -= 1
        artist.save()



# playlist item

# Signal handler for when a new save is added for a Playlist
# @receiver(m2m_changed, sender=Playlist.collaborators.through)
# def playlist_collaborator_added(sender, instance, action, reverse, model, pk_set, **kwargs):
#     if action == 'post_add':
#         # Loop through the added collaborators
#         for user_id in pk_set:
#             # Get the corresponding PlaylistItem and update save count
#             playlist_item = PlaylistItem.objects.get(playlist=instance, song__owner_id=user_id)
#             playlist_item.save_count += 1
#             playlist_item.save()

# # Signal handler for when a save is removed from a Playlist
# @receiver(m2m_changed, sender=Playlist.collaborators.through)
# def playlist_collaborator_removed(sender, instance, action, reverse, model, pk_set, **kwargs):
#     if action == 'post_remove':
#         # Loop through the removed collaborators
#         for user_id in pk_set:
#             # Get the corresponding PlaylistItem and update save count
#             playlist_item = PlaylistItem.objects.get(playlist=instance, song__owner_id=user_id)
#             if playlist_item.save_count > 0:
#                 playlist_item.save_count -= 1
#                 playlist_item.save()



# Signal handler for when a new save is added for a Playlist
@receiver(m2m_changed, sender=Playlist.collaborators.through)
def playlist_collaborator_added(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == 'post_add':
        # Increment the Playlist's save count for each added collaborator
        instance.save_count += pk_set
        instance.save()

# Signal handler for when a save is removed from a Playlist
@receiver(m2m_changed, sender=Playlist.collaborators.through)
def playlist_collaborator_removed(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == 'post_remove':
        # Decrement the Playlist's save count for each removed collaborator
        instance.save_count -= pk_set
        instance.save()
            
        























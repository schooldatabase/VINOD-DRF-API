from django.contrib import admin
from .models import Song, Artist, Album


# class PostAdmin(admin.ModelAdmin):
#     list_display = ('name',)  

# admin.site.register(Post, PostAdmin)

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name',)  

admin.site.register(Artist, ArtistAdmin)

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('artists',)

admin.site.register(Album, AlbumAdmin)

class SongAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Display 'title' in the list view
    filter_horizontal = ('artists', 'albums') 

admin.site.register(Song, SongAdmin)











# from django.contrib import admin
# from .models import *

# # Register your models with the admin site here
# @admin.site.register(Artist)
# class ArtistAdmin(admin.ModelAdmin):
#     list_display = ('name',)
    
# @admin.site.register(Album)
# class AlbumAdmin(admin.ModelAdmin):
#     list_display = ('title', 'artists',)
    
# @admin.site.register(Song)
# class SongAdmin(admin.ModelAdmin):
#     list_display = ('title', 'artists', 'albums',)










# admin.site.register(SongRating)
# admin.site.register(LikedSong)
# admin.site.register(AlbumReview)
# admin.site.register(SavedAlbum)
# admin.site.register(FollowedArtist)
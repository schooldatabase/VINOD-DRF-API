from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from .signals import *

# class PostViewSet(viewsets.ModelViewSet):
#     queryset =  Post.objects.all()
#     serializer_class = PostSerializer
    
class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

        
class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    
    
    
    
    
    
    
    
    
    

# class LikedSongViewSet(viewsets.ModelViewSet):
#     queryset = LikedSong.objects.all()
#     serializer_class = LikedSongSerializer
    
#     def create(self, request, *args, **kwargs):
#         user = request.user
#         song_id = request.data.get('song')

#         try:
#             song = Song.objects.get(id=song_id)
#         except Song.DoesNotExist:
#             return Response({'message': 'Song not found'}, status=status.HTTP_404_NOT_FOUND)

#         liked_song, created = LikedSong.objects.get_or_create(user=user, song=song)

#         if not created:
#             liked_song.delete()
#             return Response({'message': 'Song unliked'}, status=status.HTTP_204_NO_CONTENT)
#         else:
#             return Response({'message': 'Song liked'}, status=status.HTTP_201_CREATED)
# class AlbumReviewViewSet(viewsets.ModelViewSet):
#     queryset = AlbumReview.objects.all()
#     serializer_class = AlbumReviewSerializer
    
# class SavedAlbumViewSet(viewsets.ModelViewSet):
#     queryset = SavedAlbum.objects.all()
#     serializer_class = SavedAlbumSerializer
    
#     def create(self, request, *args, **kwargs):
#         user = request.user
#         album_id = request.data.get('album')

#         # Check if the album is already saved by the user
#         saved_album = SavedAlbum.objects.filter(user=user, album=album_id).first()

#         if saved_album:
#             saved_album.delete()
#             return Response({'detail': 'Album is already saved by the user. so your Album is unsaved '}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             # Create a new saved album record
#             serializer = self.get_serializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save(user=user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def destroy(self, request, *args, **kwargs):
#         user = request.user
#         album_id = self.kwargs.get('pk')

#         try:
#             # Find and delete the saved album record for the user and album
#             saved_album = SavedAlbum.objects.get(user=user, album=album_id)
#             saved_album.delete()
#             return Response({'detail': 'Album unsaved successfully.'}, status=status.HTTP_204_NO_CONTENT)
#         except SavedAlbum.DoesNotExist:
#             return Response({'detail': 'Album is not saved by the user.'}, status=status.HTTP_400_BAD_REQUEST)
        
        
# class ArtistViewSet(viewsets.ModelViewSet):
#     queryset = Artist.objects.all()
#     serializer_class = ArtistSerializer

# # class FollowedArtistViewSet(viewsets.ModelViewSet):
# #     queryset = FollowedArtist.objects.all()
# #     serializer_class = FollowedArtistSerializer
    
# #     def create(self, request):
# #         user = request.user
# #         artist_id = request.data.get('artist')

# #         # Check if the user is already following the artist
# #         if FollowedArtist.objects.filter(user=user, artist_id=artist_id).exists():
# #             return Response({'detail': 'User is already following this artist.'}, status=status.HTTP_400_BAD_REQUEST)

# #         # Create a new FollowedArtist instance
# #         follow = FollowedArtist(user=user, artist_id=artist_id)
# #         follow.save()

# #         return Response({'detail': 'User is now following this artist.'}, status=status.HTTP_201_CREATED)

# #     def destroy(self, request, pk=None):
# #         user = request.user
# #         artist = get_object_or_404(FollowedArtist, artist_id=pk, user=user)

# #         # Delete the FollowedArtist instance to unfollow the artist
# #         artist.delete()

# #         return Response({'detail': 'User has unfollowed this artist.'}, status=status.HTTP_204_NO_CONTENT)
        
# # class FollowedViewSet(viewsets.ModelViewSet):
# #     queryset = Followed.objects.all()
# #     serializer_class = FollowedSerializer
   

# #     # def create(self, request, *args, **kwargs):
# #     #     user = request.user
# #     #     data = request.data
# #     #     data['user'] = user.id  # Ensure the user is the current authenticated user
# #     #     serializer = self.get_serializer(data=data)
# #     #     serializer.is_valid(raise_exception=True)
# #     #     self.perform_create(serializer)
# #     #     return Response(serializer.data, status=status.HTTP_201_CREATED)

# #     # def destroy(self, request, *args, **kwargs):
# #     #     instance = self.get_object()
# #     #     self.perform_destroy(instance)
# #     #     return Response(status=status.HTTP_204_NO_CONTENT)
    
# # class PlaylistViewSet(viewsets.ModelViewSet):
# #     queryset = Playlist.objects.all()
# #     serializer_class = PlaylistSerializer

# # class PlaylistItemViewSet(viewsets.ModelViewSet):
# #     queryset = PlaylistItem.objects.all()
# #     serializer_class = PlaylistItemSerializer
    
# #     def create(self, request, playlist_pk=True, song_pk=True):
# #         playlist = get_object_or_404(Playlist, pk=playlist_pk)
# #         song = get_object_or_404(Song, pk=song_pk)

# #         # Check if the playlist item already exists
# #         playlist_item, created = PlaylistItem.objects.get_or_create(playlist=playlist, song=song)

# #         if created:
# #             playlist_item.save()
# #             return Response({'detail': 'Song saved to the playlist.'}, status=status.HTTP_201_CREATED)
# #         else:
# #             playlist_item.delete()
# #             return Response({'detail': 'Song is already saved to the playlist.'}, status=status.HTTP_400_BAD_REQUEST)

# #     def destroy(self, request, playlist_pk=True, song_pk=True):
# #         playlist = get_object_or_404(Playlist, pk=playlist_pk)
# #         song = get_object_or_404(Song, pk=song_pk)

# #         # Check if the playlist item exists and delete it
# #         try:
# #             playlist_item = PlaylistItem.objects.get(playlist=playlist, song=song)
# #             playlist_item.delete()
# #             return Response({'detail': 'Song removed from the playlist.'}, status=status.HTTP_204_NO_CONTENT)
# #         except PlaylistItem.DoesNotExist:
# #             return Response({'detail': 'Song is not saved to the playlist.'}, status=status.HTTP_400_BAD_REQUEST)

# # class CollaboratorViewSet(viewsets.ModelViewSet):
# #     queryset = Collaborator.objects.all()
# #     serializer_class = CollaboratorSerializer

# # class RadioStationViewSet(viewsets.ModelViewSet):
# #     queryset = RadioStation.objects.all()
# #     serializer_class = RadioStationSerializer





# # class PodcastViewSet(viewsets.ModelViewSet):
# #     queryset = Podcast.objects.all()
# #     serializer_class = PodcastSerializer

# # class PodcastEpisodeViewSet(viewsets.ModelViewSet):
# #     queryset = PodcastEpisode.objects.all()
# #     serializer_class = PodcastEpisodeSerializer

# # class PodcastCommentViewSet(viewsets.ModelViewSet):
# #     queryset = PodcastComment.objects.all()
# #     serializer_class = PodcastCommentSerializer

# # class DownloadedPodcastViewSet(viewsets.ModelViewSet):
# #     queryset = DownloadedPodcast.objects.all()
# #     serializer_class = DownloadedPodcastSerializer

# # class PremiumUserViewSet(viewsets.ModelViewSet):
# #     queryset = PremiumUser.objects.all()
# #     serializer_class = PremiumUserSerializer

# # class TopChartViewSet(viewsets.ModelViewSet):
# #     queryset = TopChart.objects.all()
# #     serializer_class = TopChartSerializer

# # class OfflineItemViewSet(viewsets.ModelViewSet):
# #     queryset = OfflineItem.objects.all()
# #     serializer_class = OfflineItemSerializer

# # class NotificationViewSet(viewsets.ModelViewSet):
# #     queryset = Notification.objects.all()
# #     serializer_class = NotificationSerializer

# # class MessageViewSet(viewsets.ModelViewSet):
# #     queryset = Message.objects.all()
# #     serializer_class = MessageSerializer

# # class ReviewViewSet(viewsets.ModelViewSet):
# #     queryset = Review.objects.all()
# #     serializer_class = ReviewSerializer

# # class UserLocationViewSet(viewsets.ModelViewSet):
# #     queryset = UserLocation.objects.all()
# #     serializer_class = UserLocationSerializer

# # class PaymentMethodViewSet(viewsets.ModelViewSet):
# #     queryset = PaymentMethod.objects.all()
# #     serializer_class = PaymentMethodSerializer

# # class PaymentTransactionViewSet(viewsets.ModelViewSet):
# #     queryset = PaymentTransaction.objects.all()
# #     serializer_class = PaymentTransactionSerializer

# # class RecommendationViewSet(viewsets.ModelViewSet):
# #     queryset = Recommendation.objects.all()
# #     serializer_class = RecommendationSerializer

# # class UserActivityViewSet(viewsets.ModelViewSet):
# #     queryset = UserActivity.objects.all()
# #     serializer_class = UserActivitySerializer

# # class SharedItemViewSet(viewsets.ModelViewSet):
# #     queryset = SharedItem.objects.all()
# #     serializer_class = SharedItemSerializer

# # class EventViewSet(viewsets.ModelViewSet):
# #     queryset = Event.objects.all()
# #     serializer_class = EventSerializer

# # class AdvertisementViewSet(viewsets.ModelViewSet):
# #     queryset = Advertisement.objects.all()
# #     serializer_class = AdvertisementSerializer

# # class UserFeedbackViewSet(viewsets.ModelViewSet):
# #     queryset = UserFeedback.objects.all()
# #     serializer_class = UserFeedbackSerializer

# # class ApplicationStatisticsViewSet(viewsets.ModelViewSet):
# #     queryset = ApplicationStatistics.objects.all()
# #     serializer_class = ApplicationStatisticsSerializer

# # class UserPreferencesViewSet(viewsets.ModelViewSet):
# #     queryset = UserPreferences.objects.all()
# #     serializer_class = UserPreferencesSerializer

# # class FriendViewSet(viewsets.ModelViewSet):
# #     queryset = Friend.objects.all()
# #     serializer_class = FriendSerializer

# # class BadgeViewSet(viewsets.ModelViewSet):
# #     queryset = Badge.objects.all()
# #     serializer_class = BadgeSerializer

# # class SubscriptionViewSet(viewsets.ModelViewSet):
# #     queryset = Subscription.objects.all()
# #     serializer_class = SubscriptionSerializer

# # class PlayHistoryViewSet(viewsets.ModelViewSet):
# #     queryset = PlayHistory.objects.all()
# #     serializer_class = PlayHistorySerializer

# # class FavoriteViewSet(viewsets.ModelViewSet):
#     queryset = Favorite.objects.all()
#     serializer_class = FavoriteSerializer

# Import necessary modules
from rest_framework import serializers
from .models import *


#  Define serializers for each model
# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = '__all__'
        
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        
    def validate_duration(self, value):
        # Custom validation for the duration field
        if value.total_seconds() > 600:  # Assuming a maximum duration of 10 minutes (600 seconds)
            raise serializers.ValidationError("Song duration cannot exceed 10 minutes.")
        return value

class SongRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongRating
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumReview
        fields = '__all__'
    
class FollowedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Followed
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

class PlaylistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistItem
        fields = '__all__'

class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = '__all__'

class RadioStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadioStation
        fields = '__all__'

class LikedSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikedSong
        fields = '__all__'

class SavedAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedAlbum
        fields = '__all__'

class FollowedArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowedArtist
        fields = '__all__'



class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'

class PodcastEpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PodcastEpisode
        fields = '__all__'

class PodcastCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PodcastComment
        fields = '__all__'

class DownloadedPodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownloadedPodcast
        fields = '__all__'

class PremiumUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumUser
        fields = '__all__'

class TopChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopChart
        fields = '__all__'

class OfflineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfflineItem
        fields = '__all__'
    
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = '__all__'

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'

class PaymentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransaction
        fields = '__all__'

class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = '__all__'

class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = '__all__'

class SharedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedItem
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'

class UserFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFeedback
        fields = '__all__'

class ApplicationStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationStatistics
        fields = '__all__'

class UserPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreferences
        fields = '__all__'

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = '__all__'

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

class PlayHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayHistory
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
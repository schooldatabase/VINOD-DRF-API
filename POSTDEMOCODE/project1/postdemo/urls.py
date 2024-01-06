from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a DefaultRouter instance
router = DefaultRouter()

# Register viewsets for different models
# router.register(r'user-profiles', views.UserProfileViewSet)
# router.register(r'post', views.PostViewSet)
router.register(r'songs', views.SongViewSet)
router.register(r'albums', views.AlbumViewSet)
router.register(r'artists', views.ArtistViewSet)


# router.register(r'song-ratings', views.SongRatingViewSet)
# router.register(r'liked-songs', views.LikedSongViewSet)
# router.register(r'album-reviews', views.AlbumReviewViewSet) # not used full album reviews
# router.register(r'saved-albums', views.SavedAlbumViewSet)
# router.register(r'followed-artists', views.FollowedArtistViewSet)
# router.register(r'followed', views.FollowedViewSet)
# router.register(r'playlists', views.PlaylistViewSet)
# router.register(r'playlist-items', views.PlaylistItemViewSet)
# router.register(r'collaborators', views.CollaboratorViewSet)
# router.register(r'radio-stations', views.RadioStationViewSet)
# router.register(r'podcasts', views.PodcastViewSet)
# router.register(r'podcast-episodes', views.PodcastEpisodeViewSet)
# router.register(r'podcast-comments', views.PodcastCommentViewSet)
# router.register(r'downloaded-podcasts', views.DownloadedPodcastViewSet)
# router.register(r'premium-users', views.PremiumUserViewSet)
# router.register(r'top-charts', views.TopChartViewSet)
# router.register(r'offline-items', views.OfflineItemViewSet)
# router.register(r'notifications', views.NotificationViewSet)
# router.register(r'messages', views.MessageViewSet)
# router.register(r'reviews', views.ReviewViewSet)
# router.register(r'user-locations', views.UserLocationViewSet)
# router.register(r'payment-methods', views.PaymentMethodViewSet)
# router.register(r'payment-transactions', views.PaymentTransactionViewSet)
# router.register(r'recommendations', views.RecommendationViewSet)
# router.register(r'user-activities', views.UserActivityViewSet)
# router.register(r'shared-items', views.SharedItemViewSet)
# router.register(r'events', views.EventViewSet)
# router.register(r'advertisements', views.AdvertisementViewSet)
# router.register(r'user-feedback', views.UserFeedbackViewSet)
# router.register(r'application-statistics', views.ApplicationStatisticsViewSet)
# router.register(r'user-preferences', views.UserPreferencesViewSet)
# router.register(r'friends', views.FriendViewSet)
# router.register(r'badges', views.BadgeViewSet)
# router.register(r'subscriptions', views.SubscriptionViewSet)
# router.register(r'play-history', views.PlayHistoryViewSet)
# router.register(r'favorites', views.FavoriteViewSet)

# Define urlpatterns
urlpatterns = [
    path('', include(router.urls)),
    # Add more URL patterns for other views or custom endpoints here.
]

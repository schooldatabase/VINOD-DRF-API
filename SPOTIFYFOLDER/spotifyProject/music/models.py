from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import timedelta
# Create your models here.

# user profile
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True)
#     birth_date = models.DateField(blank=True, null=True)
#     profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
#     # Add fields for user location, website, and social media links.
#     location = models.CharField(max_length=100, blank=True, null=True)
#     website = models.URLField(max_length=200, blank=True, null=True)
#     facebook_profile = models.URLField(max_length=200, blank=True, null=True)
#     twitter_profile = models.URLField(max_length=200, blank=True, null=True)

#     def __str__(self):
#         return self.user.username

# music
def validate_audio_extension(value):
    if not value.name.endswith(('.mp3', '.wav', '.ogg', '.flac', '.aac')):
        raise ValidationError(_('Invalid file format. Supported formats: .mp3, .wav, .ogg, .flac, .aac'))

def validate_audio_size(value):
    max_size = 10 * 1024 * 1024  # 10 MB
    if value.size > max_size:
        raise ValidationError(_('File size exceeds the maximum limit of 10 MB.'))
    
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    duration = models.DurationField()
    audio_file = models.FileField(upload_to='audio/', validators=[validate_audio_extension, validate_audio_size])
    # Additional fields for the Music app
    album = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()

    def __str__(self):
        return self.title
# SongRating
class SongRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default= 0, choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])
    # Add fields for additional details or comments.

    def __str__(self):
        return f"{self.user.username}'s rating for {self.song.title}"
    
    def clean(self):
        if self.rating < 1 or self.rating > 5:
            raise ValidationError('Rating must be between 1 and 5.')

# Library 
class LikedSong(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # song = models.ForeignKey('music.Song', on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    
class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='album_covers/')
    release_date = models.DateField()
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class AlbumReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    artist_name = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()

class SavedAlbum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # album = models.ForeignKey('music.Album', on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    
class Artist(models.Model): 
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    albums = models.ManyToManyField(Album, related_name='artists')  # Use a custom related_name
    followers_count = models.PositiveIntegerField(default=0)  # Add this field
    
class FollowedArtist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # artist = models.ForeignKey('music.Artist', on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Followed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    followed_artist = models.ForeignKey(FollowedArtist, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    # You can add more fields as needed

    class Meta:
        unique_together = ('user', 'followed_artist')

    def __str__(self):
        return f'{self.user.username} follows {self.followed_artist.artist.name}'
    
# Playlists
class Playlist(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    songs = models.ManyToManyField(Song, through='PlaylistItem')
    is_private = models.BooleanField(default=False)
    cover_image = models.ImageField(upload_to='playlist_covers/', blank=True, null=True)
    collaborators = models.ManyToManyField(User, related_name='collaborative_playlists', blank=True)

class PlaylistItem(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    
#   PlaylistHistory  
class PlaylistHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # Add fields to track the songs and order in the playlist history.
    

class Collaborator(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    can_edit = models.BooleanField(default=False)
    # Add more fields to specify the role of the collaborator.

    def __str__(self):
        return f"{self.user.username} - {self.playlist.name} Collaborator"
   
# Radio 
class RadioStation(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # songs = models.ManyToManyField('music.Song')
    songs = models.ManyToManyField(Song)


    
# Social
class Friendship(models.Model):
    user1 = models.ForeignKey(User, related_name='user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='user2', on_delete=models.CASCADE)

class ActivityFeed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
# Podcasts 
class Podcast(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    host = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='podcast_covers/')

    # Additional fields for the Podcast model
    genre = models.CharField(max_length=50)
    subscribers = models.ManyToManyField('auth.User', related_name='subscribed_podcasts')

    def __str__(self):
        return self.title

class PodcastEpisode(models.Model):
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DurationField()
    audio_file = models.FileField(upload_to='audio/', validators=[validate_audio_extension, validate_audio_size])

    
    # Additional fields for the PodcastEpisode model
    release_date = models.DateField()

    def __str__(self):
        return self.title

# PodcastComment
class PodcastComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    podcast_episode = models.ForeignKey(PodcastEpisode, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add fields for additional details or replies.

    def __str__(self):
        return f"Comment by {self.user.username} on {self.podcast_episode.title}"
    
class DownloadedPodcast(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    episode = models.ForeignKey(PodcastEpisode, on_delete=models.CASCADE)

# Premium
class PremiumUser(models.Model):
    SUBSCRIPTION_TYPE_CHOICES = [
        ('monthly', 'Monthly'),
        ('annual', 'Annual'),
        ('quarterly', 'Quarterly'),
        ('lifetime', 'Lifetime'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
        ('upi', 'UPI (Unified Payments Interface)'),
        ('other', 'Other'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription_type = models.CharField(
        max_length=50,
        choices=SUBSCRIPTION_TYPE_CHOICES,
        default='monthly',  # Set a default subscription type if needed
    )
    expiration_date = models.DateField()  # Date when the premium subscription expires
    active = models.BooleanField(default=True)  # Indicates if the premium membership is active
    payment_method = models.CharField(
        max_length=50,
        choices=PAYMENT_METHOD_CHOICES,
        default='credit_card',  # Set a default payment method if needed
    )
    payment_reference = models.CharField(max_length=100)  # Reference ID for the payment
    usage_stats = models.JSONField(null=True, blank=True)  # Store user's premium usage statistics in JSON format
    is_auto_renew = models.BooleanField(default=False)  # Indicates whether the subscription auto-renews
    promo_code = models.CharField(max_length=20, null=True, blank=True)  # Stores a promo code if used for the subscription
    last_payment_date = models.DateTimeField(null=True, blank=True)  # Date and time of the last payment
    notes = models.TextField(null=True, blank=True)  # Additional notes or comments about the premium user

    # Add more fields as needed

    def __str__(self):
        return self.user.username
 
#  Connect Devices    
class ConnectedDevice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=50)
    # Add fields for device information and status.
    
# queue item  
# class QueueItem(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # song = models.ForeignKey('music.Song', on_delete=models.CASCADE)
    # Add fields for queue position, timestamp, etc.
    
# Search history
class SearchEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add fields to track the search type (e.g., songs, artists, albums).
    
# Recently Played 
class PlayedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=50)  # Song or Playlist
    content_id = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
# top chat
class TopChart(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    # Add fields for chart-specific details.

# offline mode   
class OfflineItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=50)  # Song or Playlist
    content_id = models.PositiveIntegerField()
    # Add fields for offline storage details.
    
#Notification  
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    notification_type = models.CharField(max_length=50)
    
# Message 
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# Review 
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add fields for the reviewed item (e.g., song, album, podcast)
    
# Geolocation
class UserLocation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    # Add fields for user's location details.
    
class PaymentMethod(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
        ('upi', 'UPI (Unified Payments Interface)'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES,
        default='credit_card',  # Set a default payment method if needed
    )
    card_number = models.CharField(max_length=16, null=True, blank=True)
    card_holder_name = models.CharField(max_length=100, null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    is_default = models.BooleanField(default=False)

    # Add fields to store billing address and other payment details
    billing_address = models.TextField(null=True, blank=True)
    cvv = models.CharField(max_length=4, null=True, blank=True)  # Card Verification Value for credit cards
    paypal_email = models.EmailField(null=True, blank=True)  # Email associated with PayPal account

    # Add more fields or methods as needed

    def __str__(self):
        return f"{self.user.username}'s {self.get_payment_type_display()} Payment Method"

# PaymentTransaction

class PaymentTransaction(models.Model):
    TRANSACTION_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    
    TRANSACTION_TYPE_CHOICES = [
        ('purchase', 'Purchase'),
        ('refund', 'Refund'),
        ('subscription', 'Subscription'),
        ('other', 'Other'),
    ]
    
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=TRANSACTION_STATUS_CHOICES, default='pending')
    reference_number = models.CharField(max_length=50, null=True)  # Reference number or transaction ID
    payment_gateway = models.CharField(max_length=50, null=True, blank=True)  # Payment gateway used
    description = models.TextField(null=True, blank=True)  # Additional transaction description

    # Add more fields as needed for your payment transaction records
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE_CHOICES, default='other')  # e.g., 'purchase', 'refund'
    order_number = models.CharField(max_length=50, null=True, blank=True)  # Order number associated with the transaction
    payment_status_code = models.CharField(max_length=10, null=True, blank=True)  # Payment gateway status code
    currency = models.CharField(max_length=3, null=True, blank=True)  # Currency code (e.g., 'USD', 'EUR')
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)  # Exchange rate used
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Tax amount
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Shipping cost
    payment_receipt = models.FileField(upload_to='payment_receipts/', null=True, blank=True)  # Payment receipt file
    additional_info = models.JSONField(null=True, blank=True)  # Additional JSON data for custom details

    def __str__(self):
        return f"Transaction for {self.user.username} - {self.amount} {self.get_status_display()}"
    
# Recommendation 
class Recommendation(models.Model):
    from_user = models.ForeignKey(User, related_name='recommendations_sent', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='recommendations_received', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add fields for recommendation details.
    
# UserActivity
class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)  # e.g., "listening", "creating_playlist"
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField()  # Additional details about the activity.
    location = models.CharField(max_length=100, blank=True, null=True)  # Capture the user's location.
    device_info = models.CharField(max_length=100, blank=True, null=True)  # Store information about the user's device.
    duration_seconds = models.PositiveIntegerField(blank=True, null=True)  # Track the duration of the activity.
    
# sharing   
class SharedItem(models.Model):
    user_from = models.ForeignKey(User, related_name='shared_items_sent', on_delete=models.CASCADE)
    user_to = models.ForeignKey(User, related_name='shared_items_received', on_delete=models.CASCADE)
    content_type = models.CharField(max_length=50)  # e.g., "song", "playlist"
    content_id = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True, null=True)  # A custom message along with the shared item.
    permissions = models.CharField(max_length=50)  # Define permissions (e.g., read-only, edit).
    expiration_date = models.DateTimeField(blank=True, null=True)  # Set an expiration date for shared items.
    is_viewed = models.BooleanField(default=False)  # Track whether the shared item has been viewed.
    
# Event
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)  # Include ticket price.
    organizer = models.CharField(max_length=100)  # Store event organizer information.
    event_url = models.URLField(blank=True, null=True)  # Link to an event website.
    
# Advertisement
class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='ads/')
    link = models.URLField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)  # Track the status of the advertisement.
    target_audience = models.CharField(max_length=100)  # Define the target audience.
    placement = models.CharField(max_length=100)  # Specify ad placement details.
    
# UserFeedback
class UserFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50)  # Categorize feedback (e.g., bug report, feature request).
    rating = models.PositiveIntegerField()  # Allow users to provide ratings.
    screenshots = models.ImageField(upload_to='feedback_screenshots/', blank=True, null=True)
    
# statistics
class ApplicationStatistics(models.Model):
    active_users = models.PositiveIntegerField()
    total_songs_played = models.PositiveIntegerField()
    revenue = models.DecimalField(max_digits=10, decimal_places=2)  # Track financial data.
    user_growth_rate = models.DecimalField(max_digits=5, decimal_places=2)  # Monitor user acquisition.
    feature_usage = models.JSONField()  # Store data about feature usage.
   
# UserPreferences 
class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dark_mode = models.BooleanField(default=False)
    email_notifications = models.BooleanField(default=True)
    preferred_language = models.CharField(max_length=20, default='en')
    show_recommendations = models.BooleanField(default=True)
    # Add fields to store user-specific preferences, such as theme, notifications, language, etc.
    
# User Friends
class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_friends')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_friends_with')
    is_favorite = models.BooleanField(default=False)
    last_interaction = models.DateTimeField(blank=True, null=True)  # Track the last interaction with the friend.
    # Add more fields for friend status, last interaction, etc.
    
# User Badges
class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='badge_images/')
    users = models.ManyToManyField(User, related_name='badges')
    # Add fields for badge criteria and conditions.
    
# User Subscriptions
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscribed_to = models.ForeignKey(User, related_name='subscribers', on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    subscription_type = models.CharField(max_length=50)  # Define the type of subscription.
    is_active = models.BooleanField(default=True)  # Track the status of the subscription.
    # Add fields for subscription type, status, and payment details.

# User Play History
class PlayHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    play_timestamp = models.DateTimeField(auto_now_add=True)
    duration_seconds = models.PositiveIntegerField()
    # Add fields to track the device used and user's location during play.
    device_used = models.CharField(max_length=100, blank=True, null=True)
    user_location = models.CharField(max_length=100, blank=True, null=True)
    
# User Favorites 
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite_name = models.CharField(max_length=100)
    favorite_type = models.CharField(max_length=50)
    favorite_id = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    # Add fields to specify the type and details of the favorite item.
    

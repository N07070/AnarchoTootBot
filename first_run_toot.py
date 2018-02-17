from mastodon import Mastodon

# The first argument is the name of your app
# The second is the mastodon instance url you want to connect ot.
# Don't touch the last one or everything will break and brun !
Mastodon.create_app(
     '',
     api_base_url = '',
     to_file = 'pytooter_clientcred.secret'
)

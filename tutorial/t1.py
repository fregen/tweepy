from getpass import getpass
import cPickle as pickle
import tweepy

""" Tutorial 1 -- Authentication

Tweepy supports both basic auth and OAuth authentication. It is 
recommended you use OAuth so you can be more secure and also 
set a custom "from xxx" for you application.

Authentication is handled by AuthHandler instances. You must either
create a BasicAuthHandler or OAuthHandler which we will pass into our 
api instance to let twitter know who we are.

First let's try creating a basic auth handler.
"""
username = raw_input('Twitter username: ')
password = getpass('Twitter password: ')
basic_auth = tweepy.BasicAuthHandler(username, password)

"""
Now for an OAuth handler...

You must supply the handler both your consumer key and secret which
twitter supplies you with at http://twitter.com/oauth_clients
You may also supply a callback URL as an optional parameter.
"""
consumer_key = 'ZbzSsdQj7t68VYlqIFvdcA'
consumer_secret = '4yDWgrBiRs2WIx3bfvF9UWCRmtQ2YKpKJKBahtZcU'
oauth_auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
oauth_auth_callback = tweepy.OAuthHandler(consumer_key, consumer_secret,
                                            'http://test.com/my/callback/url')

"""
We must redirect the user to twitter so they can authorize us.
To do this you will ask the OAuthHandler for the authorization URL
which you will then display to the user OR open their browser to that URL.
For this example we will just print the URL to the console.
"""
print 'Please authorize us: %s' % oauth_auth.get_authorization_url()

"""
Now that we have been authorized, we must fetch the access token.
To do this the user must either supply us with a PIN OR if we are using a callback
we must wait for that and grab the verifier number from the request.
For this example we will ask the user for the PIN.
"""
verifier = raw_input('PIN: ').strip()
oauth_auth.get_access_token(verifier)

"""
Okay we are all set then with OAuth. If you want to store the access
token for later use, here's how...
"""
access_token = oauth_auth.access_token
print 'Access token: %s' % access_token

"""
For later use we will keep the token pickled into a file.
"""
token_file = open('oauth_token', 'wb')
pickle.dump(access_token, token_file)
token_file.close()

"""
And to reload the token...
"""
token_file = open('oauth_token', 'rb')
oauth_token = pickle.load(token_file)
token_file.close()
oauth_auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
oauth_auth.access_token = access_token

"""
Now let's plugin our newly created auth handler into an API instance
so we can start playing with the Twitter API. :)
"""
api_via_basic = tweepy.API(basic_auth)
api_via_oath = tweepy.API(oauth_auth)

""" API.new() shortcut

To make creating API instances a bit more easy you way use the
static method API.new() to create new instances. Here is an example:
"""
new_basic_api = tweepy.API.new('basic', username, password)
new_oauth_api = tweepy.API.new('oauth', consumer_key, consumer_secret)
new_oauth_api.auth_handler  # here's how to access the auth handler to do the oauth flow

""" The End

That wraps up this first tutorial. You have learned how to setup
authentication and create an API instance which can then be used
to interact with the Twitter API.

We are now ready for Tutorial 2.
"""


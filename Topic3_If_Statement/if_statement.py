# an example of an instagram page

following = True # boolean variable

if following:
    button_message = 'Following'
    button_color = 'grey'

else: # not following this account
    button_message = 'Follow'
    button_color = 'blue'


user_has_liked_post = False # gives you a red heart when liked and
                            # nothing when not liked with images icon used

if user_has_liked_post:
        like_icon = 'red_heart.jpg'
else:
        like_icon = 'heart_outline.jpg'

print(like_icon)

likes = 50 # looks and counts for how many people liked

if likes == 0: # no likes yet
    message = 'Be the first to like this'
elif likes == 1:
    message = '1 like'
else:
    message = str(likes) + ' likes'

print(message)


post_text = 'llama ' * 100
print(post_text)








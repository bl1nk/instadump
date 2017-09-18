# instadump

This can dump the Instagram stories of all your friends.  You can only dump
stories that have been submitted in the last 24 hours. 

Theoretically you can also download stories older than 24 hours if you know
their URL.

Based on the findings of [Alec Garcia on Medium][source].

Edit `config.py` to set things up.

###### `pushover_app_token` & `pushover_user_token`

Add/edit these if you want to get notified via pushover when the script
finishes.  Useful if you run this as a cronjob or systemd timer or whatever.

###### `instagram_cookies`

Holds `ds_user_id`, `sessionid` and `csrftoken` you can get on instagram.com.

[source]: https://medium.com/@calialec/chrome-ig-story-bribing-the-instagram-story-api-with-cookies-c813e6dff911

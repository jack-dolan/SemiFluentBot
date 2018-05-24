# [SemiFluentBot](https://www.reddit.com/user/SemiFluentBot/)
A small Reddit bot that takes Reddit text titles, translates them several times (like the game "Telephone"), and returns it in English again. Sometimes yields funny results.

Because the results from this bot aren't always great (e.g. the text is largely unchanged or changed so much it's not readable), a control mechanism is built in via a Telegram bot. The python translation bot sends its output to the user via Telegram, and then the user has the option to choose which (if any) of the presented options are good enough to actually post on Reddit.

### Reviews:
* "This is the bot we need, but not the one we deserve." *-/u/Robelius*
* "This reads like a Trump quote" *-/u/freakierchicken*
* "Good bot" *-75+ reddit users*

## Usage
- /start to start the bot after TB.py has been started successfully
- When presented with translated options:
  - /cancel to select none, and set the bot to wait for /start again, or
  - "x,y,z..." or "x" to select options to post. E.g. if you want to post options 1, 3, and 7 (as they are labelled in the Telegram messages), reply with "1,3,7". Don't include spaces or quotes.

## Flowchart
![SemiFluentBot Flowchart](https://github.com/drummingjack2/SemiFluentBot/blob/master/SFB_flowchart.png)

## authentication.py
You need a file in the project directory called `authentication.py` with the following:

    USER_AGENT = 'redditscript_useragent_e.g._SemiFluentBot by /u/SemiFluentBot'
    CLIENT_ID = 'redditscript_client_id'
    CLIENT_SECRET = 'reddit_scriptclient_secret'
    USERNAME = 'redditUsername'
    PASSWORD = 'redditPassword'
    TELEGRAM_TOKEN = 'insert_your_telegram_bot_token_here'
    STARTUP_KEY = 'string_you_want_to_use_to_start_bot'
    
## Heroku Deployment
SemiFluentBot originally ran on a Raspberry Pi, but I wanted to learn how to deploy to a cloud platform, and I chose Heroku. If you're interested in the steps I took to get the program ready for deployment, here they are:
* Remove `authentication.py` which previously contained variables such as reddit and python authentication passwords (detailed above). Instead, declare these variables as Heroku config variables, and call them programatically like so: `user_agent = os.environ['USER_AGENT']`. You'll need to import os for this.
* Create a file called Procfile (no file extension) - This file tells the Heroku platform what command(s) to run in order to start your app. In this case, it's a one line file saying worker: `python telegramBot.py`
* Create a file called runtime.txt - This file just declares the version of python needed to run your app.
* Create a file called requirements.txt - this is a file that declares all the dependencies your app has, so that the cloud platform can install them for you before the app starts running. Essentially, anythin you would 'pip install XXX' or otherwise install with a package manager to run your Python app, list it here.

## Bugs

~~Currently SFB doesn't discern between Telegram users, so anyone who knows the username and commands can use it.~~

Occasionally the telegram service has timeout issues, but it doesn't appear to be related to the duration of the reddit post fetch. Not sure why it happens, but it is sometimes caught with my current barebones error catching.

When the aforementioned error catching doesn't work, errors about having two instances of the telegram bot running simultaneously get thrown.

There is no input filter whatsoever, so if the user replies with something other than "/cancel", "x,y,z", or "x", there are no filters to catch that.


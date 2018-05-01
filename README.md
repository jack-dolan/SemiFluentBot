# SemiFluentBot
A small Reddit bot that takes Reddit text titles, translates them several times (like the game "Telephone"), and returns it in English again. Sometimes yields funny results.

Because the results from this bot aren't always great (e.g. the text is largely unchanged or changed so much it's not readable), a control mechanism is built in via a Telegram bot. The python translation bot sends its output to the user via Telegram, and then the user has the option to choose which (if any) of the presented options are good enough to actually post on Reddit.

## Flowchart
![SemiFluentBot Flowchart](https://github.com/drummingjack2/SemiFluentBot/blob/master/SFB_flowchart.png)

## Bugs

Currently SFB doesn't discern between Telegram users, so anyone who knows the username and commands can use it.

Occasionally the telegram service has timeout issues, but it doesn't appear to be related to the duration of the reddit post fetch. Not sure why it happens, but it is sometimes caught with my current barebones error catching.

When the aforementioned error catching doesn't work, errors about having two instances of the telegram bot running simultaneously get thrown.

There is no input filter whatsoever, so if the user replies with something other than "/cancel", "x,y,z", or "x", there are no filters to catch that.


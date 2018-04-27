# SemiFluentBot
A small Reddit bot that takes Reddit text titles, translates them several times (like the game "Telephone"), and returns it in English again. Sometimes yields funny results.

Because the results from this bot aren't always great (e.g. the text is largely unchanged or changed so much it's not readable), a control mechanism is built in via a Telegram bot. The python translation bot sends its output to the user via Telegram, and then the user has the option to choose which (if any) of the presented options are good enough to actually post on Reddit.

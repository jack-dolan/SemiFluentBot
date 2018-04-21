import praw
import random
import translate
from authentication import USERNAME, PASSWORD, USER_AGENT, CLIENT_ID, CLIENT_SECRET

user_agent = USER_AGENT
client_id = CLIENT_ID
client_secret = CLIENT_SECRET
username = USERNAME
password = PASSWORD

r = praw.Reddit(user_agent=user_agent, client_id=client_id, client_secret=client_secret,
                username=username, password=password)
r.read_only = False


def lang_roller(lang):   # Randomly chooses middle languages (ie EN > X > Y > Z > EN)
    if lang == 1:  # spanish
        chosen_lang = ["es", "Spanish"]
    elif lang == 2:  # french
        chosen_lang = ["fr", "French"]
    elif lang == 3:  # chinese (traditional)
        chosen_lang = ["zh-TW", "Chinese (Traditional)"]
    elif lang == 4:  # russian
        chosen_lang = ["ru", "Russian"]
    elif lang == 5:  # hebrew
        chosen_lang = ["iw", "Hebrew"]
    elif lang == 6:  # korean
        chosen_lang = ["ko", "Korean"]
    elif lang == 7:  # dutch
        chosen_lang = ["nl", "Dutch"]
    else:
        chosen_lang = ["es", "Spanish"]

    return chosen_lang


def trans_it(text, lang_1, lang_2, lang_3):  # Uses translate.translate function and string-ifies everything out nicely.
    trans_it_output = str(("English > " + lang_1[1] + " > " + lang_2[1] + " > " + lang_3[1] +
                           " > English") + '\n' + ("Original: " + text) + '\n' +
                          ("SemiFluent: " + translate.translate(text, lang_1[0], lang_2[0], lang_3[0])) + '\n')
    return trans_it_output


def produce_output():
    subreddit = r.subreddit('ShowerThoughts')
    submissionList = []
    for submission in subreddit.hot(limit=5):  # Increase this number if you want more posts fetched
        if submission.stickied == 0:  # Excludes stickied posts from printout
            submissionList.append(submission)  # submissionList is now a list of (10-stickies) Submission entities

    for submission in submissionList:
        post_title = submission.title
        langList = random.sample(range(1, 8), 3)
        rolled_lang1 = (lang_roller(langList[0]))
        rolled_lang2 = (lang_roller(langList[1]))
        rolled_lang3 = (lang_roller(langList[2]))
        print(trans_it(post_title, rolled_lang1, rolled_lang2, rolled_lang3))


produce_output()

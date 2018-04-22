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


def trans_it(count, text, lang_1, lang_2, lang_3):  # Uses translate.translate function
                                                    # and string-ifies everything out nicely.
    trans_it_output = str(str(count) + '\n' + ("English > " + lang_1[1] + " > " + lang_2[1] + " > " + lang_3[1] +
                                               " > English") + '\n' + ("Original: " + text) + '\n' + ("SemiFluent: " +
                                                translate.translate(text, lang_1[0], lang_2[0], lang_3[0])) + '\n')
    return trans_it_output


submissionList = []  # A global list of submission objects, filled with top X posts
postable_list = []  # A global list of the above submissions, but formatted into reddit-postable strings


def produce_output():
    subreddit = r.subreddit('ShowerThoughts')

    global submissionList
    global postable_list

    submissionList = []  # A list of submission objects
    for submission in subreddit.hot(limit=10):  # Increase this number if you want more posts fetched
        if submission.stickied == 0:  # Excludes stickied posts from printout
            submissionList.append(submission)  # submissionList is now a list of (10-stickies) Submission entities
    item_count = 0
    options_list = []  # A list of Telegram-message-formatted submission objects
    postable_list = []

    for submission in submissionList:
        item_count += 1
        post_title = submission.title
        langList = random.sample(range(1, 8), 3)
        rolled_lang1 = (lang_roller(langList[0]))
        rolled_lang2 = (lang_roller(langList[1]))
        rolled_lang3 = (lang_roller(langList[2]))
        # print(trans_it(item_count, post_title, rolled_lang1, rolled_lang2, rolled_lang3))
        options_list.append(trans_it(item_count, post_title, rolled_lang1, rolled_lang2, rolled_lang3))
        postable_list.append(str("Here's that ShowerThought translated from English, to three different languages, "
                                 "then back to English.\n\n" + "English > " + rolled_lang1[1] + " > " + rolled_lang2[1]
                                 + " > " + rolled_lang3[1] + " > English\n\n" + translate.translate(post_title,
                                rolled_lang1[0], rolled_lang2[0], rolled_lang3[0])))

    return options_list


def receive_input(choice_string):
    chosen_list = [int(item) if item.isdigit() else item for item in choice_string.split(',')]  # Gets choices into list
    chosen_submission_list = []  # Will be a list of the chosen translations, in reddit-postable format
    for num in chosen_list:
        chosen_submission_list.append(postable_list[(num-1)])

    comment_count = 0
    for comment in chosen_submission_list:
        current_submission = submissionList[chosen_list[comment_count]-1]
        current_submission.reply(comment)
        comment_count += 1



# test123 = produce_output()
# receive_input('1')
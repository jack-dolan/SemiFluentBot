import praw
import random
import translate
import os

user_agent = os.environ['USER_AGENT']
client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
username = os.environ['USERNAME']
password = os.environ['PASSWORD']

r = praw.Reddit(user_agent=user_agent, client_id=client_id, client_secret=client_secret,
                username=username, password=password)
r.read_only = False

language_list = {
    "1": ["es", "Spanish"],
    "2": ["fr", "French"],
    "3": ["zh-TW", "Chinese (Traditional)"],
    "4": ["ru", "Russian"],
    "5": ["iw", "Hebrew"],
    "6": ["ko", "Korean"],
    "7": ["nl", "Dutch"],
    "8": ["ga", "Irish"],
    "9": ["pa", "Punjabi"]
}


def trans_it(count, text, lang_1, lang_2, lang_3):  # Uses translate.translate function
                                                    # and string-ifies everything out nicely.
    trans_it_output = str(str(count) + '\n' + ("English > " + lang_1[1] + " > " + lang_2[1] + " > " + lang_3[1] +
                                               " > English") + '\n' + ("Original: " + text) + '\n' + ("SemiFluent: " +
                                                translate.translate(text, lang_1[0], lang_2[0], lang_3[0])) + '\n')
    return trans_it_output

#  TODO: Remove dependency on these global variables. Probably need to use classes
submissionList = []  # A global list of submission objects, filled with top X posts
postable_list = []  # A global list of the above submissions, but formatted into reddit-postable strings


def produce_output(subreddit_choice):
    subreddit = r.subreddit(subreddit_choice)

    global submissionList
    global postable_list

    submissionList = []  # A list of submission objects
    for submission in subreddit.hot(limit=11):  # Increase this number if you want more posts fetched
        if submission.stickied == 0:  # Excludes stickied posts from printout
            submissionList.append(submission)  # submissionList is now a list of (10-stickies) Submission entities
    item_count = 0
    options_list = []  # A list of Telegram-message-formatted submission objects
    postable_list = []  # A list of Reddit-comment-formatted submission objects

    for submission in submissionList:
        item_count += 1
        post_title = submission.title
        rand_num_list = random.sample(range(1, (len(language_list)+1)), 3)  # 3 random non-repeating number 1-(totalLangs)
        rolled_lang1 = language_list[str(rand_num_list[0])]
        rolled_lang2 = language_list[str(rand_num_list[1])]
        rolled_lang3 = language_list[str(rand_num_list[2])]
        options_list.append(trans_it(item_count, post_title, rolled_lang1, rolled_lang2, rolled_lang3))
        post_text = ("Here's that post translated from English, to three random languages, then back to English. [Code]"
                     "(https://github.com/jack-dolan/SemiFluentBot)\n\nEnglish > {} > {} > {} > English\n\n{}")
        postable_list.append(post_text.format(rolled_lang1[1], rolled_lang2[1], rolled_lang3[1],
                            translate.translate(post_title, rolled_lang1[0], rolled_lang2[0], rolled_lang3[0])))

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


# Need to create a telegram bot, then interface with it here using the python-telegram-bot library
import authentication
import logging
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler)

token = authentication.TELEGRAM_TOKEN

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

#-----TEST VARIABLES AND STUFF-----------------
# USE THIS FORMATE WHEN PASSING BACK OPTIONS
translated_options = ['1\nThis is the original text\nThis is the translated text\n','2\nThis is the original text\nThis is the translated text\n','3\nThis is the original text\nThis is the translated text\n','4\nThis is the original text\nThis is the translated text\n']
#----------------------

CHOICES = 'placeholder'  # Probably don't do this

def start(bot, update):
    update.message.reply_text(
        'Hello! Here are your options:\n\n')
    for option in translated_options:
        update.message.reply_text(option)
    update.message.reply_text('Send /cancel to stop talking to me.\n\n'
        'What are your choices?')

    return CHOICES


def choices(bot, update):
    user = update.message.from_user
    logger.info("Choices of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('You just said "' + update.message.text + '". \n My job here is done unless I messed up.')

    return ConversationHandler.END


def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.')

    return ConversationHandler.END


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the state CHOICES
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            CHOICES: [MessageHandler(Filters.text, choices)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
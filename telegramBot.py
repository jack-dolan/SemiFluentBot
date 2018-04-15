# Need to create a telegram bot, then interface with it here using the python-telegram-bot library
import authentication
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


token = authentication.TELEGRAM_TOKEN

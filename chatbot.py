# -*- coding: utf-8 -*-

import logging
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

__author__ = 'faezrah'

# Uncomment the following line to enable verbose logging
# logging.basicConfig(level=logging.INFO)

bot = ChatBot(
    'Norman',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    database='./database.json'
)

# Train based on the english corpus
bot.train(
    'chatterbot.corpus.english',
    'chatterbot.corpus.english.greetings',
    'chatterbot.corpus.english.conversations'
)

bot.set_trainer(ListTrainer)

bot.train([
    'What is your name?',
    'My name is Norman',
])

print('Type something to begin...')

# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(None)
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except(KeyboardInterrupt, EOFError, SystemExit):
        break

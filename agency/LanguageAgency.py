from agency.Agency import Agency
from environment.LanguageEncoded import LanguageEncoded

import nltk

class LanguageAgency(Agency):

    PUNCTUATION = [',', '.', '!', '?']

    def __init__(self):
        self.name = 'Language'

    def isCommandToMe(self, languageEncoded, myName):
        
        '''
        We have to have at least two tokens for a valid command.

        "[Bot name, Command]"

        "ChairBot stop" or "ChairBot, turn off the lights, please"
        '''
        if len(languageEncoded.tokens) < 2:
            return False

        # if the first word is the bot's name
        if languageEncoded.tokens[0].lower() == myName.lower():

            # got the pos tags
            tags = nltk.pos_tag(languageEncoded.tokens)

            # get the tag for the second word of the statment
            checkPos = None

            # if their are more than two tokens
            if len(languageEncoded.tokens) > 2:

                # if the second token is punctuation
                if languageEncoded.tokens[1] in LanguageAgency.PUNCTUATION:
                
                    # we need the third token's POS
                    checkPos = tags[2][1]

                else:

                    # get the second token's POS
                    checkPos = tags[1][1]

            else:

                # get the second token's POS
                checkPos = tags[1][1]

            '''
            We know the first word was my name, so if the second
            word is a verb, this is a command and it's for me.

            TODO: for some reason right now the following works:

            ChairBot, stop

            but adding a period turns "stop" into a noun

            ChairBot, stop.

            ChairBot, turn doesn't work either, so I need to figure out
            better parsing
            '''

            if checkPos == 'VB':

                return True

        else:

            # the first word was not my name
            return false

    def processSensoryData(self, data):

        # if language detected
        return LanguageEncoded(data.data)
        # else
        # return None

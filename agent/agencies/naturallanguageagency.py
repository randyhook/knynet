class NaturalLanguageAgency:
    '''Base class for processing natural language'''

    def get_addressee(self, message):
        # message is a tuple (word, part-of-speech)

        addressee = list()
        for m in message:
            if m[0] not in ['.', ',', '!']:
                addressee.append(m[0])
            else:
                break;

        return addressee

    def is_command(self, message):
        is_command = False

        addressee = self.get_addressee(message)
        if len(addressee) == 0:
            return False

        # get the first word after the addressee
        if len(message) > len(addressee) + 1 and message[len(addressee) + 1][1] == 'VB':
            is_command = True

        return is_command


from bots.bot import Bot

class SimBot(Bot):
    '''Base Bot Class for Simulator Use'''

    def create(name, serial_number, owner):
        new_bot = Bot(name, serial_number, owner)

        return new_bot

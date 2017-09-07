from util.Client import Client
if __name__ == '__main__':
    bot_name = b"NAME confused\n" # <--- bot name goes here
    c = Client(bot_name)
    c.setup_bot()
    c.run_bot()
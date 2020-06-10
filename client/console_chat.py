from client.chat_client import ChatClient


class ConsoleChat:

    def __init__(self, chat_client: ChatClient):
        self.username: str = ''
        self._chat_client: ChatClient = chat_client

    def start(self):
        self._get_username()
        self._chat_client.start_listen_messages(self._message_received)
        self._get_inputs()

    def _get_username(self):
        while not self.username:
            self.username = input('Enter Username: ')

    def _message_received(self, message):
        print(f'[{message.author}]: {message.text}')

    def _get_inputs(self):
        try:
            text = input('> ')
            while text != 'quit':
                if text:
                    self._chat_client.send_message(self.username, text)
                text = input('> ')
        except KeyboardInterrupt:
            pass
        print('Bye')
        # We tell the customer to disconnect from the server.
        # In general, it is not necessary, because our program is already ending at this point
        self._chat_client.close()

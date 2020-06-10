import threading
import grpc

import client.grpc_out.chat_pb2 as chat_proto
import client.grpc_out.chat_pb2_grpc as chat_grpc


class ChatClient:

    def __init__(self, port=5000, host='127.0.0.1'):
        self._port = port
        self._host = host
        self._on_message_receive = None
        # Create a channel to connect to the service
        self._channel = grpc.insecure_channel(f'{self._host}:{self._port}')
        # Create a service client on this channel
        self._chat_service = chat_grpc.ChattingStub(self._channel)

    def start_listen_messages(self, message_received):
        # The function we'll call when the message comes
        self._on_message_receive = message_received
        # Create a separate thread where we read the incoming text of messages from the server
        threading.Thread(target=self._listen_for_messages, daemon=True).start()

    def _listen_for_messages(self):
        # The cycle will wait until the messages come, process all those who have come and wait for the next
        for message in self._chat_service.MessageStream(chat_proto.Empty()):
            self._on_message_receive(message)
            print('self._on_message_receive(message)')

    def send_message(self, username, text):
        message = chat_proto.Message()
        message.author = username
        message.text = text
        self._chat_service.SendMessage(message)

    def close(self):
        self._channel.close()


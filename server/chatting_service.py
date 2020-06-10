from queue import Queue
from time import sleep

import grpc

import server.grpc_out.chat_pb2 as chat_proto
import server.grpc_out.chat_pb2_grpc as chat_grpc


class ChattingService(chat_grpc.ChattingServicer):
    """
    implements the service described in the Proto file
    """

    MESSAGE_STREAM_INTERVAL: 0.1

    def __init__(self):
        # History of all messages
        self._history = []
        self._is_working = True

    def MessageStream(self, request, context: grpc.ServicerContext):
        last_read = len(self._history) - 1
        # Endlessly send messages while the connection is active
        while context.is_active():
            # Send all messages from the queue of unsent
            while last_read < len(self._history) - 1:
                last_read += 1
                message = self._history[last_read]
                # yield - it's like endless return.
                # The feature will return values over and over again when called yield.
                yield message
            # Add a little sleep to reduce the load on the server by constantly checking new messages
            sleep(0.1)

    def SendMessage(self, message: chat_proto.Message, context):
        print(f'[{message.author}] {message.text}')
        self._history.append(message)
        return chat_proto.Nothing()

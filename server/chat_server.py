from concurrent import futures
from time import sleep
import grpc

import server.grpc_out.chat_pb2_grpc as chat_grpc

from server.chatting_service import ChattingService


class ChatServer:
    """
    a server that hostes our service
    """
    def __init__(self, port=5000, host='[::]', max_workers=3):
        self._port = port
        self._host = host
        # The server is created by thread with maximum max_workers threads,
        # all the thread-driven gRPC
        self._server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
        # We say that our ChattingService implements the chat service described in Proto on this server
        chat_grpc.add_ChattingServicer_to_server(ChattingService(), self._server)

    def serve(self):
        print('Starting server...')
        self._server.add_insecure_port(f'{self._host}:{self._port}')
        self._server.start()
        print(f'Listening on {self._host}:{self._port}')
        print('Press CTRL+C to stop...')
        try:
            # wait_for_termination does nothing (you can replace it with a very large sleep), just waiting
            # Until the server stops, so that the main process of the program does not end.
            self._server.wait_for_termination()
        except KeyboardInterrupt:
            self._server.stop(None)
            print('Server is stopped')


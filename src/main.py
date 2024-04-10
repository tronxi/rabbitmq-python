import time
import event
import signal
from datetime import datetime

import rabbitmq_connection_manager


class Main:
    def __init__(self):
        self.connection_manager = rabbitmq_connection_manager.RabbitmqConnectionManager()
        signal.signal(signal.SIGTSTP, self.exit_program)

    def exit_program(self, signum, frame):
        self.connection_manager.close()
        exit(1)

    def main(self):
        while True:
            ev = event.Event(datetime.now())
            self.connection_manager.publish(ev.to_json())
            print(ev)
            time.sleep(2)


if __name__ == "__main__":
    Main().main()

## this module essentially wraps the Controller object from pynput and runs it in a separate process
# this was necessary to do because pynput doesn't work out of the box on MacOS

from collections import namedtuple
import contextlib
import logging
import multiprocessing
from multiprocessing import Process, Queue
import time

from pynput.keyboard import Controller, Key

# commands to be sent to the keyboard controller process
KBCntrlCommand = namedtuple('KBCntrlCommand', 'name, payload')

def pynp_kb_cntrl_job(command_queue: Queue):
    """Keyboard controller job meant to be run in a separate process

    Args:
        command_queue: inter-process queue for commanding the keyboard controller
    """
    kb_cntrl = Controller()

    while True:
        command: KBCntrlCommand = command_queue.get()
        # tap key
        if command.name == 'tap':
            kb_cntrl.tap(command.payload)
        # terminate the loop
        elif command.name == 'terminate':
            break
        else:
            raise NotImplementedError(f'No command "{command.name}"')

class KBCntrlrWrapper:
    """This class is a wrapper around pynput.keyboard.Controller
    
    This class is not meant to be instantiated by itself in end user code, but rather
    obtained from an instance of KBCntrlrWrapperManager
    """

    def __init__(self, command_queue: Queue):
        self._command_queue = command_queue

    def tap(self, char: Key):
        self._command_queue.put(KBCntrlCommand('tap', char))

class KBCntrlrWrapperManager:
    """Manages the keyboard controller. Only one instance of this class should be
    created, and used everywhere needed

    This class is needed as a container for the separate process spun up for 
    managing the pynput keyboard controller. That separate process is needed 
    because threading doesn't work with pynput on Mac.

    Big fat note: an instance of this class can only be created *in a main module*. 
    Cannot be created as a module-level variable. Multiprocessing doesn't like that,
    at least in python3.8, and will complain about: 
        "RuntimeError: 
            An attempt has been made to start a new process before the
            current process has finished its bootstrapping phase.
        "

    Should only create one instance of this class per program (so only one separate
     process managing the keyboard controller)
    """

    def __init__(self):
        # queue of KBCntrlCommand objects
        self._command_queue = Queue()
        self._kbc_proc = Process(target=pynp_kb_cntrl_job, 
            args=(self._command_queue, ))

        self.kb_cntrl_wrapper = KBCntrlrWrapper(self._command_queue)
        
    def start(self):
        """Start the process. Need to call terminate() at some point too 
        """
        self._kbc_proc.start()

    def terminate(self):
        """Terminate KB controller process

        Should be called when the separate keyboard controller process needs to be spun down
        """
        # tell the process' job to stop doing stuff
        self._command_queue.put(KBCntrlCommand('terminate', None))
        # end the proc
        # todo make sure queue is clear, per https://docs.python.org/3/library/multiprocessing.html#programming-guidelines
        # todo throw error if already joined
        self._kbc_proc.join()

if __name__ == '__main__':

    mngr = KBCntrlrWrapperManager()
    mngr._command_queue.put(KBCntrlCommand('tap', 'l'))
    mngr._command_queue.put(KBCntrlCommand('tap', 'b'))
    mngr._command_queue.put(KBCntrlCommand('tap', 'l'))
    mngr.terminate()

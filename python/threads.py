import threading
from threading import Lock
# Queue is thread safe
# https://docs.python.org/2/library/queue.html#module-Queue
from queue import Queue, Empty

lock = Lock()

def parser_thread(raw_stt_output_q: Queue,
        events: Dict[str, threading.Event]):

    shutdown_event = events['shutdown']
    key_pressed_event = events['key_pressed_parser']
    mouse_clicked_event = events['mouse_clicked_parser']
    
    logger.info("Parser thread ready")
    # the main thread loop. Go forever.
    while True:
        try:
            # get raw text from the queue
            raw_utterance: str = raw_stt_output_q.get(
                block=True, timeout=0.1)
            
            saw_user_action = mouse_clicked_event.is_set() or \
                    key_pressed_event.is_set()

            lock.acquire()
            do_stuff()
            lock.release()

        # queue was empty up to timeout
        except Empty:
            # check if it's time to close shop
            if shutdown_event.is_set(): 
                break
        

# dictionary of events for coordination between threads
events: Dict[str, threading.Event] = {
    # event used to signal shutdown across threads
    # once set, this should NEVER BE CLEARED!
    'shutdown': threading.Event(),
    # indicates sleep mode - when asleep, no speech should be acted on
    'sleep': threading.Event(),
    # mouse moved, for signaling parser thread 
    'mouse_moved_parser': threading.Event(),
    # mouse clicked, for signaling parser thread 
    'mouse_clicked_parser': threading.Event(),
    # key pressed, for signaling parser thread 
    'key_pressed_parser': threading.Event()
}

raw_stt_output_q = queue.Queue()

# note that shutdown event can be invoked from keyboard.py
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = []
    futures.append(executor.submit(
        parser_thread,
        raw_stt_output_q,
        events))
    # other threads...
    futures.append(executor.submit(
        webspeech_thread, 
        raw_stt_output_q,
        events,
        WEBSPEECH_HOST,
        WEBSPEECH_PORT))
    # allows you to see errors from inside threads
    for future in as_completed(futures):
        logger.debug(f"Thread exit: {repr(future.exception())}")
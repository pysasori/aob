import random
import time

def random_delay(min_delay=0.05, max_delay=0.2):
    time.sleep(random.uniform(min_delay, max_delay))
from . import api

import time
import random

@api.route('/')
def index():

    time.sleep(5)

    r_number = random.randint(0, 1000)

    return "inside index : " +str(r_number)
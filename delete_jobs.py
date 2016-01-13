#!/usr/bin/env python

from sys import argv
from threading import Thread
import beanstalkc


def delete_jobs(i, host, port, tube, type):
    bs = beanstalkc.Connection(host=host, port=port, parse_yaml=False)
    bs.use(tube)

    while True:
        if type == "delayed":
            job = bs.peek_delayed()
        else:
            job = bs.peek_buried()

        if job is None:
            break

        try:
            job.delete()
            print str(i) + " - " + tube + " - Deleting job: " + str(job.jid)
        except Exception as e:
            pass


if __name__ == '__main__':
    host = argv[1]
    port = int(argv[2])
    tube = argv[3]
    type = argv[4]

    for i in range(5):
        t = Thread(target=delete_jobs, args=(i, host, port, tube, type))
        t.start()

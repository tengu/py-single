import unittest
import os, sys
import time
from subprocess import Popen, PIPE


class Test(unittest.TestCase):

    def setUp(self):
        self.command_duration = 1
        self.poll_interval = 0.1
        # Locate the command file relative to this test file.
        single_path = os.path.join(os.path.dirname(__file__), 'single.py')
        assert os.path.exists(single_path), ('failed to locate command', single_path)
        self.single_path = single_path

    def test_loser_exists(self):
        """
        Ensure that loser process exists early with appropriate status.

        todo: read stderr of procs and check the loser's message.
        todo: test loser exists immediately.
        """
        procs = dict()

        winner = Popen((self.single_path, '-c', 'sleep', str(self.command_duration)))
        # sys.stderr.write(str(['winner', winner.pid])+'\n')
        procs[winner.pid] = winner

        time.sleep(0.1)

        loser = Popen((self.single_path, '-c', 'sleep', str(self.command_duration)))
        # sys.stderr.write(str(['loser', loser.pid])+'\n')
        procs[loser.pid] = loser

        events = []

        while procs:
            # xxx make this order deterministic so that tick can be tested reliably.
            for pid, proc in procs.items():
                reaped_id, exit_status = os.waitpid(pid, os.WNOHANG)
                print 'wait:', (pid, reaped_id, exit_status)
                if reaped_id:
                    print 'reapted:', reaped_id, exit_status
                    del procs[reaped_id]
                    events.append(('reapted', pid, exit_status))
                time.sleep(self.poll_interval)

        self.assertEqual(
            events,
            [
                ('reapted', loser.pid, 256),
                ('reapted', winner.pid, 0)
            ]
        )
            



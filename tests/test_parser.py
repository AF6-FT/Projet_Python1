import unittest

from pipeline.parser import AuthLogParser

PREFIX = "May 24 00:04:36 ns sshd[1]: "


class TestParser(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = AuthLogParser(2026)

    def test_failed_password(self) -> None:
        event = self.parser.parse_line(PREFIX + "Failed password for root from 1.2.3.4 port 40940 ssh2")
        self.assertEqual(event.status, "Failed")
        self.assertEqual(event.username, "root")
        self.assertEqual(event.ip, "1.2.3.4")

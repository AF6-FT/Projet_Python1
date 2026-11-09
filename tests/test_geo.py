import tempfile
import unittest
from pathlib import Path

from pipeline.geo import GeoLocator
from storage.event_store import EventStore


class TestGeo(unittest.TestCase):
    def test_private_ip(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with EventStore(Path(tmp) / "t.db") as store:
                self.assertEqual(GeoLocator(store).lookup("127.0.0.1"), "Private")

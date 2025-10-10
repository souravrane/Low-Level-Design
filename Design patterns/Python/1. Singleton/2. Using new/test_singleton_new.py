import unittest
from concurrent.futures import ThreadPoolExecutor
from singleton_new import SingletonNew, Logger, Database

class TestSingletonMeta(unittest.TestCase):

    def setUp(self):
        Logger._instance = None
        Database._instance = None

    def test_same_instance_for_logger(self):
        a = Logger()
        b = Logger()
        self.assertIs(a, b)

    def test_same_instance_for_database(self):
        a = Database("a://")
        b = Database("b://") # 2nd creation is ignored
        self.assertIs(a, b)
        self.assertEqual(b.url, "a://")

    def test_init_called_only_once(self):
        calls = {"count" : 0}
        original_init = Logger.__init__

        def count_init(self):
            if not hasattr(self, '_initialized') or not self._initialized:
                calls["count"] += 1
                self._initialized = True

        try:
            Logger.__init__ = count_init  # temporarily replacing __init__
            _ = Logger()
            _ = Logger()
            self.assertEqual(calls["count"], 1)
        finally:
            Logger.__init__ = original_init

    def test_thread_safety(self):
        def make_logger():
            return Logger()

        with ThreadPoolExecutor(max_workers=32) as ex:
            instances = list(ex.map(lambda _: make_logger(), range(500)))
        
        first_instance = instances[0]
        for inst in instances:
            self.assertIs(first_instance, inst)

if __name__ == "__main__":
    unittest.main()
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from learn_path.cli import main
from learn_path.models import Note, ProjectState, Task


class ProjectSmokeTests(unittest.TestCase):
    def test_cli_help(self) -> None:
        self.assertEqual(main([]), 0)


if __name__ == "__main__":
    unittest.main()

"""Pytest configuration and fixtures."""

from __future__ import annotations

import os
import tempfile
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from cocoindex_code.settings import UserSettings

# === Environment setup BEFORE any cocoindex_code imports ===
_TEST_DIR = Path(tempfile.mkdtemp(prefix="cocoindex_test_"))
os.environ["COCOINDEX_CODE_ROOT_PATH"] = str(_TEST_DIR)


# NOTE: deliberately NOT prefixed with `test_` — pytest auto-collects any
# top-level `test_*` function as a test case.
def make_test_user_settings() -> UserSettings:
    """Test UserSettings using the stub embedder — no model download required."""
    from cocoindex_code.settings import EmbeddingSettings, UserSettings

    return UserSettings(
        embedding=EmbeddingSettings(
            provider="stub",
            model="stub",
        ),
    )


@pytest.fixture(scope="session")
def test_codebase_root() -> Path:
    """Session-scoped test codebase directory."""
    return _TEST_DIR

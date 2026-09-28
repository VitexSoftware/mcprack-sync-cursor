"""Resolve Cursor MCP config paths."""

from __future__ import annotations

import os
import sys
from pathlib import Path


def _home() -> Path:
    return Path.home()


def _candidates() -> list[Path]:
    home = _home()
    if sys.platform == "darwin":
        return [
            home / "Library" / "Application Support" / "Cursor" / "User" / "mcp.json",
            home / ".cursor" / "mcp.json",
        ]
    if sys.platform == "win32":
        appdata = os.environ.get("APPDATA", str(home / "AppData" / "Roaming"))
        return [
            Path(appdata) / "Cursor" / "User" / "mcp.json",
            home / ".cursor" / "mcp.json",
        ]
    xdg = Path(os.environ.get("XDG_CONFIG_HOME", str(home / ".config")))
    return [
        xdg / "Cursor" / "User" / "mcp.json",
        home / ".cursor" / "mcp.json",
    ]


def cursor_config_path() -> Path:
    """Prefer an existing config file; otherwise the primary Cursor User path."""
    candidates = _candidates()
    for path in candidates:
        if path.is_file():
            return path
    return candidates[0]

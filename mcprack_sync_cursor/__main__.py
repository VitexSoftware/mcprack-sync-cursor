from __future__ import annotations

import sys

from mcprack_client.cli import run_cli

from .paths import cursor_config_path


def main(argv: list[str] | None = None) -> int:
    return run_cli(
        prog="mcprack-sync-cursor",
        description="Keep Cursor IDE MCP config in sync with mcprack",
        tool="cursor",
        api_client="cursor",
        servers_key="mcpServers",
        resolve_config_path=cursor_config_path,
        argv=argv,
    )


if __name__ == "__main__":
    raise SystemExit(main())

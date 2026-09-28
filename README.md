# mcprack-sync-cursor

Keep **Cursor** IDE MCP server configuration up to date from a
[mcprack](https://github.com/VitexSoftware/mcprack) catalog.

## Install

```bash
sudo apt install mcprack-sync-cursor
```

## Setup

```bash
mcprack-sync-cursor configure \
  --url https://mcprack.example.com \
  --token mcr_your_token_here

mcprack-sync-cursor sync
mcprack-sync-cursor sync --dry-run
mcprack-sync-cursor status
```

Default target (Linux): `~/.config/Cursor/User/mcp.json` (falls back to
`~/.cursor/mcp.json` if that file already exists).

Only the `mcpServers` key is updated; local-only servers are preserved unless
you pass `--replace`.

## Timer

```bash
systemctl --user enable --now mcprack-sync-cursor.timer
```

## License

MIT

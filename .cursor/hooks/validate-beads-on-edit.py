"""Cursor afterFileEdit hook: validate beads when bead files change."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def _extract_edited_paths(payload: dict) -> list[str]:
    paths: list[str] = []

    for key in ("file_path", "filePath", "path", "file"):
        value = payload.get(key)
        if isinstance(value, str):
            paths.append(value)

    for key in ("file_paths", "filePaths", "paths", "files"):
        value = payload.get(key)
        if isinstance(value, list):
            paths.extend(item for item in value if isinstance(item, str))

    tool_input = payload.get("tool_input")
    if isinstance(tool_input, dict):
        for key in ("file_path", "filePath", "path", "target_file"):
            value = tool_input.get(key)
            if isinstance(value, str):
                paths.append(value)

    return paths


def _is_bead_file(path_str: str) -> bool:
    normalized = path_str.replace("\\", "/").lower()
    return "/docs/work-graph/beads/" in normalized and normalized.endswith(".md")


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0

    edited_paths = _extract_edited_paths(payload)
    if not any(_is_bead_file(path) for path in edited_paths):
        return 0

    repo_root = Path(__file__).resolve().parents[2]
    result = subprocess.run(
        [sys.executable, "-m", "harness.beads", "validate"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )

    if result.returncode == 0:
        if result.stdout.strip():
            print(result.stdout.strip())
        return 0

    if result.stderr.strip():
        print(result.stderr.strip(), file=sys.stderr)
    if result.stdout.strip():
        print(result.stdout.strip(), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

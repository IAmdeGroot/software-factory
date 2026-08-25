"""CLI entry point for bead tools."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from harness.beads.claim import ClaimError, claim_bead
from harness.beads.listing import (
    build_ready_queue,
    build_status_summary,
    format_ready_text,
    format_summary_text,
    ready_to_json,
    summary_to_json,
)
from harness.beads.status import TransitionError, complete_bead, done_bead
from harness.beads.validate import validate_beads_dir


def _default_beads_dir() -> Path:
    repo_root = Path(__file__).resolve().parents[2]
    return repo_root / "docs" / "work-graph" / "beads"


def _validate_command(beads_dir: Path) -> int:
    result = validate_beads_dir(beads_dir)
    if result.ok:
        print(f"OK: {len(list(beads_dir.glob('*.md')))} bead(s) validated in {beads_dir}")
        return 0

    print(f"Bead validation failed ({len(result.errors)} error(s)):", file=sys.stderr)
    for error in result.errors:
        print(f"  - {error}", file=sys.stderr)
    return 1


def _list_command(beads_dir: Path, json_output: bool) -> int:
    summary = build_status_summary(beads_dir)
    if json_output:
        print(summary_to_json(summary))
    else:
        print(format_summary_text(summary))
    return 0


def _ready_command(beads_dir: Path, json_output: bool) -> int:
    ready = build_ready_queue(beads_dir)
    if json_output:
        print(ready_to_json(ready))
    else:
        print(format_ready_text(ready))
    return 0


def _claim_command(beads_dir: Path, bead_id: str, assignee: str) -> int:
    try:
        result = claim_bead(beads_dir, bead_id, assignee=assignee)
    except ClaimError as exc:
        print(f"Claim failed: {exc}", file=sys.stderr)
        return 1

    print(f"Claimed {result.bead_id} for {result.assignee}")
    return 0


def _complete_command(beads_dir: Path, bead_id: str) -> int:
    try:
        result = complete_bead(beads_dir, bead_id)
    except TransitionError as exc:
        print(f"Complete failed: {exc}", file=sys.stderr)
        return 1

    print(f"Completed {result.bead_id} ({result.from_status} -> {result.to_status})")
    return 0


def _done_command(beads_dir: Path, bead_id: str) -> int:
    try:
        result = done_bead(beads_dir, bead_id)
    except TransitionError as exc:
        print(f"Done failed: {exc}", file=sys.stderr)
        return 1

    print(f"Marked {result.bead_id} done ({result.from_status} -> {result.to_status})")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    default_beads = str(_default_beads_dir())

    parser = argparse.ArgumentParser(prog="python -m harness.beads")
    subparsers = parser.add_subparsers(dest="command")

    validate_parser = subparsers.add_parser("validate", help="validate all bead files")
    validate_parser.add_argument("beads_dir", nargs="?", default=default_beads)

    list_parser = subparsers.add_parser("list", help="list all bead statuses")
    list_parser.add_argument("beads_dir", nargs="?", default=default_beads)
    list_parser.add_argument("--json", action="store_true", dest="json_output")

    ready_parser = subparsers.add_parser("ready", help="show claimable beads")
    ready_parser.add_argument("beads_dir", nargs="?", default=default_beads)
    ready_parser.add_argument("--json", action="store_true", dest="json_output")

    claim_parser = subparsers.add_parser("claim", help="claim a ready bead")
    claim_parser.add_argument("bead_id", help="bead id to claim, e.g. FACTORY-005")
    claim_parser.add_argument("--assignee", default="agent")
    claim_parser.add_argument("--beads-dir", default=default_beads, dest="beads_dir")

    complete_parser = subparsers.add_parser("complete", help="mark an in_progress bead as review")
    complete_parser.add_argument("bead_id", help="bead id to complete, e.g. FACTORY-007")
    complete_parser.add_argument("--beads-dir", default=default_beads, dest="beads_dir")

    done_parser = subparsers.add_parser("done", help="mark a review bead as done")
    done_parser.add_argument("bead_id", help="bead id to mark done, e.g. FACTORY-007")
    done_parser.add_argument("--beads-dir", default=default_beads, dest="beads_dir")

    if not args:
        args = ["validate"]

    parsed = parser.parse_args(args)
    beads_dir = Path(parsed.beads_dir)

    if parsed.command == "validate":
        return _validate_command(beads_dir)
    if parsed.command == "list":
        return _list_command(beads_dir, parsed.json_output)
    if parsed.command == "ready":
        return _ready_command(beads_dir, parsed.json_output)
    if parsed.command == "claim":
        return _claim_command(beads_dir, parsed.bead_id, parsed.assignee)
    if parsed.command == "complete":
        return _complete_command(beads_dir, parsed.bead_id)
    if parsed.command == "done":
        return _done_command(beads_dir, parsed.bead_id)

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

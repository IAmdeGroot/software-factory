"""CLI entry point for bead tools."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from harness.beads.backlog import default_backlog_path, sync_backlog
from harness.beads.claim import ClaimError, claim_bead, claim_next
from harness.beads.listing import (
    build_ready_queue,
    build_review_queue,
    build_status_summary,
    format_ready_text,
    format_review_text,
    format_summary_text,
    ready_to_json,
    review_to_json,
    summary_to_json,
)
from harness.beads.status import TransitionError, complete_bead, done_bead
from harness.beads.validate import validate_beads_dir
from harness.beads.wishes import (
    build_open_wishes,
    format_wishes_text,
    next_wish_id,
    next_wish_id_to_json,
    validate_wishes_dir,
    wishes_to_json,
)


def _default_beads_dir() -> Path:
    repo_root = Path(__file__).resolve().parents[2]
    return repo_root / "docs" / "work-graph" / "beads"


def _default_wishes_dir() -> Path:
    repo_root = Path(__file__).resolve().parents[2]
    return repo_root / "docs" / "work-graph" / "wishes"


def _validate_command(beads_dir: Path) -> int:
    result = validate_beads_dir(beads_dir)
    wishes_dir = _default_wishes_dir()
    wish_result = validate_wishes_dir(wishes_dir)
    result.errors.extend(wish_result.errors)
    if result.ok:
        bead_count = len(list(beads_dir.glob("*.md"))) if beads_dir.is_dir() else 0
        print(f"OK: {bead_count} bead(s) validated in {beads_dir}")
        if wishes_dir.is_dir():
            wish_count = len(
                [path for path in wishes_dir.glob("*.md") if path.stem.startswith("WISH-")]
            )
            print(f"OK: {wish_count} wish(es) validated in {wishes_dir}")
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


def _review_queue_command(beads_dir: Path, json_output: bool) -> int:
    review = build_review_queue(beads_dir)
    if json_output:
        print(review_to_json(review))
    else:
        print(format_review_text(review))
    return 0


def _claim_command(beads_dir: Path, bead_id: str, assignee: str) -> int:
    try:
        result = claim_bead(beads_dir, bead_id, assignee=assignee)
    except ClaimError as exc:
        print(f"Claim failed: {exc}", file=sys.stderr)
        return 1

    print(f"Claimed {result.bead_id} for {result.assignee}")
    return 0


def _next_command(beads_dir: Path, assignee: str, json_output: bool) -> int:
    try:
        result = claim_next(beads_dir, assignee=assignee)
    except ClaimError as exc:
        print(f"Next failed: {exc}", file=sys.stderr)
        return 1

    if json_output:
        print(
            json.dumps(
                {
                    "id": result.bead_id,
                    "title": result.title,
                    "assignee": result.assignee,
                },
                indent=2,
            )
        )
    else:
        print(f"Claimed {result.bead_id}: {result.title} for {result.assignee}")
    return 0


def _complete_command(beads_dir: Path, bead_id: str) -> int:
    try:
        result = complete_bead(beads_dir, bead_id)
    except TransitionError as exc:
        print(f"Complete failed: {exc}", file=sys.stderr)
        return 1

    print(f"Completed {result.bead_id} ({result.from_status} -> {result.to_status})")
    return 0


def _sync_backlog_command(beads_dir: Path, backlog_path: Path) -> int:
    path = sync_backlog(beads_dir, backlog_path)
    print(f"Synced backlog: {path}")
    return 0


def _done_command(beads_dir: Path, bead_id: str) -> int:
    try:
        result = done_bead(beads_dir, bead_id)
    except TransitionError as exc:
        print(f"Done failed: {exc}", file=sys.stderr)
        return 1

    print(f"Marked {result.bead_id} done ({result.from_status} -> {result.to_status})")
    return 0


def _wishes_command(wishes_dir: Path, json_output: bool) -> int:
    wishes = build_open_wishes(wishes_dir)
    if json_output:
        print(wishes_to_json(wishes))
    else:
        print(format_wishes_text(wishes))
    return 0


def _next_wish_id_command(wishes_dir: Path, json_output: bool) -> int:
    wish_id = next_wish_id(wishes_dir)
    if json_output:
        print(next_wish_id_to_json(wish_id))
    else:
        print(wish_id)
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

    review_parser = subparsers.add_parser("review-queue", help="show beads waiting for review")
    review_parser.add_argument("beads_dir", nargs="?", default=default_beads)
    review_parser.add_argument("--json", action="store_true", dest="json_output")

    claim_parser = subparsers.add_parser("claim", help="claim a ready bead")
    claim_parser.add_argument("bead_id", help="bead id to claim, e.g. FACTORY-005")
    claim_parser.add_argument("--assignee", default="agent")
    claim_parser.add_argument("--beads-dir", default=default_beads, dest="beads_dir")

    next_parser = subparsers.add_parser("next", help="claim the first ready bead")
    next_parser.add_argument("--assignee", default="agent")
    next_parser.add_argument("--json", action="store_true", dest="json_output")
    next_parser.add_argument("--beads-dir", default=default_beads, dest="beads_dir")

    complete_parser = subparsers.add_parser("complete", help="mark an in_progress bead as review")
    complete_parser.add_argument("bead_id", help="bead id to complete, e.g. FACTORY-007")
    complete_parser.add_argument("--beads-dir", default=default_beads, dest="beads_dir")

    done_parser = subparsers.add_parser("done", help="mark a review bead as done")
    done_parser.add_argument("bead_id", help="bead id to mark done, e.g. FACTORY-007")
    done_parser.add_argument("--beads-dir", default=default_beads, dest="beads_dir")

    sync_parser = subparsers.add_parser("sync-backlog", help="regenerate backlog.md from bead files")
    sync_parser.add_argument("--beads-dir", default=default_beads, dest="beads_dir")
    sync_parser.add_argument("--backlog", default=None, dest="backlog_path")

    wishes_parser = subparsers.add_parser("wishes", help="list open wishes")
    wishes_parser.add_argument(
        "wishes_dir", nargs="?", default=str(_default_wishes_dir())
    )
    wishes_parser.add_argument("--json", action="store_true", dest="json_output")

    next_wish_parser = subparsers.add_parser(
        "next-wish-id", help="print the next unused WISH-NNN id"
    )
    next_wish_parser.add_argument(
        "wishes_dir", nargs="?", default=str(_default_wishes_dir())
    )
    next_wish_parser.add_argument("--json", action="store_true", dest="json_output")

    if not args:
        args = ["validate"]

    parsed = parser.parse_args(args)
    beads_dir = Path(parsed.beads_dir) if hasattr(parsed, "beads_dir") else _default_beads_dir()

    if parsed.command == "validate":
        return _validate_command(beads_dir)
    if parsed.command == "list":
        return _list_command(beads_dir, parsed.json_output)
    if parsed.command == "ready":
        return _ready_command(beads_dir, parsed.json_output)
    if parsed.command == "review-queue":
        return _review_queue_command(beads_dir, parsed.json_output)
    if parsed.command == "claim":
        return _claim_command(beads_dir, parsed.bead_id, parsed.assignee)
    if parsed.command == "next":
        return _next_command(beads_dir, parsed.assignee, parsed.json_output)
    if parsed.command == "complete":
        return _complete_command(beads_dir, parsed.bead_id)
    if parsed.command == "done":
        return _done_command(beads_dir, parsed.bead_id)
    if parsed.command == "sync-backlog":
        backlog_path = (
            Path(parsed.backlog_path)
            if parsed.backlog_path
            else default_backlog_path(beads_dir)
        )
        return _sync_backlog_command(beads_dir, backlog_path)
    if parsed.command == "wishes":
        return _wishes_command(Path(parsed.wishes_dir), parsed.json_output)
    if parsed.command == "next-wish-id":
        return _next_wish_id_command(Path(parsed.wishes_dir), parsed.json_output)

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

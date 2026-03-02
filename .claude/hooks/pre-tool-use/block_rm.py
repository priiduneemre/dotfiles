#!/usr/bin/env python3
"""PreToolUse hook: blocks any rm shell operation."""

import json
import re
import sys
from typing import Any, Dict, TextIO

RM_PATTERN: re.Pattern[str] = re.compile(r"\brm\b")


def main(stdin: TextIO) -> None:
    """Read stdin, check for rm, and emit a deny response if matched."""
    command: str = get_bash_cmd(json.load(stdin))
    if contains_rm(command):
        print(json.dumps(get_deny_payload(command)))


def get_bash_cmd(payload: Dict[str, Any]) -> str:
    """Extract the Bash command from the hook payload."""
    return payload.get("tool_input", {}).get("command", "")


def contains_rm(command: str) -> bool:
    """Check if the command contains rm operations."""
    return bool(RM_PATTERN.search(command))


def get_deny_payload(command: str) -> Dict[str, Any]:
    """Build a deny output payload with respective reason."""
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": (
                f"rm is blocked. Use trash/safe-delete instead: {command}"
            ),
        }
    }


if __name__ == "__main__":
    main(sys.stdin)

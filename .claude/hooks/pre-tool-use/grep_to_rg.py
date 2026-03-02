#!/usr/bin/env python3
"""PreToolUse hook: rewrites grep calls to rg (ripgrep)."""

import json
import re
import sys
from typing import Any, Dict, Optional, TextIO

GREP_PATTERN: re.Pattern[str] = re.compile(r"(?<![a-zA-Z0-9_/-])grep\b")


def main(stdin: TextIO) -> None:
    """Read stdin, rewrite grep to rg, and emit a response if changed."""
    tool_input: Dict[str, Any] = json.load(stdin).get("tool_input", {})
    if payload := get_updated_payload(tool_input):
        print(json.dumps(payload))


def get_updated_payload(tool_input: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Get an updated payload if the command was replaced, otherwise None."""
    command: str = tool_input.get("command", "")
    rg_command: str = GREP_PATTERN.sub("rg", command)
    if command != rg_command:
        return get_allow_payload(rg_command, tool_input)
    return None


def get_allow_payload(command: str, tool_input: Dict[str, Any]) -> Dict[str, Any]:
    """Build an allow output payload with the given command."""
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "allow",
            "updatedInput": {**tool_input, "command": command},
        }
    }


if __name__ == "__main__":
    main(sys.stdin)

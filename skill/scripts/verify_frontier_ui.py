#!/usr/bin/env python3
"""Warning-only static pass for Frontier UI Forge examples."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

COLOR_RE = re.compile(r"(?<![-\w])#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})(?![\w-])")
EMOJI_RE = re.compile("[\U0001F300-\U0001FAFF]")
IMG_RE = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
FOCUS_RE = re.compile(r":focus-visible|:focus\b", re.IGNORECASE)


def files_for(root: Path) -> list[Path]:
    suffixes = {".html", ".htm", ".css", ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte"}
    return [p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in suffixes and "node_modules" not in p.parts]


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a small warning-only Frontier UI static pass")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    root = args.path.resolve()
    paths = [root] if root.is_file() else files_for(root)
    if not paths:
        print("FRONTIER_UI_STATIC_FAIL: no UI source files found")
        return 2

    warnings: list[str] = []
    combined = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in paths)
    for path in paths:
        text = path.read_text(encoding="utf-8", errors="ignore")
        lowered = text.lower()
        label = str(path)
        if "transition: all" in lowered or "transition-all" in lowered:
            warnings.append(f"{label}: avoid transition: all; enumerate cheap properties")
        if "100vh" in lowered and "100dvh" not in lowered:
            warnings.append(f"{label}: 100vh found without a dynamic viewport fallback")
        if path.suffix.lower() in {".html", ".htm"}:
            for img in IMG_RE.findall(text):
                if not re.search(r"\balt\s*=", img, re.IGNORECASE):
                    warnings.append(f"{label}: image is missing alt text")
        if EMOJI_RE.search(text):
            warnings.append(f"{label}: emoji glyph found; confirm it is an intentional product choice")
        if COLOR_RE.search(text) and "--" not in text:
            warnings.append(f"{label}: raw color literal found without a visible token declaration")

    if not FOCUS_RE.search(combined):
        warnings.append("project: no :focus-visible/:focus rule found")
    if "prefers-reduced-motion" not in combined:
        warnings.append("project: no prefers-reduced-motion rule found")

    if warnings:
        print("FRONTIER_UI_STATIC_WARNINGS")
        for item in warnings:
            print(f"- {item}")
        return 1
    print("FRONTIER_UI_STATIC_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

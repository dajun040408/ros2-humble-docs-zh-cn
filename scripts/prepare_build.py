#!/usr/bin/env python3
"""Prepare an upstream ROS 2 Humble Sphinx checkout with local zh-CN overlays."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"Cannot patch upstream conf.py: pattern not found for {label}")
    return text.replace(old, new, 1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--upstream", type=Path, required=True)
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    upstream = args.upstream.resolve()
    source_overlay = repo_root / "source"
    upstream_source = upstream / "source"
    conf_path = upstream / "conf.py"

    if not upstream_source.is_dir() or not conf_path.is_file():
        raise SystemExit(f"Not a ROS 2 documentation checkout: {upstream}")

    copied = 0
    for item in source_overlay.rglob("*"):
        if not item.is_file():
            continue
        relative = item.relative_to(source_overlay)
        target = upstream_source / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if item.resolve() != target.resolve():
            shutil.copy2(item, target)
        copied += 1

    conf = conf_path.read_text(encoding="utf-8")
    conf = replace_once(conf, "project = 'ROS 2 documentation'",
                        "project = 'ROS 2 Humble 中文文档'", "project")
    conf = replace_once(conf, "author = 'Open Robotics'",
                        "author = 'ROS 2 社区中文翻译贡献者'", "author")
    conf = replace_once(conf, "language = 'en'", "language = 'zh_CN'", "language")
    conf = replace_once(conf, "'github_user': 'ros2'",
                        "'github_user': 'dajun040408'", "GitHub owner")
    conf = replace_once(conf, "'github_repo': 'ros2_documentation'",
                        "'github_repo': 'ros2-humble-docs-zh-cn'", "GitHub repo")
    conf = replace_once(conf, "'github_version': 'rolling/source/'",
                        "'github_version': 'main/source/'", "GitHub source link")
    conf = replace_once(conf, "html_baseurl = 'https://docs.ros.org/en'",
                        "html_baseurl = 'https://dajun040408.github.io/ros2-humble-docs-zh-cn/'",
                        "HTML base URL")
    conf = replace_once(conf, "ogp_site_url = 'https://docs.ros.org/en/humble/'",
                        "ogp_site_url = 'https://dajun040408.github.io/ros2-humble-docs-zh-cn/'",
                        "OpenGraph URL")
    conf = replace_once(conf, "ogp_site_name = 'ROS 2 Documentation'",
                        "ogp_site_name = 'ROS 2 Humble 中文文档'", "OpenGraph site name")

    conf = re.sub(
        r"macros = \{\n.*?\n\}",
        "macros = {\n"
        "    'DISTRO': 'humble',\n"
        "    'DISTRO_TITLE': 'Humble',\n"
        "    'DISTRO_TITLE_FULL': 'Humble Hawksbill',\n"
        "    'REPOS_FILE_BRANCH': 'humble',\n"
        "}",
        conf,
        count=1,
        flags=re.S,
    )
    if "'DISTRO': 'humble'" not in conf:
        raise RuntimeError("Failed to set Humble build macros")

    conf += "\nhtml_js_files = ['zh-search.js']\nhtml_css_files = ['zh-search.css']\nhtml_extra_path = ['search-zh.html']\n"
    conf_path.write_text(conf, encoding="utf-8")
    print(f"Overlay files copied: {copied}")
    print("Sphinx configuration patched for zh_CN and ROS 2 Humble.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

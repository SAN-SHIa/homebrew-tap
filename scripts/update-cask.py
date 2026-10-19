#!/usr/bin/env python3
"""Update the fixed SwiftCull version and verify the upstream asset digest."""

import hashlib
import json
import os
from pathlib import Path
import re
import urllib.request

API = "https://api.github.com/repos/SAN-SHIa/SwiftCull/releases/latest"


def main():
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "SwiftCull-Homebrew-Tap"}
    token = os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = "Bearer " + token
    request = urllib.request.Request(API, headers=headers)
    with urllib.request.urlopen(request, timeout=60) as response:
        release = json.load(response)
    tag = release["tag_name"]
    if not re.fullmatch(r"v(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)", tag):
        raise ValueError("Expected a stable vMAJOR.MINOR.PATCH release")
    if release["draft"] or release["prerelease"]:
        raise ValueError("The selected release is not stable")
    assets = [asset for asset in release["assets"] if asset["name"] == "SwiftCull.dmg"]
    if len(assets) != 1:
        raise ValueError("Expected exactly one SwiftCull.dmg asset")
    asset = assets[0]
    url = f"https://github.com/SAN-SHIa/SwiftCull/releases/download/{tag}/SwiftCull.dmg"
    if asset["browser_download_url"] != url:
        raise ValueError("Unexpected upstream download URL")
    digest = hashlib.sha256()
    download = urllib.request.Request(url, headers={"User-Agent": "SwiftCull-Homebrew-Tap"})
    with urllib.request.urlopen(download, timeout=120) as response:
        while chunk := response.read(1024 * 1024):
            digest.update(chunk)
    checksum = digest.hexdigest()
    if asset.get("digest") != "sha256:" + checksum:
        raise ValueError("Downloaded asset does not match its GitHub SHA-256 digest")
    path = Path(__file__).resolve().parents[1] / "Casks" / "swiftcull.rb"
    previous = path.read_text()
    updated, versions = re.subn(r'^  version "[^"]+"$', f'  version "{tag[1:]}"', previous, flags=re.M)
    updated, hashes = re.subn(r'^  sha256 "[^"]+"$', f'  sha256 "{checksum}"', updated, flags=re.M)
    if versions != 1 or hashes != 1:
        raise ValueError("Expected exactly one version and one sha256 declaration")
    if updated == previous:
        print(f"SwiftCull {tag} is already current")
        return
    path.write_text(updated)
    print(f"Updated SwiftCull to {tag}; sha256 {checksum}")


if __name__ == "__main__":
    main()

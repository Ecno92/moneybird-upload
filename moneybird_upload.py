#!/usr/bin/env python3
import json
import os
import sys
import httpx
import datetime
from urllib.parse import unquote, urlparse
from pathlib import Path


def get_paths(selected_uris):
    uris = selected_uris.splitlines()
    paths = [Path(unquote(urlparse(uri).path)) for uri in uris]
    return paths


def current_datetime_string():
    return (
        datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="milliseconds")[
            :23
        ]
        + "Z"
    )


def read_settings():
    with open(Path(__file__).resolve().parent / "settings", mode="r") as settings_file:
        content = settings_file.read()
        return content.splitlines()


class MoneyBirdApiClient:
    def __init__(self, token, administration):
        self.token = token

        self.client = httpx.Client(
            base_url=f"https://moneybird.com/api/v2/{administration}",
            headers={"Authorization": f"Bearer {self.token}"},
        )

    def create_typeless_document(self, reference):
        response = self.client.post(
            "/documents/typeless_documents.json",
            json={"typeless_document": {"reference": reference}},
        )
        return response.json()["id"]

    def upload_typeless_document_attachement(self, document_id, path):
        response = self.client.post(
            f"/documents/typeless_documents/{document_id}/attachments.json",
            files={"file": open(path, "rb")},
        )
        response.raise_for_status()


def main():
    token, administration = read_settings()
    client = MoneyBirdApiClient(token, administration)
    paths = get_paths(os.environ["NAUTILUS_SCRIPT_SELECTED_URIS"])

    for path in paths:
        # First we need to create an empty, typeless document.
        document_id = client.create_typeless_document(reference=path.name)

        # Now we can read the file and post the contents.
        client.upload_typeless_document_attachement(document_id, path)


if __name__ == "__main__":
    main()

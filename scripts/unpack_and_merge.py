import os
import json
import zipfile
from pathlib import Path

VERSIONS_DIR = Path("versions")
MERGED_DIR = Path("merged")
METADATA_FILE = VERSIONS_DIR / "metadata.json"
TARGET_DIRS = {"taxonomy", "samples"}

def load_metadata():
    with open(METADATA_FILE, encoding="utf-8") as f:
        return {entry["filename"]: entry["source_url"] for entry in json.load(f)}

def unpack_zip(zip_path, metadata):
    filename = zip_path.name
    source_url = metadata.get(filename)

    if not source_url:
        print(f"[警告] metadata.json に未登録の ZIP: {filename}")
    else:
        print(f"[展開] {filename}（出典: {source_url}）")

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for member in zip_ref.infolist():
            parts = Path(member.filename).parts
            for i, part in enumerate(parts):
                if part in TARGET_DIRS:
                    relative_path = Path(*parts[i:])  # 「samples」または「taxonomy」から下を展開
                    target_path = MERGED_DIR / relative_path
                    if member.is_dir():
                        target_path.mkdir(parents=True, exist_ok=True)
                    else:
                        target_path.parent.mkdir(parents=True, exist_ok=True)
                        with zip_ref.open(member) as source, open(target_path, "wb") as target:
                            target.write(source.read())
                    break  # 最初に見つけた対象ディレクトリで処理終了

def main():
    metadata = load_metadata()
    MERGED_DIR.mkdir(exist_ok=True)
    for sub in TARGET_DIRS:
        (MERGED_DIR / sub).mkdir(exist_ok=True)

    for zip_file in sorted(VERSIONS_DIR.glob("*.zip")):
        unpack_zip(zip_file, metadata)

    print("\n✅ 統合完了：merged/taxonomy/ および merged/samples/ に展開されました")

if __name__ == "__main__":
    main()
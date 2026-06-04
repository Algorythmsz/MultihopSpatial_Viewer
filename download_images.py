"""
Download the 60 sample images used in index.html from the MultihopSpatial HuggingFace dataset.
Usage: python download_images.py
       python download_images.py --token hf_xxx   # if repo requires auth
"""
import argparse
import os
from pathlib import Path

from huggingface_hub import hf_hub_download

REPO_ID = "etri-vilab/MultihopSpatial"
REPO_TYPE = "dataset"
IMAGES_DIR = Path(__file__).parent / "images"

REQUIRED_IMAGES = [
    "000000008170.jpg", "000000011271.jpg", "000000016823.jpg", "000000023723.jpg",
    "000000037456.jpg", "000000048001.jpg", "000000051203.jpg", "000000052030.jpg",
    "000000053037.jpg", "000000054671.jpg", "000000060519.jpg", "000000062608.jpg",
    "000000083369.jpg", "000000085803.jpg", "000000086514.jpg", "000000092957.jpg",
    "000000096973.jpg", "000000100558.jpg", "000000105520.jpg", "000000114519.jpg",
    "000000116268.jpg", "000000117400.jpg", "000000132669.jpg", "000000174896.jpg",
    "000000177258.jpg", "000000190705.jpg", "000000193213.jpg", "000000205947.jpg",
    "000000214024.jpg", "000000244844.jpg", "000000247680.jpg", "000000250790.jpg",
    "000000254917.jpg", "000000256824.jpg", "000000261858.jpg", "000000263323.jpg",
    "000000277150.jpg", "000000279199.jpg", "000000281970.jpg", "000000293805.jpg",
    "000000322634.jpg", "000000336182.jpg", "000000357604.jpg", "000000364032.jpg",
    "000000385001.jpg", "000000385150.jpg", "000000417373.jpg", "000000446956.jpg",
    "000000463132.jpg", "000000463498.jpg", "000000474499.jpg", "000000491888.jpg",
    "000000508741.jpg", "000000521427.jpg", "000000526737.jpg", "000000535602.jpg",
    "000000537371.jpg", "000000554238.jpg", "000000567636.jpg", "000000572732.jpg",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", default=None, help="HuggingFace access token (if needed)")
    args = parser.parse_args()

    IMAGES_DIR.mkdir(exist_ok=True)

    already = [f for f in REQUIRED_IMAGES if (IMAGES_DIR / f).exists()]
    todo = [f for f in REQUIRED_IMAGES if f not in already]

    if already:
        print(f"Already downloaded: {len(already)} / {len(REQUIRED_IMAGES)}")
    if not todo:
        print("All images present. Nothing to do.")
        return

    print(f"Downloading {len(todo)} images → {IMAGES_DIR}\n")
    failed = []
    for i, fname in enumerate(todo, 1):
        dest = IMAGES_DIR / fname
        try:
            path = hf_hub_download(
                repo_id=REPO_ID,
                repo_type=REPO_TYPE,
                filename=f"data/images/{fname}",
                token=args.token,
                local_dir=str(IMAGES_DIR.parent),
            )
            # hf_hub_download saves to local_dir/data/images/fname; move to images/fname
            src = Path(path)
            if src != dest:
                dest.write_bytes(src.read_bytes())
                src.unlink()
            print(f"  [{i:2}/{len(todo)}] ✓ {fname}")
        except Exception as e:
            print(f"  [{i:2}/{len(todo)}] ✗ {fname}  ({e})")
            failed.append(fname)

    print(f"\nDone. {len(todo) - len(failed)} downloaded, {len(failed)} failed.")
    if failed:
        print("Failed files:")
        for f in failed:
            print(f"  {f}")


if __name__ == "__main__":
    main()

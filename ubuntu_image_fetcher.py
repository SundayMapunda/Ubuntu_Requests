import requests
import os
import hashlib
from urllib.parse import urlparse
from pathlib import Path

# Constants
SAVE_DIR = "Fetched_Images"
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
VALID_IMAGE_MIME_PREFIX = "image/"

# Store image hashes to detect duplicates
downloaded_hashes = set()

def get_file_hash(content):
    return hashlib.sha256(content).hexdigest()

def sanitize_filename(url):
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename or '.' not in filename:
        filename = "downloaded_image.jpg"
    return filename

def download_image(url):
    try:
        headers = {
            "User-Agent": "UbuntuImageFetcher/1.0"
        }

        response = requests.get(url, timeout=10, headers=headers, stream=True, allow_redirects=True)
        response.raise_for_status()

        # Check Content-Type
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith(VALID_IMAGE_MIME_PREFIX):
            print(f"✗ Skipping {url}: Content-Type is not an image ({content_type})")
            return

        # Check Content-Length if present
        content_length = response.headers.get("Content-Length")
        if content_length and int(content_length) > MAX_FILE_SIZE:
            print(f"✗ Skipping {url}: File size too large ({int(content_length) / (1024*1024):.2f} MB)")
            return

        # Download image content
        content = response.content

        # Additional size check (in case Content-Length was missing or incorrect)
        if len(content) > MAX_FILE_SIZE:
            print(f"✗ Skipping {url}: Actual file size too large ({len(content) / (1024*1024):.2f} MB)")
            return

        # Check for duplicates
        content_hash = get_file_hash(content)
        if content_hash in downloaded_hashes:
            print(f"⚠ Duplicate image skipped: {url}")
            return
        downloaded_hashes.add(content_hash)

        # Save the image
        filename = sanitize_filename(url)
        save_path = os.path.join(SAVE_DIR, filename)

        # Ensure unique filename if same name exists
        base, ext = os.path.splitext(filename)
        counter = 1
        while os.path.exists(save_path):
            save_path = os.path.join(SAVE_DIR, f"{base}_{counter}{ext}")
            counter += 1

        with open(save_path, "wb") as f:
            f.write(content)

        print(f"✓ Saved: {filename} → {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Network error while fetching {url}: {e}")
    except Exception as e:
        print(f"✗ Error processing {url}: {e}")

def main():
    print("🖼️ Ubuntu Image Fetcher — Download images safely and mindfully\n")

    # Prompt for multiple comma-separated URLs in a single line
    url_input = input("Enter one or more image URLs (comma-separated): ").strip()
    if not url_input:
        print("No URLs provided. Exiting.")
        return

    # Split and clean the URLs
    urls = [url.strip() for url in url_input.split(",") if url.strip()]

    if not urls:
        print("No valid URLs provided. Exiting.")
        return

    # Create directory if needed
    os.makedirs(SAVE_DIR, exist_ok=True)

    # Download each image
    for url in urls:
        download_image(url)

    print("\n📦 All done. Images saved in 'Fetched_Images'.")
    print("🤝 Connection strengthened. Community enriched.")

if __name__ == "__main__":
    main()


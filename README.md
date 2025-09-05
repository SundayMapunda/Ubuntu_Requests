# 🖼️ Ubuntu Image Fetcher

A mindful, community-oriented Python tool to safely fetch and organize images from the web. Built with simplicity, safety, and sharing in mind — in the spirit of Ubuntu.

---

## 🌍 Description

**Ubuntu Image Fetcher** allows users to download one or more images from the internet using direct URLs. It stores them in a dedicated folder, ensures that downloads are secure, prevents duplicates, and gracefully handles errors — all while encouraging responsible interaction with the wider web community.

---

## 🚀 Features

- ✅ Accepts multiple comma-separated image URLs
- ✅ Creates a `Fetched_Images` directory automatically
- ✅ Downloads and saves images in binary mode
- ✅ Prevents duplicate downloads using SHA-256 hashing
- ✅ Checks for valid image MIME types (`image/jpeg`, `image/png`, etc.)
- ✅ Skips downloads exceeding 10 MB
- ✅ Graceful handling of network and HTTP errors
- ✅ Auto-renames files to avoid overwrites
- ✅ Uses headers like `Content-Type` and `Content-Length` responsibly

---

## 📦 Requirements

- Python 3.x
- [`requests`](https://pypi.org/project/requests/)

Install dependencies:

```bash
pip install requests

## 🧪 Usage
## 📁 Run the script
python3 ubuntu_image_fetcher.py

## ⌨️ Input

Paste one or more comma-separated image URLs (direct links only):
https://images.unsplash.com/photo-1506744038136-46273834b3fb, https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e

## 📥 Output

Images are downloaded and saved to the Fetched_Images directory:

✓ Saved: photo-1506744038136-46273834b3fb → Fetched_Images/photo-1506744038136-46273834b3fb.jpg
✓ Saved: photo-1529626455594-4ff0802cfb7e → Fetched_Images/photo-1529626455594-4ff0802cfb7e.jpg

## 🌱 Ubuntu Principles in Practice
Principle	Implementation
Community	Connects with the broader web to retrieve visual content
Respect	Handles failures and unknowns gracefully, without crashing
Sharing	Organizes content into a reusable and shareable folder
Practicality	Solves a common task in a lightweight and scriptable way

## 🛡️ Security Notes

Validates Content-Type to ensure it's an image

Enforces a maximum image size (10MB)

Uses hashed content to detect and prevent duplicates

Does not follow suspicious redirects blindly


## ❤️ Inspired by Ubuntu

"I am because we are." This script aims to strengthen our connection through respectful technology and shared resources.

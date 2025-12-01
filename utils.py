import os

def ensure_dir(path):
    """Create directory if not exists."""
    if not os.path.exists(path):
        os.makedirs(path)

def list_folders(base_path="data"):
    """List all folders inside the base data directory."""
    if not os.path.exists(base_path):
        return []

    return [
        f for f in os.listdir(base_path)
        if os.path.isdir(os.path.join(base_path, f))
    ]

def list_pdfs(folder, base_path="data"):
    """List all PDF files inside the selected folder."""
    folder_path = os.path.join(base_path, folder)

    if not os.path.exists(folder_path):
        return []

    return [
        f for f in os.listdir(folder_path)
        if f.lower().endswith(".pdf")
    ]

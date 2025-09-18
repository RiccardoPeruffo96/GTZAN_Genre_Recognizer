import os

def adapt_path(x: str) -> str:
    """Adapt a path string to the current OS."""
    if os.name == "nt":  # Windows
        return x.replace("/", "\\")
    else:  # POSIX (Linux, macOS, etc.)
        return x.replace("\\", "/")

def check_os() -> tuple[bool, str]:
    """Check the current operating system and return a tuple (is_recognized, os_name)."""
    if os.name == 'nt':  # Windows
        return True, "Windows"
    if os.name == 'posix':  # Linux or Mac
        return True, "Linux"
    return False, "OS not recognized"

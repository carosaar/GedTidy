import subprocess

def write_version_file():
    try:
        version = subprocess.check_output(
            ["git", "describe", "--tags"],
            stderr=subprocess.STDOUT
        ).decode().strip()
    except Exception:
        version = "unknown"

    with open("version.txt", "w") as f:
        f.write(version)

if __name__ == "__main__":
    write_version_file()
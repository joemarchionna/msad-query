from typing import Tuple
import subprocess


def runPS(command: str) -> Tuple[bool, str]:
    try:
        # Use 'pwsh' for PowerShell Core or 'powershell.exe' for Windows PowerShell
        # -NoProfile prevents loading the user profile, making execution faster
        # -Command or -c specifies the command to run
        result = subprocess.run(
            ["powershell.exe", "-NoProfile", "-Command", command],
            capture_output=True,
            text=True,  # Decode stdout/stderr as text
            check=True,  # Raise an exception if the command returns a non-zero exit code
        )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

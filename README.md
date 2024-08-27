This repository contains a Python-based solver for challenges encountered on the Winamax sports betting application. The solver is designed through reverse engineering of the application's JavaScript files.

### How It Works

1. **GUID Generation**: A unique identifier (GUID) is generated using random hexadecimal values.
2. **Hashing**: The GUID is hashed using the SHA-256 algorithm to produce a secure hash.
3. **Base64 Encoding**: The resulting hash is then encoded into Base64 format for compatibility and ease of use.

The main components of the script include:
- **`convert_to_base64(string)`**: Converts a given string to Base64 encoding.
- **`hash256(challenge)`**: Computes the SHA-256 hash of a challenge string.
- **`S4()`**: Generates a 4-character hexadecimal string.
- **`guid()`**: Assembles an 8-segment GUID from hexadecimal strings.

The script prints out the GUID, its SHA-256 hash, and the Base64-encoded hash, demonstrating how the challenge is solved.

Any Question/Help? Join my [discord](https://discord.gg/uPP3SyRymP)

import re
import sys
import os

def read_savefile(filepath):
    with open(filepath, 'rb') as f:
        return f.read()

def write_savefile(filepath, data):
    with open(filepath, 'wb') as f:
        f.write(data)

def simple_additive_checksum(data: bytes) -> int:
    total = sum(data) % 10_000_000
    adjusted = (total - 10) % 10_000_000
    return adjusted

def patch_save(input_file: str):
    # Read save data
    data = read_savefile(input_file)

    # Remove existing checksum
    stripped_data = re.sub(rb'<!--\d+-->', b'', data, count=1)

    # Calculate new checksum
    checksum = simple_additive_checksum(stripped_data)
    new_comment = f"<!--{checksum}-->".encode()

    # Insert new checksum at the top of the file
    patched_data = new_comment + stripped_data

    # Save patched file
    base, ext = os.path.splitext(input_file)
    output_file = f"{base}-patched{ext}"
    write_savefile(output_file, patched_data)

    print(f"[✔] Patched file saved as: {output_file}")
    print(f"[ℹ] New checksum: {checksum}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python MTP.py <savefile.xml>")
        sys.exit(1)

    patch_save(sys.argv[1])

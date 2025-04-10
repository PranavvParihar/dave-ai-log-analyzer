import os
import subprocess
import platform
from pathlib import Path

IS_WINDOWS = platform.system() == "Windows"

def find_txt_files(directory):
    directory = str(directory)
    if IS_WINDOWS:
        txt_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".txt"):
                    txt_files.append(str(Path(root) / file))
        return txt_files
    else:
        try:
            result = subprocess.run(['find', directory, '-type', 'f', '-name', '*.txt'],
                                    capture_output=True, text=True, check=True)
            return result.stdout.strip().split('\n') if result.stdout else []
        except subprocess.CalledProcessError as e:
            print(f"[!] Error finding .txt files: {e}")
            return []

def count_error_lines(filepath):
    error_count, total_lines = 0, 0
    try:
        with open(filepath, 'r', errors='ignore') as f:
            for line in f:
                total_lines += 1
                if 'error' in line.lower():
                    error_count += 1
    except Exception as e:
        print(f"[!] Error reading file {filepath}: {e}")
    return error_count, total_lines

def get_wc_line_count(filepath):
    if IS_WINDOWS:
        return -1  # Not available
    try:
        result = subprocess.run(['wc', '-l', filepath], capture_output=True, text=True, check=True)
        return int(result.stdout.strip().split()[0])
    except Exception as e:
        print(f"[!] Error using wc on file {filepath}: {e}")
        return -1

def write_summary(file_summaries, output_path):
    with open(output_path, 'w') as f:
        for file, error_count, py_count, wc_count in file_summaries:
            f.write(f"File: {file}\n")
            f.write(f"Error Count: {error_count}\n")
            if wc_count != -1 and py_count != wc_count:
                f.write(f"Line Count Mismatch: Python={py_count}, wc={wc_count}\n")
            f.write("\n")

def create_archive(files, output_dir, archive_name="logs_archive.tar.gz"):
    if IS_WINDOWS:
        print("[!] Skipping archive creation: 'tar' not available on Windows. To generate 'tar' run it on Linux")
        return
    try:
        temp_dir = Path(files[0]).parent.resolve()
        os.chdir(temp_dir)
        relative_files = [os.path.basename(f) for f in files]
        archive_path = output_dir / archive_name
        subprocess.run(['tar', '-czf', str(archive_path)] + relative_files, check=True)
        print(f"[+] Archive created: {archive_path}")
    except Exception as e:
        print(f"[!] Error creating archive: {e}")

def main():
    directory_input = input("Enter the full path to the directory (e.g., /home/ubuntu/logs): ").strip()
    directory = Path(directory_input).resolve()

    if not directory.is_dir():
        print("[!] Invalid directory path.")
        return

    print("[*] Searching for .txt files...")
    txt_files = find_txt_files(directory)

    if not txt_files:
        print("[!] No .txt files found in the specified directory.")
        return

    summaries = []
    for file in txt_files:
        error_count, py_count = count_error_lines(file)
        wc_count = get_wc_line_count(file)
        summaries.append((file, error_count, py_count, wc_count))

    output_dir = Path(__file__).parent.resolve()
    summary_path = output_dir / "summary.txt"
    write_summary(summaries, summary_path)
    print(f"[+] Summary written to {summary_path}")

    create_archive(txt_files, output_dir)

if __name__ == "__main__":
    main()

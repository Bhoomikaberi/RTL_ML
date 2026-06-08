import os
import csv
import re
import subprocess

RTL_ROOT = "rtl_dataset"

rows = []

for root, dirs, files in os.walk(RTL_ROOT):

    for file in files:

        if file.endswith(".v"):

            filepath = os.path.join(root, file)

            print(f"\nProcessing: {file}")

            script = f"""
            read_verilog {filepath}
            synth
            stat
            """

            result = subprocess.run(
                ["yosys", "-p", script],
                capture_output=True,
                text=True
            )

            output = result.stdout

            # DEBUG: print last part of Yosys output
            print("\n===== YOSYS OUTPUT =====")
            print(output[-1500:])
            print("========================\n")

            # Try multiple regex patterns
            cell_count = 0
            wire_count = 0

            patterns_cells = [
                r"Number of cells:\s+(\d+)",
                r"(\d+)\s+cells"
            ]

            patterns_wires = [
                r"Number of wires:\s+(\d+)",
                r"(\d+)\s+wires"
            ]

            for pattern in patterns_cells:
                match = re.search(pattern, output)
                if match:
                    cell_count = int(match.group(1))
                    break

            for pattern in patterns_wires:
                match = re.search(pattern, output)
                if match:
                    wire_count = int(match.group(1))
                    break

            print(f"Cells: {cell_count}")
            print(f"Wires: {wire_count}")

            rows.append({
                "filename": file,
                "cell_count": cell_count,
                "wire_count": wire_count
            })

os.makedirs("dataset", exist_ok=True)

with open("dataset/yosys_stats.csv", "w", newline="") as f:

    writer = csv.DictWriter(
        f,
        fieldnames=[
            "filename",
            "cell_count",
            "wire_count"
        ]
    )

    writer.writeheader()
    writer.writerows(rows)

print("\nDone!")
print("Created: dataset/yosys_stats.csv")
import os
import re
import math
import pandas as pd

RTL_ROOT = "rtl_dataset"

rows = []

for root, dirs, files in os.walk(RTL_ROOT):

    for file in files:

        if file.endswith(".v"):

            filepath = os.path.join(root, file)

            with open(filepath, "r") as f:
                code = f.read()

            # ----------------------------
            # Width Extraction
            # ----------------------------

            widths = re.findall(r'\[(\d+):0\]', code)

            if widths:
                width = max(int(w) + 1 for w in widths)
            else:
                width = 1

            # ----------------------------
            # Fix mux widths
            # ----------------------------

            if file.startswith("mux2"):
                width = 2

            elif file.startswith("mux4"):
                width = 4

            elif file.startswith("mux8"):
                width = 8

            elif file.startswith("mux16"):
                width = 16

            # ----------------------------
            # Arithmetic Operators
            # ----------------------------

            num_add = code.count('+')
            num_sub = code.count('-')
            num_mul = code.count('*')

            # ----------------------------
            # Logic Operators
            # ----------------------------

            num_and = code.count('&')
            num_or = code.count('|')
            num_xor = code.count('^')

            # ----------------------------
            # RTL Constructs
            # ----------------------------

            num_assign = len(
                re.findall(
                    r'\bassign\b',
                    code
                )
            )

            num_always = len(
                re.findall(
                    r'\balways\b',
                    code
                )
            )

            num_case = len(
                re.findall(
                    r'\bcase\b',
                    code
                )
            )

            num_if = len(
                re.findall(
                    r'\bif\b',
                    code
                )
            )

            num_modules = len(
                re.findall(
                    r'\bmodule\b',
                    code
                )
            )

            # ----------------------------
            # Logic Depth Estimation
            # ----------------------------

            depth = math.ceil(
                math.log2(width)
            ) + 1

            rows.append({

                "filename": file,

                "width": width,

                "depth": depth,

                "num_add": num_add,

                "num_sub": num_sub,

                "num_mul": num_mul,

                "num_and": num_and,

                "num_or": num_or,

                "num_xor": num_xor,

                "num_assign": num_assign,

                "num_always": num_always,

                "num_case": num_case,

                "num_if": num_if,

                "num_modules": num_modules

            })

df = pd.DataFrame(rows)

os.makedirs(
    "dataset",
    exist_ok=True
)

df.to_csv(
    "dataset/rtl_features.csv",
    index=False
)

print(df.to_string())

print(
    "\nTotal RTL Files =",
    len(df)
)

print(
    "\nrtl_features.csv generated successfully!"
)
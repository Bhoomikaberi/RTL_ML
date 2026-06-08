import re

def parse_verilog(code):

    return {
        "num_add": len(re.findall(r"\+", code)),
        "num_sub": len(re.findall(r"\-", code)),
        "num_and": len(re.findall(r"\&", code)),
        "num_or": len(re.findall(r"\|", code)),
        "num_xor": len(re.findall(r"\^", code))
    }
import os

os.makedirs("generated", exist_ok=True)

widths = [4,8,16,32,64]

for width in widths:

    code = f"""
module adder_{width}(
input [{width-1}:0] a,
input [{width-1}:0] b,
output [{width-1}:0] sum
);

assign sum = a + b;

endmodule
"""

    with open(f"generated/adder_{width}.v","w") as f:
        f.write(code)

print("Generated RTL files")
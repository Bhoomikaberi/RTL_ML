import subprocess

def synthesize(file):

    cmd = f"""
    read_verilog {file}
    synth
    stat
    """

    subprocess.run(
        ["yosys","-p",cmd]
    )
import os, argparse, textwrap
CASES = {"00":"Do nothing","01":"Flip (X)","10":"Twist (Z)","11":"Flip then Twist (X then Z)"}

def make(outdir="teleport_class_set", pairs=12):
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir,"_TEACHER_SUMMARY.txt"),"w") as t:
        t.write("Teleportation case legend:\n")
        for k,v in CASES.items(): t.write(f"  {k} → {v}\n")
    for i in range(1, pairs+1):
        pair = f"pair{i:02d}"
        common = textwrap.dedent(f"""
        Teleportation — Team {pair}
        Steps: secret coin → Bell team → link & peek → two clues → fix → check
        Case legend: 00→none, 01→flip (X), 10→twist (Z), 11→flip+twist
        """).strip()
        for who in ["Alice","Bob"]:
            with open(os.path.join(outdir,f"{pair}_{who}.txt"),"w") as f:
                f.write(common + "\n\nNotes:\n- Secret choice (0 / 1 / mix-H): ______\n- Clues (two bits): __ __\n- Fix used: ______\n- Did q2 match? Yes/No. Why?\n")
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--pairs", type=int, default=12)
    ap.add_argument("--outdir", default="teleport_class_set")
    args = ap.parse_args()
    make(args.outdir, args.pairs)

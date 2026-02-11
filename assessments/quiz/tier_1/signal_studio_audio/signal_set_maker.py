import os, wave, struct, random, math, argparse, textwrap

def gen_tone(path, seconds=1.6, freq=660.0, rate=22050, noise=0.0, seed=42):
    random.seed(seed)
    N = int(seconds * rate)
    amp = 16000
    with wave.open(path, "w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate)
        frames = []
        for i in range(N):
            t = i / rate
            s = math.sin(2*math.pi*freq*t)
            if noise > 0.0:
                s += noise * (2*random.random()-1)
            s = max(-1.0, min(1.0, s))
            frames.append(struct.pack("<h", int(amp*s)))
        w.writeframes(b"".join(frames))

def main():
    ap = argparse.ArgumentParser(description="Make clean/noisy WAVs and a simple worksheet stub.")
    ap.add_argument("--outdir", default="signal_set")
    ap.add_argument("--seconds", type=float, default=1.6)
    ap.add_argument("--freq", type=float, default=660.0)
    ap.add_argument("--noise", type=float, default=0.35)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    clean = os.path.join(args.outdir, "clean.wav")
    noisy = os.path.join(args.outdir, "noisy.wav")

    gen_tone(clean, seconds=args.seconds, freq=args.freq, noise=0.0, seed=args.seed)
    gen_tone(noisy, seconds=args.seconds, freq=args.freq, noise=args.noise, seed=args.seed+1)

    with open(os.path.join(args.outdir, "worksheet_stub.txt"), "w", encoding="utf-8") as f:
        f.write(textwrap.dedent("""\
        Signal Studio — Class Set
        Files: clean.wav, noisy.wav
        Student tasks: Listen → Try Repeat & Stretch → Record SAME/DIFFERENT → Explain.
        """))

    print("Wrote:", clean, "and", noisy, "in", os.path.abspath(args.outdir))

if __name__ == "__main__":
    main()

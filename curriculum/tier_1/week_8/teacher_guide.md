# Teacher Guide — Week 8 (Tier 1) Secret Code Post

## Goal

Students see that:

- Two people can build a **shared secret key** by:
  - choosing random "views" (colors),
  - later comparing notes,
  - and keeping only **matching** positions.
- If someone tries to eavesdrop, it tends to **create more mismatches**, which we can notice.

This is a story version of **BB84 Quantum Key Distribution**.

## Materials

- Secret Code sheets (one per pair) with:
  - Row for Sender colors (B / R),
  - Row for Sender bits (0 / 1),
  - Row for Receiver colors (B / R),
  - A "Shared Key" row,
  - Space for decoded message or drawing.
- A simple code dictionary for decoding pairs of bits, for example:
  - 00 → S
  - 01 → U
  - 10 → N
  - 11 → ☀
- Optional: a third student or teacher acts as "Eve" the eavesdropper in Round 2.

## Flow (about 40 minutes)

1. Hook (3–5 min)  
   Story: "You want to send your friend a tiny secret postcard, but you do not fully trust the post office. How can you agree on a secret code that helps you catch sneaky listeners?"

2. Round 1 – Build a key (15 min)  
   Sender:
   - Chooses 8 random bits (0 or 1).
   - For each bit, chooses a random color: Blue (B) or Red (R).
   Receiver:
   - For each position, chooses a random color (B or R) **without seeing** the Sender's colors.
   Then compare:
   - For any position where colors match, keep that bit.
   - For positions where colors differ, cross it out.
   - The remaining bits in order form a **shared key**.

3. Round 1 – Decode a postcard (10 min)  
   - Split the shared key into pairs of bits.
   - Use the code dictionary to decode a simple "postcard" word or symbol.
   - Students draw or write their postcard at the bottom of the sheet.

4. Round 2 – Eavesdropper (10 min)  
   - Add an "Eve" who pretends to read and resend bits in the middle.
   - Her random choices will usually create extra mismatches.
   - After comparing colors, count mismatches:
     - "Number of mismatches with Eve" versus "Number without Eve" from Round 1.
   - Highlight that more mismatches can be a **warning sign**.

5. Bridge to higher tiers (2–3 min)  
   Brief explanation:
   "Upper tiers replace colors with different quantum bases and use math to prove that an eavesdropper cannot stay hidden if they try to read the key. Today you saw the idea in a game."

Use Tier 1 language: "views", "colors", "matches and mismatches", "sneaky listener".  
Do not use heavy algebra or matrix language with this group.

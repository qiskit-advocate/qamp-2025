# Pixel Reveal (Quantum Postcards)

**Story:** your team’s 16-bit “shared bits” act like a tiny secret key.

**Rule to decode:** go bit by bit → **same = 0**, **different = 1**.  
Use the class **CIPHER** (teacher provides) and your team’s 16-bit key to get a 16-bit **MESSAGE**.  
Color a **4×4 grid** (1 = color, 0 = blank) to reveal the icon.

Icons (4×4, choose one for class):
- Earth:  0 1 1 0 / 1 1 1 1 / 1 1 1 1 / 0 1 1 0
- Tree:   0 1 0 0 / 1 1 1 0 / 0 1 0 0 / 0 1 0 0
- Water:  1 0 1 0 / 0 1 0 1 / 1 0 1 0 / 0 1 0 1
- Sun:    0 1 0 0 / 1 1 1 1 / 0 1 0 1 / 0 1 1 0

**Teacher tip (1 min):** pick one icon, write its 16 bits as the hidden **MESSAGE**, pick any 16-bit class key, and put **CIPHER** on the board using the same/different rule. Students recover the picture with their team key.

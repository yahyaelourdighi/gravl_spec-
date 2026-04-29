# GRAVL — Grid-Advancing Register-Value Language
### Specification v0.1

GRAVL is a 2D esoteric language. A read/write head moves across a
**toroidal 16x16 grid** of 8-bit cells (all initialized to 0).
An **accumulator** (`acc`, 8-bit, init 0) handles computation.
The head starts at position **(0, 0)**, facing **East**.

---

## Instruction Set

| Char | Name         | Description                                                     |
|------|--------------|-----------------------------------------------------------------|
| `>`  | Turn Right   | Rotate direction 90° clockwise (E→S→W→N→E)                    |
| `<`  | Turn Left    | Rotate direction 90° counter-clockwise                          |
| `^`  | Reverse      | Flip direction 180°                                             |
| `@`  | Step         | Move head 1 cell forward (toroidal wrap)                        |
| `#`  | Jump         | Move head forward by `cell[y][x]` cells (toroidal wrap)         |
| `+`  | Increment    | `cell[y][x] = (cell[y][x] + 1) % 256`                         |
| `-`  | Decrement    | `cell[y][x] = (cell[y][x] - 1) % 256`                         |
| `~`  | Load         | `acc = cell[y][x]`                                              |
| `&`  | Store        | `cell[y][x] = acc`                                              |
| `*`  | XOR          | `acc = acc XOR cell[y][x]`                                      |
| `!`  | Output       | Print `chr(acc % 128)` to stdout                               |
| `[`  | Loop Start   | If `acc == 0`, jump to matching `]`                             |
| `]`  | Loop End     | If `acc != 0`, jump to matching `[`                             |

---

## Notes
- All other characters are ignored (treated as comments/whitespace)
- The grid wraps toroidally: moving East from x=15 puts you at x=0
- `#` at a cell with value 0 moves 0 steps (no-op for movement)
- Directions: East=(+x), South=(+y), West=(-x), North=(-y)

---

*This language was designed for the CSP 2026 CTF.*

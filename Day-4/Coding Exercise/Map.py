line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()

position_letter = position[0]
position_letter.lower()
alphabet_map = ["a", "b", "c"]
position_alphabet = alphabet_map.index(position_letter)
position_alphabet = position_alphabet
position_number = int(position[1]) -1
map[position_number][position_alphabet] = "X"

print(f"{line1}\n{line2}\n{line3}")

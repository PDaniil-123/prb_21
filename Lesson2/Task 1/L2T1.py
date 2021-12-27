vocebm = {'A': '•—', 'B': '—•••', 'C': '—•—•', 'D': '—••', 'E': '•', 'F': '••—•', 'G': '——•', 'H': '••••', 'I': '••', 'J': '•———', 'K': '—•—', 'L': '•—••', 'M': '——', 'N': '—•', 'O': '———', 'P': '•——•', 'Q': '——•—', 'R': '•—•', 'S': '•••', 'T': '—', 'U': '••—', 'V': '•••—', 'W': '•——', 'X': '—••—', 'Y': '—•——', 'Z': '——••'}
message = str(input())
message = message.upper()
morze=vocebm[message[0]]
for i in range(1, len(message)):
    morze=morze+vocebm[message[i]]
print(morze)

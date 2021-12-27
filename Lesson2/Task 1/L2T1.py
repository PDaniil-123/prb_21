vocebm = {'A': '•—', 'B': '—•••', 'C': '—•—•', 'D': '—••', 'E': '•', 'F': '••—•', 'G': '——•', 'H': '••••', 'I': '••', 'J': '•———', 'K': '—•—', 'L': '•—••', 'M': '——', 'N': '—•', 'O': '———', 'P': '•——•', 'Q': '——•—', 'R': '•—•', 'S': '•••', 'T': '—', 'U': '••—', 'V': '•••—', 'W': '•——', 'X': '—••—', 'Y': '—•——', 'Z': '——••'}
message = str(input())
message = message.upper()
morze=str()
for i in message:
    morze = morze+vocebm[i]
print(morze)

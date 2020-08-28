import base64
# link = 'https://forms.gle/9S22816WiBEyAMzf7'
# a = base64.b64encode(link)
# print(a)

ans = base64.b64decode(b'aHR0cHM6Ly9mb3Jtcy5nbGUvOVMyMjgxNldpQkV5QU16Zjc=')
print(ans)
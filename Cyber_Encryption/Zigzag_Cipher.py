
def zigzag_encrypt(text, rails):
    if rails == 1:
        return text

    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1  # 1 for down, -1 for up

    for char in text:
        fence[rail].append(char)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    return ''.join(''.join(row) for row in fence)

def zigzag_decrypt(cipher, rails):
    if rails == 1:
        return cipher

    # Create an empty fence
    fence = [[] for _ in range(rails)]
    n = len(cipher)

    # Determine the pattern of movement (which rail each char belongs to)
    rail_pattern = []
    rail = 0
    direction = 1
    for _ in range(n):
        rail_pattern.append(rail)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    # Count how many chars go to each rail
    counts = [rail_pattern.count(r) for r in range(rails)]

    # Fill the fence rows with the appropriate number of chars from cipher
    index = 0
    for r in range(rails):
        fence[r] = list(cipher[index:index+counts[r]])
        index += counts[r]

    # Reconstruct the original text by following the rail pattern
    result = []
    rail_indices = [0]*rails
    for r in rail_pattern:
        result.append(fence[r][rail_indices[r]])
        rail_indices[r] += 1

    return ''.join(result)




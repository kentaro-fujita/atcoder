class TomekPhone:
    def minKeystrokes(frequencies, keySizes):
        frequencies.sort(reverse=True)
        keySizes.sort(reverse=True)
        k = len(keySizes)

        keyUsed = [0] * k

        count, key = 0, 0
        for f in frequencies:
            if keyUsed[key] < keySizes[key]:
                count += f * (keyUsed[key] + 1)
                keyUsed[key] += 1
                key = (key + 1) % k
            else:
                key = (key + 1) % k
                if keyUsed[key] >= keySizes[key]:
                    return -1

        return count


print(TomekPhone.minKeystrokes([7, 3, 4, 1], [2, 2]))

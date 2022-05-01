import pickle
import random
import json

n = 1000
numMax = 100

l = []
for i in range(n):
    l.append(random.randint(0, numMax))

l = sorted(l)
jsonString = json.dumps(l)


# print(jsonString)

tree = {0: "1100001", 1: "1110101", 2: "1011100", 3: "1111011", 4: "1110001", 5: "1100101", 6: "000100", 7: "1011111", 8: "1010110", 9: "010000", 10: "0101011", 11: "0011000", 12: "001011", 13: "1001111", 14: "1001000", 15: "011100", 16: "1000100", 17: "0111011", 18: "1001101", 19: "1001011", 20: "10011100", 21: "1100011", 22: "1110110", 23: "000010", 24: "001111", 25: "1111000", 26: "101000", 27: "0110001", 28: "010001", 29: "001110", 30: "000110", 31: "010110", 32: "1011000", 33: "1101001", 34: "1111100", 35: "1011001", 36: "1001100", 37: "1101101", 38: "1101111", 39: "0101010", 40: "1110010", 41: "1111001", 42: "011010", 43: "1111111", 44: "010111", 45: "1101100", 46: "11100110", 47: "1011011", 48: "010011", 49: "000011", 50: "00011100",
        51: "010100", 52: "100001", 53: "0110000", 54: "1011101", 55: "000101", 56: "101010", 57: "000000", 58: "10011101", 59: "0001111", 60: "0111010", 61: "0011010", 62: "1001001", 63: "011011", 64: "1010111", 65: "0011011", 66: "1110111", 67: "011110", 68: "1101000", 69: "0110010", 70: "11100111", 71: "11110101", 72: "011111", 73: "1001010", 74: "11110100", 75: "1011110", 76: "1101110", 77: "001001", 78: "101001", 79: "1101010", 80: "1101011", 81: "001000", 82: "1111101", 83: "1111110", 84: "0110011", 85: "0011001", 86: "1110000", 87: "1100010", 88: "010010", 89: "1000101", 90: "1000110", 91: "000001", 92: "1000111", 93: "001010", 94: "1100100", 95: "1011010", 96: "100000", 97: "1100000", 98: "1110100", 99: "110011", 100: "00011101"}


with open('dataset/dataset_0_'+str(numMax)+'_'+str(n)+'.json', 'w') as file:
    # file.write(jsonString)
    file.write(json.dumps(tree))

    #pickle.dump(tree, file)


# data = np.random.randint(0, 100, size=n)

# df = pd.DataFrame(data, columns=['random_numbers'])


# # print(df)
# # df.to_json('dataset.json')


# sorted = df.sort_values(by=['random_numbers'], ignore_index=True)
# sorted.to_json('dataset/dataset_0_100_'+str(n) + '.json')

# print(sorted)
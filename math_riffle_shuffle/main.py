num_cards = 52
cards = [i for i in range(1, num_cards+1)]

def riffle_shuffle(input_list):
    list_halfs = split_into_two(input_list)
    shuffled_list = shuffle_combine(*list_halfs)
    return shuffled_list


def split_into_two(input_list):
    return input_list[:len(input_list)//2],input_list[len(input_list)//2:]

def shuffle_combine(*list_halfs):
    shuffle_combined_list = []
    for i in range(len(list_halfs[0])):
        shuffle_combined_list.append(list_halfs[0][i])
        shuffle_combined_list.append(list_halfs[1][i])

    return shuffle_combined_list

cards_lists = []
for i in range(10):
    cards = riffle_shuffle(cards)
    cards_lists.append(cards)

for i in range(len(cards)):
    for j in cards_lists:
        print(j[i], " "*(3-len(str(j[i]))), end="")
    print()

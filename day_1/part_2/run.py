def main():
    left_side = []
    right_side = []

    # load from file
    with open('../inputs/input.txt', 'r') as f:
        for line in f:
            left_side_item, right_side_item = line.removesuffix('\n').strip().split('   ')
            left_side.append(int(left_side_item))
            right_side.append(int(right_side_item))

    occurence_map = {}
    total_similarity_score = 0

    for i in right_side:
        if i in occurence_map:
            occurence_map[i]+=1
        else:
            occurence_map[i]=1

    for i in left_side:
        if i in occurence_map:
            num_occurences = occurence_map[i]
        else:
            num_occurences = 0

        similarity_score = int(i) * num_occurences
        total_similarity_score += similarity_score

    print('similarity score', total_similarity_score)






if __name__ == '__main__':
    main()
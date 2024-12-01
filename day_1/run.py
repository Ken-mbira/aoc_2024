def main():
    left_side = []
    right_side = []

    # load from file
    with open('input.txt', 'r') as f:
    # with open('test_input.txt', 'r') as f:
        for line in f:
            left_side_item, right_side_item = line.removesuffix('\n').strip().split('   ')
            left_side.append(int(left_side_item))
            right_side.append(int(right_side_item))

    # sort them
    left_side.sort()
    right_side.sort()

    difference_counter = 0

    for i in range(0, len(left_side)):
        difference = abs(left_side[i] - right_side[i])
        difference_counter += difference

    print('difference is ... -> ', difference_counter)

if __name__ == '__main__':
    main()
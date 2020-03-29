# 1. Составить список из чисел от 1 до 1000, которые имеют в своём составе 7.

numbers_with_7 = [number for number in range(1, 1001) if '7' in str(number)]

# 2. Взять предложение **Would it save you a lot of time if I just gave up and went mad now?**
# и сделать его же без гласных. **up:** можно оставить в виде списка слов и не собирать строку.

sentence_1 = 'Would it save you a lot of time if I just gave up and went mad now?'
words_1 = sentence_1.split()
vowels = 'a, A, o, O, e, E, i, I, u, U'
new_sentence_1 = []
for word in words_1:
    new_word = ''.join([letter for letter in word if letter not in vowels])
    new_sentence_1.append(new_word)

# 3. Для предложения **The ships hung in the sky in much the same way that bricks don't**
# составить словарь, где слову соответствует его длина.

sentence_2 = 'The ships hung in the sky in much the same way that bricks don\'t'
words_2 = sentence_2.split(' ')
dictionary = {word: len(word) for word in words_2}

# Следующие две сложные и потребуют вложенных lc:

# 4*. Для чисел от 1 до 1000 наибольшая цифра, на которую они делятся (1-9).
# по идее, тут не нужен вложенный lc, поскольку ключу будет присваиваться последнее=максимальное
# подходящее значение

max_dict = {x: y for x in range(1, 1001) for y in range(1, 10) if x % y == 0}

# если хотим не соответсвие, а просто цифру, то:

max_list = [max_dict[x] for x in range(1, 1001)]


# 5*. Список всех чисел от 1 до 1000, не имеющих делителей среди чисел от 2 до 9.

my_list = [a for a in range(1, 1001) if a not in [x for x in range(1, 1001)
                                                  for y in range(2, 10) if x % y == 0]]

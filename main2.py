import types

def flat_generator(list_of_lists):
    # Иду по айтемам в списке
    for item in list_of_lists:
        # Если айтем - список, рекурсивно запускаю flat_generator с параметром айтема
        if isinstance(item, list):
            yield from flat_generator(item)
        # Если айтем - не список, возвращаю айтем
        else:
            yield item


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

if __name__ == '__main__':
    test_2()
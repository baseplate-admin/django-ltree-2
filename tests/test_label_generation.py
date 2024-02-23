from django_ltree.paths import PathGenerator


def test_label_generation():
    assert PathGenerator.guess_the_label_size(62, 62) == 2
    assert PathGenerator.guess_the_label_size(0, 62) == 1

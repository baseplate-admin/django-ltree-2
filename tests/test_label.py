from django_ltree.paths import PathGenerator


def test_label_generation():
    assert PathGenerator.guess_the_label_size(62, 62) == 2
    assert PathGenerator.guess_the_label_size(0, 62) == 1


def test_automatic_name_creation():
    from taxonomy.models import Taxonomy

    for i in range(0, 1000):
        Taxonomy.objects.create_child(name=i)

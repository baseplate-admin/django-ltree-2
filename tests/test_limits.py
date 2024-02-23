from taxonomy.models import Taxonomy


def test_automatic_name_creation():
    for i in range(0, 2_538_557_185_841_324_496):
        Taxonomy.objects.create_child(name=i)

from taxonomy.models import Taxonomy

TEST_RANGE = 1_00_0


def test_automatic_name_creation():
    for i in range(0, TEST_RANGE):
        Taxonomy.objects.create_child(name=i)

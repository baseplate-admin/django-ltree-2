from taxonomy.models import Taxonomy

# Test whether the automatic path creation works as expected for create_child()
# The test creates a tree of Taxonomy objects with a specified depth and breadth.
def test_automatic_path_creation(db):
    
    TEST_DEPTH = 5
    TEST_BREADTH = 3
    NAME_PREFIX = "test_automatic_path_creation_"
    
    """Recursively create a tree of Taxonomy objects."""
    def recursive_create(depth: int, parent: Taxonomy):
        if depth == TEST_DEPTH:
            return
        for i in range(0, TEST_BREADTH):
            child = Taxonomy.objects.create_child(name=NAME_PREFIX+str(depth)+"_"+str(i), parent=parent)
            recursive_create(depth + 1, child)

    root = Taxonomy.objects.create_child(name=NAME_PREFIX+"root")
    recursive_create(depth=0, parent=root)
    
    # Check that the tree was created correctly

    # Check that the root node is correct
    assert root is not None, "Root should not be None"
    assert root.children().count() == TEST_BREADTH, f"Root should have {TEST_BREADTH} children"
    
    # Check that the children of the root node are correct
    possible_labels = [str(i) for i in range(0, TEST_DEPTH)]
    for i in range(0, TEST_BREADTH):
        child = root.children()[i]
        assert child is not None, f"Child {i} should not be None"
        assert child.label() in possible_labels, f"Child {i} label should be one of '{possible_labels}'" # order is not guaranteed
        assert child.children().count() == TEST_BREADTH, f"Child {i} should have {TEST_BREADTH} children"
        
    # Check that the depth of the tree is correct
    parent = root
    possible_labels = [str(i) for i in range(0, TEST_DEPTH)]
    for i in range(0, TEST_DEPTH):
        child = parent.children()[0]
        assert child is not None, f"Child {i} should not be None"
        assert child.label() in possible_labels, f"Child {i} label should have one of the following labels '{possible_labels}'" # order is not guaranteed
        parent = child
        
    # Latest child should have no children
    assert parent.children().count() == 0, "Latest child should have no children"


# Test whether the path creation works as expected for create_child() when providing a label
# The test creates a tree of Taxonomy objects with a set of labels
def test_manual_path_creation(db):
    DEPTH_LABELS = ["AA", "AB", "AC", "AD", "AE"]
    BREADTH_LABELS = ["X0", "Y_1", "Z__2"]
    NAME_PREFIX = "test_manual_path_creation_"
    
    """Recursively create a tree of Taxonomy objects."""
    def recursive_create_with_label(depth: int, parent: Taxonomy):
        if depth == len(DEPTH_LABELS):
            return
        
        depth_label = DEPTH_LABELS[depth]
        for breadth_label in BREADTH_LABELS:
            label = depth_label + "_" + breadth_label
            child = Taxonomy.objects.create_child(name=NAME_PREFIX+label, label=label, parent=parent)
            recursive_create_with_label(depth + 1, child)

    root_label = "root"
    root = Taxonomy.objects.create_child(name=NAME_PREFIX+"root", label=root_label)
    recursive_create_with_label(depth=0, parent=root)
    
    # Check that the tree was created correctly
    
    # Check that the root node is correct
    assert root is not None, "Root should not be None"
    assert root.label() == root_label, f"Root label should be '{root_label}'"
    assert root.children().count() == len(BREADTH_LABELS), f"Root should have {len(BREADTH_LABELS)} children"
        
    # Check that the children of the root node are correct
    possible_labels = [DEPTH_LABELS[0] + "_" + breadth for breadth in BREADTH_LABELS] # order is not guaranteed, so multiple labels are possible
    for i in range(0, len(BREADTH_LABELS)):
        child = root.children()[i]
        assert child is not None, f"Child at breadth {i} should not be None"
        assert child.label() in possible_labels, f"Label of child at breadth {i} should be one of '{possible_labels}'" 
        assert child.children().count() == len(BREADTH_LABELS), f"Child {i} should have {len(BREADTH_LABELS)} children"
        
    # Check that the depth of the tree is correct
    parent = root
    for i in range(0, len(DEPTH_LABELS)):
        possible_labels = [DEPTH_LABELS[i] + "_" + breadth for breadth in BREADTH_LABELS]  
        child = parent.children()[0]
        assert child is not None, f"Child at depth {i} should not be None"
        assert child.label() in possible_labels, f"Label of child at depth {i} should have one of the following labels '{possible_labels}'"
        parent = child
        
    # Latest child should have no children
    assert parent.children().count() == 0, "Latest child should have no children"
    
    # Check that the path is correct for one of the children at max depth:
    path_components = [root_label] + [depth + "_" + BREADTH_LABELS[0] for depth in DEPTH_LABELS]
    path_str = ".".join(path_components)
    deepest_child = Taxonomy.objects.filter(path=path_str)
    assert deepest_child.exists(), f"Child with path '{path_str}' should exist"


from taxonomy.models import Taxonomy
import pytest

# ----- Automatic Path Creation Tests -----

def test_create_root_node_automatic(db):
    """Test creating a root node with automatic labeling."""
    root = Taxonomy.objects.create_child(name="test_auto_root")
    assert root is not None
    assert root.children().count() == 0

def test_create_children_automatic(db):
    """Test creating children with automatic labels."""
    root = Taxonomy.objects.create_child(name="test_auto_root")
    
    # Create children
    for i in range(3):
        Taxonomy.objects.create_child(name=f"test_auto_child_{i}", parent=root)
    
    assert root.children().count() == 3

def test_children_have_automatic_labels(db):
    """Test that automatically created children get labels."""
    root = Taxonomy.objects.create_child(name="test_auto_root")
    child = Taxonomy.objects.create_child(name="test_auto_child", parent=root)
    
    assert child.label() is not None

def test_multilevel_hierarchy_automatic(db):
    """Test a multi-level hierarchy with automatic labels."""
    root = Taxonomy.objects.create_child(name="test_auto_root")
    child = Taxonomy.objects.create_child(name="test_auto_child", parent=root)
    grandchild = Taxonomy.objects.create_child(name="test_auto_grandchild", parent=child)
    
    assert root.children().count() == 1
    assert child.children().count() == 1
    assert grandchild.children().count() == 0

def test_deep_tree_automatic(db):
    """Test creating a deep tree with automatic labels."""
    root = Taxonomy.objects.create_child(name="test_auto_root")
    
    # Create a chain of nodes
    current = root
    for i in range(5):
        current = Taxonomy.objects.create_child(name=f"test_auto_level_{i}", parent=current)
    
    # Leaf node should have no children
    assert current.children().count() == 0

# ----- Manual Path Creation Tests -----

def test_create_root_with_custom_label(db):
    """Test creating a root node with a custom label."""
    root = Taxonomy.objects.create_child(name="test_manual_root", label="ROOT")
    assert root.label() == "ROOT"

def test_create_children_with_custom_labels(db):
    """Test creating children with custom labels."""
    root = Taxonomy.objects.create_child(name="test_manual_root", label="ROOT")
    
    labels = ["A", "B", "C"]
    for label in labels:
        Taxonomy.objects.create_child(name=f"test_manual_child_{label}", 
                                      label=label, parent=root)
    
    assert root.children().count() == len(labels)
    
    child_labels = [child.label() for child in root.children()]
    for label in labels:
        assert label in child_labels

def test_hierarchy_with_custom_labels(db):
    """Test a hierarchy with custom labels."""
    root = Taxonomy.objects.create_child(name="test_manual_root", label="ROOT")
    child = Taxonomy.objects.create_child(name="test_manual_child", 
                                         label="CHILD", parent=root)
    
    assert child.label() == "CHILD"
    assert root.children().count() == 1

def test_path_construction_with_custom_labels(db):
    """Test path construction with custom labels."""
    root = Taxonomy.objects.create_child(name="test_manual_root", label="R")
    child = Taxonomy.objects.create_child(name="test_manual_child", 
                                         label="C", parent=root)
    grandchild = Taxonomy.objects.create_child(name="test_manual_grandchild", 
                                              label="G", parent=child)
    
    # Path should be concatenated with periods
    assert str(grandchild.path) == "R.C.G"

def test_retrieve_node_by_path(db):
    """Test retrieving a node by its path."""
    root = Taxonomy.objects.create_child(name="test_manual_root", label="R")
    child = Taxonomy.objects.create_child(name="test_manual_child", 
                                         label="C", parent=root)
    Taxonomy.objects.create_child(name="test_manual_grandchild", 
                                 label="G", parent=child)
    
    # Retrieve by path
    node = Taxonomy.objects.filter(path="R.C.G").first()
    assert node is not None
    assert node.name == "test_manual_grandchild"

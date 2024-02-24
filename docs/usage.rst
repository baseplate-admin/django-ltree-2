Usage
=====

Lets assume that our model looks like this.

.. code-block:: python 
    
    # models.py
    from django import models
    from django_ltree import TreeModel

    class CustomTree(TreeModel):
        text = models.TextField()


Create a child without parent
-----------------------------

.. code-block:: python 

    from .models import CustomTree

    CustomTree.objects.create_child(text='Hello world')

The following code with create a child with no parent (ie:roots of a tree)

Create a child with parent
--------------------------
Let's assume we want to add a child to the CustomTree object of `pk 1`

.. code-block:: python 

    from .models import CustomTree

    # This must return a single object
    parent: CustomTree = CustomTree.objects.get(pk=1) 
    CustomTree.objects.create_child(text='Hello world', parent=parent)


Get all the roots of the model
------------------------------
A root means the the object that childrens anchor to.

.. code-block:: python 

    from .models import CustomTree

    roots: list[CustomTree] = CustomTree.objects.roots()


Get all the childrens of a object
---------------------------------
To get the childrens of a object, we can first get the object then call the QuerySet specific children function. 

.. code-block:: python 

    from .models import CustomTree

    instance = CustomTree.objects.get(pk=1)

    childrens: list[CustomTree] = instance.children()
    


Get the length of childrens of a object
---------------------------------------
`django` specific database functions still work when we call the filter method.

Lets assume we want to get the childrens of `CustomTree` object whose pk is 1.

.. code-block:: python 

    from .models import CustomTree

    instance = CustomTree.objects.get(pk=1)

    childrens: int = instance.children().count()
    

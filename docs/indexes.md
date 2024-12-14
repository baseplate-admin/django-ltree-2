# Indexes

If you want to add index to your `TreeModel`, use [`GistIndex`](https://docs.djangoproject.com/en/5.1/ref/contrib/postgres/indexes/#gistindex) from [`postgres`](https://www.postgresql.org/docs/9.1/textsearch-indexes.html).

```{note}
`GistIndex` was suggested based on [`@pauloxnet`](http://github.com/pauloxnet)'s code sample from this [microsoft Citus Con YouTube video](https://www.youtube.com/watch?v=u8F7bTJVe_4&t=1051s)

```

To implement the index in your model:

```{code-block} python
:caption: models.py

from django.contrib.postgres import indexes as idx
from django_ltree import TreeModel

class CustomTree(TreeModel):
    ...

    class Meta:
        indexes = [
            idx.GistIndex(fields=["path"]),
        ]
```

.. SeriAttrs documentation master file, created by
   sphinx-quickstart on Fri Feb 16 17:09:52 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to SeriAttrs's documentation!
=====================================

.. toctree::
   :caption: Contents:

   modules

How to use?
==================
Usage is the same as in attrs. The exception is that a class must inherit from DbClass or DbClassLiteral
   @define

   class Foo(DbClass):
     ...
.. toctree::
   :maxdepth: 1

   seriattrs.db_classes

Why not pure attrs?
==================
While attrs is a base of seriattrs it lacks some functionalities that make seriattrs better solution for developing applications:

- DbClass is equipped with serialize and deserialize methods that allow effortless conversion between states,

- DbClass solvers type reference problems nicely. When having classes that refer to each other in their fields DbClass automatically coverts Forward references to types,

   @define

   class Bar(DbClass):
     foo: "Foo" => Foo

   @define

   class Foo(DbClass):
     bar: "Bar" => Bar

- DbClass solvers circular reference problem so serialization and deserialization of self-referencing objects doesn't cause RecursionError.
   cat = Cat(None)

   ala = Ala(cat)

   cat.ala = ala

   serialized_cat = cat.serialize()

   serialized_ala = ala.serialize()

   deserialized_cat = Cat.deserialize(serialized_cat)

   deserialized_ala = Ala.deserialize(serialized_ala)

   assert deserialized_cat._id == cat._id

   assert deserialized_cat.ala._id == cat.ala._id

   assert deserialized_cat.ala.cat._id == cat.ala.cat._id

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

=======================
Flask-JqueryUiBootstrap
=======================

Flask jQuery Ui Bootstrap
-------------------------

Flask-JqueryUiBootstrap is minimalistic fork of `Flask-Bootstrap <https://github.com/mbr/flask-bootstrap>`_ project.
This project packages `Twitter's Bootstrap <http://twitter.github.com/bootstrap/>`_
with `jQuery UI <http://jqueryui.com/>`_ and is based on
`jQuery UI Bootstrap <http://addyosmani.github.io/jquery-ui-bootstrap/>`_ project.

If you don't need **jQuery UI Bootstrap** is **strongly recommended** to use better original plugin **Flask-Bootstrap**.

Usage
-----

Here is an example::

  from flask.ext.jqueryuibootstrap import Bootstrap

  [...]

  Bootstrap(app)

This makes base layout templates available: ``jqueryuibootstrap_base.html``.
This layout file have predefined blocks where you can put your content. The core
block to alter is ``body_content``, otherwise see the source of the template
for more possibilities.

Macros
------

A few macros are available to make your life easier. These need to be imported
(I recommend create your own ``base.html`` template that extends one of the
bootstrap base templates first and including the the macros there).

An example ``base.html``::

  {% extends "jqueryuibootstrap_base.html" %}
  {% import "jqueryuibootstrap_wtf.html" as wtf %}

Forms
+++++

The ``jqueryuibootstrap_wtf`` template contains macros to help you output forms
quickly. The most basic way is using them as an aid to create a form by hand::

  <form class="form form-horizontal" method="post">
    {{ form.hidden_tag() }}
    {{ wtf.form_errors(form, "only") }}

    {{ wtf.horizontal_field(form.field1) }}
    {{ wtf.horizontal_field(form.field2) }}

    <div class="form-actions">
       <button name="action_save" type="submit" class="btn btn-primary">Save changes</button>
    </div>
  </form>

However, often you just want to get a form done quickly and have no need for
intense fine-tuning:

::

  {{ wtf.quick_form(form) }}

Configuration options
---------------------

There are a few configuration options used by the templates:

====================================== ======================================================== ===
Option                                 Default
====================================== ======================================================== ===
``BOOTSTRAP_HTML5_SHIM``               ``True``                                                 Include the default IE-fixes that are usually included when using bootstrap.
``BOOTSTRAP_GOOGLE_ANALYTICS_ACCOUNT`` ``None``                                                 If set, include `Google Analytics <http://www.google.com/analytics>`_ boilerplate using this account.
====================================== ======================================================== ===

.. _FontAwesome: http://fortawesome.github.com/Font-Awesome/

Installation
------------

Either install from github using ``pip`` or from `PyPI
<http://pypi.python.org/pypi/Flask-JqueryUiBootstrap>`_.

A note on versifying
--------------------

Flask-JqueryUiBootstrap tries to keep some track of jQuery UI Bootstrap releases.
Versifying is usually in the form of **x.y.z** of **jQuery UI Bootstrap** version
with **.z** micro version of Flask extension Package. For example, a version of
**0.5.0.0** bundles version **0.5.0** of **jQuery UI Bootstrap** version and is
initial release of **Flask-JqueryUiBootstrap** containing that version.


FAQ
---

1. How can I add custom javascript to the template?

   Use Jinja2's ``super()`` in conjunction with the ``bootstrap_js_bottom``
   block. The super-function adds the contents of a block from the parent
   template, that way you can even decide if you want to include it before or
   after jQuery/bootstrap. Example::

     {% block bootstrap_js_bottom %}
       {{super()}}
       <script src="my_app_code.js">
     {% endblock %}

Contribute
----------

#. We are open for any help.
#. Fork `the repository`_ on GitHub to start making your changes to the **master** branch (or branch off of it).
#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to AUTHORS_.

.. _`the repository`: https://github.com/lightningwolf/Flask-JqueryUiBootstrap
.. _AUTHORS: https://github.com/lightningwolf/Flask-JqueryUiBootstrap/blob/master/AUTHORS.rst
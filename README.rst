python-trustico
===============

This module is the an API and a command line
for ordering SSL certificates from Trustico.

.. note:: 
   The code is still a work in progress 
   (i.e type2 products are not yet supported.)

Installation
------------

You need to install the dependencies listed in the `requirements.txt` file.

Usage
-----

Be sure to have unable the API in the web interface before
to try to use it.

Test the connexion::

  trustico -u trustico_user -p your_password -t

Get the status of an order::

  trustico -u trustico_user -p your_password -s -o 1111-11-11111-1111111

Create a new certificate with a existing certificate request::

  trustico -u trustico_user -p your_password -A admin_address.json -T tech_address.json -O order.json -C domain.csr

Where **order.json** looks like::

    {
        "product" : "rapidssl",
        "period" : 12,
        "approver" : "admin@example.com",
        "insurance" : 0,
        "servercount" : 1,
        "techusereseller" : 1,
        "novalidation" : 0
    }


**admin_address.json** looks like::

    {
        "title" : "Ms",
        "firstname" : "Eliza",
        "lastname" : "Xample",
        "organisation" : "EXample",
        "role" : "WebSite Owner",
        "email" : "example@example.com",
        "phonecc" : "1",
        "phoneac" : "514",
        "phonen" : "9460234",
        "address1" : "1 High Street",
        "city" : "MyTown",
        "state" : "London",
        "postcode" : "SW1 4AA",
        "country" : "GB"
    }

and for **tech_address.json** (same things but no *role* field)::

    {
        "title" : "Ms",
        "firstname" : "Eliza",
        "lastname" : "Xample",
        "organisation" : "EXample",
        "email" : "example@example.com",
        "phonecc" : "4",
        "phoneac" : "514",
        "phonen" : "9460234",
        "address1" : "1 High Street",
        "city" : "MyTown",
        "state" : "London",
        "postcode" : "SW1 4AA",
        "country" : "GB"
    }

Type::

  trustico --help

For complet usage details.

API
---

For the complet API see the official documentation at:

  https://resellers.trustico.com/geodirect/admin/api-overview.php

The script is inspired by the perl version:

  http://cpansearch.perl.org/src/CLIFFORDJ/Net-Trustico-0.01/lib/Net/Trustico.pm


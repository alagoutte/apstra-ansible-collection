.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. Anchors

.. _ansible_collections.juniper.apstra.apstra_facts_module:

.. Anchors: short name for ansible.builtin

.. Title

juniper.apstra.apstra_facts module -- Gather facts from Apstra AOS
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `juniper.apstra collection <https://galaxy.ansible.com/ui/repo/published/juniper/apstra/>`_ (version 1.0.6).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install juniper.apstra`.
    You need further requirements to be able to use this module,
    see :ref:`Requirements <ansible_collections.juniper.apstra.apstra_facts_module_requirements>` for details.

    To use it in a playbook, specify: :code:`juniper.apstra.apstra_facts`.

.. version_added

.. rst-class:: ansible-version-added

New in juniper.apstra 0.1.1

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module gathers facts from Apstra AOS, including information about blueprints, virtual networks, security zones, endpoint policies, and application points.


.. Aliases


.. Requirements

.. _ansible_collections.juniper.apstra.apstra_facts_module_requirements:

Requirements
------------
The below requirements are needed on the host that executes this module.

- python \>= 3.10
- apstra\-client \>= 1.0.0






.. Options

Parameters
----------

.. tabularcolumns:: \X{1}{3}\X{2}{3}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-api_url"></div>

      .. _ansible_collections.juniper.apstra.apstra_facts_module__parameter-api_url:

      .. rst-class:: ansible-option-title

      **api_url**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-api_url" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The URL used to access the Apstra api (APSTRA\_API\_URL).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-auth_token"></div>

      .. _ansible_collections.juniper.apstra.apstra_facts_module__parameter-auth_token:

      .. rst-class:: ansible-option-title

      **auth_token**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-auth_token" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The authentication token to use if already authenticated (APSTRA\_AUTH\_TOKEN).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-available_network_facts"></div>

      .. _ansible_collections.juniper.apstra.apstra_facts_module__parameter-available_network_facts:

      .. rst-class:: ansible-option-title

      **available_network_facts**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-available_network_facts" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, the module will return a list of available network objects.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-filter"></div>

      .. _ansible_collections.juniper.apstra.apstra_facts_module__parameter-filter:

      .. rst-class:: ansible-option-title

      **filter**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-filter" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Filter used to get the list of objects.

      Key is a type, value is a filter string.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`{"blueprints.nodes": "node\_type=system"}`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-gather_network_facts"></div>

      .. _ansible_collections.juniper.apstra.apstra_facts_module__parameter-gather_network_facts:

      .. rst-class:: ansible-option-title

      **gather_network_facts**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-gather_network_facts" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of network objects to gather facts about.

      Use 'all' to gather facts about all supported network objects.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`["blueprints"]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id"></div>

      .. _ansible_collections.juniper.apstra.apstra_facts_module__parameter-id:

      .. rst-class:: ansible-option-title

      **id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-id" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Dictionary containing identifiers to focus us.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`{}`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.juniper.apstra.apstra_facts_module__parameter-password:

      .. rst-class:: ansible-option-title

      **password**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The password for authentication (APSTRA\_PASSWORD).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.juniper.apstra.apstra_facts_module__parameter-username:

      .. rst-class:: ansible-option-title

      **username**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The username for authentication (APSTRA\_USERNAME).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-verify_certificates"></div>

      .. _ansible_collections.juniper.apstra.apstra_facts_module__parameter-verify_certificates:

      .. rst-class:: ansible-option-title

      **verify_certificates**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-verify_certificates" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to false, SSL certificates will not be verified (APSTRA\_VERIFY\_CERTIFICATES).


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    # Gather facts about all network objects
    - name: Gather all Apstra facts
      apstra_facts:
        gather_network_facts:
          - all

    # Gather facts about specific network objects for a blueprint
    - name: Gather specific Apstra facts
      apstra_facts:
        gather_network_facts:
          - virtual_networks
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"

    # Gather facts about system nodes in the blueprint
    - name: Gather system nodes
      apstra_facts:
        gather_network_facts:
          - blueprints.nodes
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
        filter:
          blueprints.nodes: "node_type=system"

    # Get the list of available network objects
    - name: List available Apstra network objects
      apstra_facts:
        gather_network_facts:
          - all
        available_network_facts: true

    # Run an arbitrary QE graph query against a blueprint
    - name: Query interfaces with if_name set
      juniper.apstra.apstra_facts:
        id:
          blueprint: "{{ blueprint_id }}"
        gather_network_facts:
          - blueprints.qe
        filter:
          blueprints.qe: >
            node(type="system", name="sys")
            .out(type="hosted_interfaces")
            .node(type="interface", name="intf")
      register: qe_result
    # Result: qe_result.ansible_facts.apstra_facts['blueprints.qe']
    # is a list of dicts keyed by each named node in the query (sys, intf, etc.)

    # Get the flat list of valid interface application-point IDs for a CT
    - name: Get CT application point IDs
      juniper.apstra.apstra_facts:
        id:
          blueprint: "{{ blueprint_id }}"
          endpoint_policy: "{{ ct_id }}"
        gather_network_facts:
          - endpoint_policy.application_point_ids
      register: ap_result
    # Result: ap_result.ansible_facts.apstra_facts['endpoint_policy.application_point_ids']
    # is a flat list of interface node ID strings



.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. tabularcolumns:: \X{1}{3}\X{2}{3}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Key
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-available_network_facts"></div>

      .. _ansible_collections.juniper.apstra.apstra_facts_module__return-available_network_facts:

      .. rst-class:: ansible-option-title

      **available_network_facts**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-available_network_facts" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of available network objects that can be gathered.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when available\_network\_facts is true

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`["blueprint.virtual\_networks", "blueprint.security\_zones", "blueprint.endpoint\_policies", "blueprint.endpoint\_policies.application\_points"]`


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Edwin Jacques (@edwinpjacques)


.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. ansible-links::

  - title: "Issue Tracker"
    url: "https://github.com/Juniper/apstra-ansible-collection/issues"
    external: true
  - title: "Homepage"
    url: "https://www.juniper.net/us/en/products/network-automation/apstra.html"
    external: true
  - title: "Repository (Sources)"
    url: "https://github.com/Juniper/apstra-ansible-collection"
    external: true


.. Parsing errors

.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. Anchors

.. _ansible_collections.juniper.apstra.property_set_module:

.. Anchors: short name for ansible.builtin

.. Title

juniper.apstra.property_set module -- Manage property sets in Apstra
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `juniper.apstra collection <https://galaxy.ansible.com/ui/repo/published/juniper/apstra/>`_ (version 1.0.6).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install juniper.apstra`.

    To use it in a playbook, specify: :code:`juniper.apstra.property_set`.

.. version_added

.. rst-class:: ansible-version-added

New in juniper.apstra 0.1.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module allows you to create, update, and delete property sets in Apstra.
- Supports two scopes depending on whether :literal:`blueprint` is provided in the :literal:`id` parameter.
- :strong:`Global scope` (no :literal:`blueprint` in :literal:`id`\ ) manages property sets in the Design \> Property Sets catalog at :literal:`/api/property\-sets`. Specify :literal:`label` and :literal:`values` (dict) in :literal:`body` to create; :literal:`property\_set` in :literal:`id` to get/update/delete.
- :strong:`Blueprint scope` (\ :literal:`blueprint` in :literal:`id`\ ) manages property sets assigned to a specific blueprint.
- For Datacenter (two\_stage\_l3clos) designs, property sets are imported from the global catalog into a blueprint by specifying the global property set :literal:`id` (and optionally a list of :literal:`keys` for partial import).
- For Freeform designs, property sets are created directly within the blueprint by specifying :literal:`label` and :literal:`values` (or :literal:`values\_yaml`\ ).
- Property sets allow arbitrary key\-value context to be passed to Jinja templates for configuration rendering.


.. Aliases


.. Requirements






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

      .. _ansible_collections.juniper.apstra.property_set_module__parameter-api_url:

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

      The URL used to access the Apstra api.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-auth_token"></div>

      .. _ansible_collections.juniper.apstra.property_set_module__parameter-auth_token:

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

      The authentication token to use if already authenticated.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body"></div>

      .. _ansible_collections.juniper.apstra.property_set_module__parameter-body:

      .. rst-class:: ansible-option-title

      **body**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Dictionary containing the property set details.

      For global property sets, use :literal:`label` and either :literal:`values` (dict) or :literal:`values\_yaml` (YAML string) to create. Use :literal:`values` or :literal:`values\_yaml` to update. The two fields are alternatives; provide one or the other.

      For Datacenter blueprint import, use :literal:`id` (global property set id) and optionally :literal:`keys` (list of keys for partial import).

      For Freeform blueprints, use :literal:`label`\ , :literal:`values` (dict) or :literal:`values\_yaml` (YAML string), and optionally :literal:`system\_id`.

      The API always returns both :literal:`values` and :literal:`values\_yaml` in responses regardless of which was used to create/update.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id"></div>

      .. _ansible_collections.juniper.apstra.property_set_module__parameter-id:

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

      Dictionary containing identifiers for the property set.

      For global property sets (Design catalog), omit :literal:`blueprint` and use :literal:`property\_set` for get/update/delete.

      For blueprint\-scoped property sets, include :literal:`blueprint` and optionally :literal:`property\_set`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.juniper.apstra.property_set_module__parameter-password:

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

      The password for authentication.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.juniper.apstra.property_set_module__parameter-state:

      .. rst-class:: ansible-option-title

      **state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Desired state of the property set.

      Use :literal:`present` to create or update.

      Use :literal:`absent` to delete.

      Use :literal:`reimported` to force a reimport of a global property set into a blueprint (PUT). This refreshes the blueprint copy with the latest values from the global catalog, even when the import metadata (\ :literal:`id`\ , :literal:`keys`\ ) has not changed.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"absent"`
      - :ansible-option-choices-entry:`"reimported"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.juniper.apstra.property_set_module__parameter-username:

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

      The username for authentication.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-verify_certificates"></div>

      .. _ansible_collections.juniper.apstra.property_set_module__parameter-verify_certificates:

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

      If set to false, SSL certificates will not be verified.


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

    # Global scope -- create a new property set in the Design catalog
    - name: Create global property set
      juniper.apstra.property_set:
        body:
          label: "my_custom_ps"
          values:
            ntp_server: "10.0.0.1"
            mtu: 9100
        state: present
      register: global_ps

    # Global scope -- update a property set by label (label must be in body)
    - name: Update global property set by label
      juniper.apstra.property_set:
        body:
          label: "my_custom_ps"
          values:
            ntp_server: "10.0.0.2"
            mtu: 9200
        state: present

    # Global scope -- update a property set by ID (no label required in body)
    - name: Update global property set by ID
      juniper.apstra.property_set:
        id:
          property_set: "{{ global_ps.id.property_set }}"
        body:
          values:
            ntp_server: "10.0.0.2"
            mtu: 9200
        state: present

    # Global scope -- create using values_yaml key inside values dict
    - name: Create global property set with values_yaml as a key in values
      juniper.apstra.property_set:
        body:
          label: "my_ps_with_yaml_key"
          values:
            ntp_server: "10.0.0.1"
            values_yaml: "mtu: 9100
    ospf_area: 0.0.0.0
    "
        state: present

    # Global scope -- create using values_yaml (YAML string)
    - name: Create global property set with YAML string values
      juniper.apstra.property_set:
        body:
          label: "my_yaml_ps"
          values_yaml: |
            ntp_server: 10.0.0.1
            mtu: 9100
        state: present
      register: yaml_ps

    # Global scope -- update using values_yaml (label must be in body to identify record)
    - name: Update global property set with YAML string by label
      juniper.apstra.property_set:
        body:
          label: "my_yaml_ps"
          values_yaml: |
            ntp_server: 10.0.0.2
            mtu: 9200
        state: present

    # Global scope -- update using values_yaml by ID
    - name: Update global property set with YAML string by ID
      juniper.apstra.property_set:
        id:
          property_set: "{{ yaml_ps.id.property_set }}"
        body:
          values_yaml: |
            ntp_server: 10.0.0.2
            mtu: 9200
        state: present

    # Global scope -- delete a property set by ID
    - name: Delete global property set by ID
      juniper.apstra.property_set:
        id:
          property_set: "{{ global_ps.id.property_set }}"
        state: absent

    # Global scope -- delete a property set by label
    - name: Delete global property set by label
      juniper.apstra.property_set:
        body:
          label: "my_custom_ps"
        state: absent

    # Blueprint scope -- import a global property set into a blueprint
    - name: Import global property set into blueprint
      juniper.apstra.property_set:
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
        body:
          id: "dcqcn"
        state: present

    # Import using property set label instead of UUID
    - name: Import property set by name
      juniper.apstra.property_set:
        id:
          blueprint: "my-blueprint"
        body:
          id: "my_custom_ps"
        state: present

    # Blueprint scope -- partial import with specific keys
    - name: Import property set with specific keys
      juniper.apstra.property_set:
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
        body:
          id: "dcqcn"
          keys:
            - "dcqcn"
        state: present

    # Blueprint scope -- Freeform design, create directly
    - name: Create property set in freeform blueprint
      juniper.apstra.property_set:
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
        body:
          label: "my_property_set"
          values:
            mtu: 9100
            ntp_server: "10.0.0.1"
        state: present

    # Blueprint scope -- Freeform design, create using values_yaml
    - name: Create property set in freeform blueprint with YAML string
      juniper.apstra.property_set:
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
        body:
          label: "my_yaml_property_set"
          values_yaml: |
            mtu: 9100
            ntp_server: 10.0.0.1
        state: present

    # Blueprint scope -- Freeform design, update using values_yaml
    - name: Update property set in freeform blueprint with YAML string
      juniper.apstra.property_set:
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
          property_set: "abc-123"
        body:
          values_yaml: |
            mtu: 9200
            ntp_server: 10.0.0.2
        state: present

    # Blueprint scope -- reimport a property set (refresh after global update)
    - name: Reimport property set into blueprint
      juniper.apstra.property_set:
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
        body:
          id: "dcqcn"
        state: reimported

    # Blueprint scope -- delete a property set
    - name: Delete property set from blueprint
      juniper.apstra.property_set:
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
          property_set: "abc-123"
        state: absent



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
        <div class="ansibleOptionAnchor" id="return-changed"></div>

      .. _ansible_collections.juniper.apstra.property_set_module__return-changed:

      .. rst-class:: ansible-option-title

      **changed**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Indicates whether the module has made any changes.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-changes"></div>

      .. _ansible_collections.juniper.apstra.property_set_module__return-changes:

      .. rst-class:: ansible-option-title

      **changes**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-changes" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Dictionary of updates that were applied.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on update


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-id"></div>

      .. _ansible_collections.juniper.apstra.property_set_module__return-id:

      .. rst-class:: ansible-option-title

      **id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-id" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The ID of the property set.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on create, or when object identified by label

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"blueprint": "5f2a77f6\-1f33\-4e11\-8d59\-6f9c26f16962", "property\_set": "dcqcn"}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.juniper.apstra.property_set_module__return-msg:

      .. rst-class:: ansible-option-title

      **msg**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-msg" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The output message that the module generates.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-property_set"></div>

      .. _ansible_collections.juniper.apstra.property_set_module__return-property_set:

      .. rst-class:: ansible-option-title

      **property_set**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-property_set" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The property set object details.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on create or update

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"id": "dcqcn", "label": "DataCenter QoS Congestion Notification", "values": {"dcqcn": {"drop\_profile": {}}}}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-response"></div>

      .. _ansible_collections.juniper.apstra.property_set_module__return-response:

      .. rst-class:: ansible-option-title

      **response**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-response" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The property set object details.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state is present and changes are made


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Vamsi Gavini (@vgavini)


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

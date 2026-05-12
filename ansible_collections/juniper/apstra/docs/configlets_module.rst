.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. Anchors

.. _ansible_collections.juniper.apstra.configlets_module:

.. Anchors: short name for ansible.builtin

.. Title

juniper.apstra.configlets module -- Manage configlets in Apstra
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `juniper.apstra collection <https://galaxy.ansible.com/ui/repo/published/juniper/apstra/>`_ (version 1.0.6).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install juniper.apstra`.

    To use it in a playbook, specify: :code:`juniper.apstra.configlets`.

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

- This module allows you to create, update, and delete configlets in Apstra.
- Supports both catalog (design) configlets and blueprint configlets.
- Catalog configlets are stored in the global design catalog.
- Blueprint configlets are applied to a specific blueprint and include a condition for role\-based targeting.
- Configlets contain one or more generators, each specifying the config style (junos, eos, nxos, sonic), section (system, set\_based\_system, interface, set\_based\_interface, file, ospf, etc.), template text, negation template text, and optional filename.


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

      .. _ansible_collections.juniper.apstra.configlets_module__parameter-api_url:

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

      .. _ansible_collections.juniper.apstra.configlets_module__parameter-auth_token:

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

      .. _ansible_collections.juniper.apstra.configlets_module__parameter-body:

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

      Dictionary containing the configlet object details.

      For catalog configlets, keys include :literal:`display\_name`\ , :literal:`ref\_archs` (optional, defaults to :literal:`["two\_stage\_l3clos"]`\ ), and :literal:`generators`.

      For blueprint configlets, keys include :literal:`label`\ , :literal:`condition`\ , and :literal:`configlet` (which itself contains :literal:`display\_name` and :literal:`generators`\ ).

      Each generator is a dictionary with :literal:`config\_style`\ , :literal:`template\_text`\ , :literal:`negation\_template\_text`\ , :literal:`section`\ , and :literal:`filename`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id"></div>

      .. _ansible_collections.juniper.apstra.configlets_module__parameter-id:

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

      Dictionary containing the configlet ID.

      For catalog configlets, use :literal:`configlet` key.

      For blueprint configlets, use :literal:`blueprint` and optionally :literal:`configlet` keys.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.juniper.apstra.configlets_module__parameter-password:

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

      .. _ansible_collections.juniper.apstra.configlets_module__parameter-state:

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

      Desired state of the configlet.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"absent"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-type"></div>

      .. _ansible_collections.juniper.apstra.configlets_module__parameter-type:

      .. rst-class:: ansible-option-title

      **type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-type" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The type of configlet to manage.

      :literal:`catalog` manages global design configlets at /api/design/configlets.

      :literal:`blueprint` manages configlets applied to a specific blueprint.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"catalog"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"blueprint"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.juniper.apstra.configlets_module__parameter-username:

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

      .. _ansible_collections.juniper.apstra.configlets_module__parameter-verify_certificates:

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

    - name: Create a catalog configlet
      juniper.apstra.configlets:
        type: catalog
        body:
          display_name: "SNMP Config"
          ref_archs:
            - "two_stage_l3clos"
          generators:
            - config_style: "junos"
              section: "system"
              template_text: |
                snmp {
                  community public;
                }
              negation_template_text: ""
              filename: ""
        state: present

    - name: Update a catalog configlet by display_name
      juniper.apstra.configlets:
        type: catalog
        body:
          display_name: "SNMP Config"
          ref_archs:
            - "two_stage_l3clos"
          generators:
            - config_style: "junos"
              section: "system"
              template_text: |
                snmp {
                  community private;
                }
              negation_template_text: ""
              filename: ""
        state: present

    - name: Delete a catalog configlet by ID
      juniper.apstra.configlets:
        type: catalog
        id:
          configlet: "550e8400-e29b-41d4-a716-446655440000"
        state: absent

    # ── Import Catalog Configlet to Blueprint ───────────────────────────
    # After creating a catalog configlet, import it into a blueprint by
    # passing the catalog configlet UUID as body.configlet. The module
    # automatically resolves the UUID to the full catalog configlet object
    # required by the Apstra API (POST /api/blueprints/{id}/configlets).

    - name: Import catalog configlet to blueprint
      juniper.apstra.configlets:
        type: blueprint
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
        body:
          configlet: "550e8400-e29b-41d4-a716-446655440000"
          condition: 'role in ["spine", "leaf"]'
          label: "SNMP Config"
        state: present
      register: bp_import

    # Import using catalog configlet display_name instead of UUID
    - name: Import catalog configlet by name
      juniper.apstra.configlets:
        type: blueprint
        id:
          blueprint: "my-blueprint"
        body:
          configlet: "SNMP Config"
          condition: 'role in ["spine", "leaf"]'
          label: "SNMP Config"
        state: present

    - name: Remove imported catalog configlet from blueprint
      juniper.apstra.configlets:
        type: blueprint
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
          configlet: "{{ bp_import.id.configlet }}"
        state: absent

    - name: Create a blueprint configlet
      juniper.apstra.configlets:
        type: blueprint
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
        body:
          label: "Leaf SNMP Config"
          condition: 'role in ["leaf"]'
          configlet:
            display_name: "Leaf SNMP Config"
            generators:
              - config_style: "junos"
                section: "system"
                template_text: |
                  snmp {
                    community public;
                  }
                negation_template_text: ""
                filename: ""
        state: present

    - name: Update a blueprint configlet
      juniper.apstra.configlets:
        type: blueprint
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
        body:
          label: "Leaf SNMP Config"
          condition: 'role in ["leaf", "spine"]'
          configlet:
            display_name: "Leaf SNMP Config"
            generators:
              - config_style: "junos"
                section: "system"
                template_text: |
                  snmp {
                    community private;
                  }
                negation_template_text: ""
                filename: ""
        state: present

    - name: Delete a blueprint configlet by ID
      juniper.apstra.configlets:
        type: blueprint
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
          configlet: "AjAuUuVLylXCUgAqaQ"
        state: absent

    - name: Create a catalog configlet with Jinja2 template variables (NTP)
      juniper.apstra.configlets:
        type: catalog
        body:
          display_name: "NTP Template Config"
          ref_archs:
            - "two_stage_l3clos"
          generators:
            - config_style: "junos"
              section: "system"
              template_text: |
                system {
                  ntp {
                    server {{ ntp_server }};
                    boot-server {{ ntp_server }};
                  }
                }
              negation_template_text: ""
              filename: ""
        state: present

    - name: Create a multi-vendor AAA catalog configlet (junos, nxos, eos)
      juniper.apstra.configlets:
        type: catalog
        body:
          display_name: "AAA Multi-Vendor Config"
          ref_archs:
            - "two_stage_l3clos"
          generators:
            - config_style: "junos"
              section: "system"
              template_text: |
                system {
                  authentication-order [ radius password ];
                  radius-server {
                    10.0.0.100 secret radpass;
                  }
                }
              negation_template_text: ""
              filename: ""
            - config_style: "nxos"
              section: "system"
              template_text: |
                radius-server host 10.0.0.100 key radpass
                aaa authentication login default group radius local
              negation_template_text: ""
              filename: ""
            - config_style: "eos"
              section: "system"
              template_text: |
                radius-server host 10.0.0.100 key radpass
                aaa authentication login default group radius local
              negation_template_text: ""
              filename: ""
        state: present

    - name: Create a blueprint syslog configlet
      juniper.apstra.configlets:
        type: blueprint
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
        body:
          label: "Syslog Config"
          condition: 'role in ["leaf", "spine"]'
          configlet:
            display_name: "Syslog Config"
            generators:
              - config_style: "junos"
                section: "system"
                template_text: |
                  system {
                    syslog {
                      host 10.0.0.1 {
                        any warning;
                      }
                    }
                  }
                negation_template_text: ""
                filename: ""
        state: present



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

      .. _ansible_collections.juniper.apstra.configlets_module__return-changed:

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

      .. _ansible_collections.juniper.apstra.configlets_module__return-changes:

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
        <div class="ansibleOptionAnchor" id="return-configlet"></div>

      .. _ansible_collections.juniper.apstra.configlets_module__return-configlet:

      .. rst-class:: ansible-option-title

      **configlet**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-configlet" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The final configlet object details.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on create or update


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-id"></div>

      .. _ansible_collections.juniper.apstra.configlets_module__return-id:

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

      The ID of the configlet.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on create, or when object identified by display\_name/label

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"configlet": "550e8400\-e29b\-41d4\-a716\-446655440000"}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.juniper.apstra.configlets_module__return-msg:

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
        <div class="ansibleOptionAnchor" id="return-response"></div>

      .. _ansible_collections.juniper.apstra.configlets_module__return-response:

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

      The configlet object details.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state is present and changes are made


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Prabhanjan KV (@kvp_jnpr)


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

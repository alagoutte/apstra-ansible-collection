.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. Anchors

.. _ansible_collections.juniper.apstra.design_module:

.. Anchors: short name for ansible.builtin

.. Title

juniper.apstra.design module -- Manage Apstra design elements (logical devices, rack types, templates)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `juniper.apstra collection <https://galaxy.ansible.com/ui/repo/published/juniper/apstra/>`_ (version 1.0.6).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install juniper.apstra`.

    To use it in a playbook, specify: :code:`juniper.apstra.design`.

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

- Create or ensure existence of Apstra design elements required before blueprint creation.
- Supports logical devices, rack types, rack\-based templates, and interface maps.
- Uses the AOS SDK generator functions to build proper API payloads from simplified YAML definitions (same format as aos\_models/).
- Idempotent — skips creation if the element already exists.


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

      .. _ansible_collections.juniper.apstra.design_module__parameter-api_url:

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

      .. _ansible_collections.juniper.apstra.design_module__parameter-auth_token:

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

      .. _ansible_collections.juniper.apstra.design_module__parameter-body:

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

      The specification dict for the design element.

      For logical\_device — must contain :literal:`panels` list.

      For rack\_type — must contain :literal:`leafs` and optionally :literal:`generics`\ , :literal:`access`.

      For template — must contain :literal:`spine`\ , :literal:`racks`\ , and optionally :literal:`overlay\_control\_protocol`\ , :literal:`asn\_allocation\_policy`.

      For interface\_map — must contain :literal:`logical\_device` and :literal:`device\_profile`. Optionally :literal:`dp\_usage` (list of [port\_id, transform\_id] pairs); if omitted, auto\-generated from the device profile's default transformations.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id"></div>

      .. _ansible_collections.juniper.apstra.design_module__parameter-id:

      .. rst-class:: ansible-option-title

      **id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-id" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Identifies the design element.

      Must contain :literal:`design\_type` and :literal:`name`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id/design_type"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.design_module__parameter-id/design_type:

      .. rst-class:: ansible-option-title

      **design_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-id/design_type" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The type of design element to manage.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"logical\_device"`
      - :ansible-option-choices-entry:`"rack\_type"`
      - :ansible-option-choices-entry:`"template"`
      - :ansible-option-choices-entry:`"interface\_map"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id/name"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.design_module__parameter-id/name:

      .. rst-class:: ansible-option-title

      **name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-id/name" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The name/id of the design element.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.juniper.apstra.design_module__parameter-password:

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

      .. _ansible_collections.juniper.apstra.design_module__parameter-state:

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

      Desired state of the design element.

      :literal:`present` creates the element if it does not exist.

      :literal:`absent` deletes the element.

      :literal:`queried` lists elements of the given :literal:`design\_type`. When :literal:`id.name` is provided, returns that single element. When :literal:`id.name` is :literal:`'\*'` or :literal:`'all'`\ , returns all elements of the type.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"absent"`
      - :ansible-option-choices-entry:`"queried"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.juniper.apstra.design_module__parameter-username:

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

      .. _ansible_collections.juniper.apstra.design_module__parameter-verify_certificates:

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

    - name: Create logical device
      juniper.apstra.design:
        api_url: "https://apstra:443/api"
        auth_token: "{{ token }}"
        id:
          design_type: logical_device
          name: simple_dc_vjunos_switch_96x1
        body:
          panels:
            - panel1:
                portgroups:
                  - portgroup1:
                      ports: 96
                      speed: 1
                      connects_to:
                        - superspine
                        - spine
                        - leaf
                        - access
                        - peer
                        - unused
                        - generic
        state: present

    - name: Create rack type
      juniper.apstra.design:
        api_url: "https://apstra:443/api"
        auth_token: "{{ token }}"
        id:
          design_type: rack_type
          name: connectorops_vjunos-rack
        body:
          leafs:
            - leaf1:
                label: leaf-1
                link_per_spine_count: 1
                link_per_spine_speed: 1
                logical_device: simple_dc_vjunos_switch_96x1
                redundancy_protocol: esi
          generics:
            - host1:
                label: host-1
                logical_device: AOS-2x1-1
                links:
                  - link1:
                      link_speed: 1
                      target_switch_label: leaf-1
                      link_per_switch_count: 1
                      label: host1_leaf1_link
                      lag_mode: lacp_active
                      attachment_type: dualAttached
        state: present

    - name: Create template
      juniper.apstra.design:
        api_url: "https://apstra:443/api"
        auth_token: "{{ token }}"
        id:
          design_type: template
          name: connectorops_2spine4leaf
        body:
          spine:
            logical_device: simple_dc_vjunos_switch_96x1
            count: 2
          racks:
            connectorops_vjunos-rack: 1
          overlay_control_protocol: evpn
          asn_allocation_policy: distinct
        state: present

    - name: Delete a design element
      juniper.apstra.design:
        api_url: "https://apstra:443/api"
        auth_token: "{{ token }}"
        id:
          design_type: template
          name: connectorops_2spine4leaf
        state: absent

    - name: Create interface map (auto-generates port mappings from device profile)
      juniper.apstra.design:
        api_url: "https://apstra:443/api"
        auth_token: "{{ token }}"
        id:
          design_type: interface_map
          name: simple_dc_vjunos_ifmap
        body:
          logical_device: simple_dc_vjunos_switch_96x1
          device_profile: vJunos-switch
        state: present

    - name: List all interface maps
      juniper.apstra.design:
        api_url: "https://apstra:443/api"
        auth_token: "{{ token }}"
        id:
          design_type: interface_map
          name: all
        state: queried
      register: all_imaps

    - name: Use queried interface maps
      ansible.builtin.debug:
        msg: "Found {{ all_imaps.design_items | length }} interface maps"

    - name: Query a specific logical device by name
      juniper.apstra.design:
        api_url: "https://apstra:443/api"
        auth_token: "{{ token }}"
        id:
          design_type: logical_device
          name: AOS-7x10-Leaf
        state: queried
      register: ld_result

    - name: Show queried logical device
      ansible.builtin.debug:
        msg: "Logical device: {{ ld_result.data }}"



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

      .. _ansible_collections.juniper.apstra.design_module__return-changed:

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

      Whether the element was created or already existed.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-data"></div>

      .. _ansible_collections.juniper.apstra.design_module__return-data:

      .. rst-class:: ansible-option-title

      **data**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-data" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The full design element data from the server.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state is present, absent, or queried with a specific name


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-design_items"></div>

      .. _ansible_collections.juniper.apstra.design_module__return-design_items:

      .. rst-class:: ansible-option-title

      **design_items**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-design_items" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of design elements returned by :literal:`state=queried`.

      When querying all (\ :literal:`name=all` or :literal:`name=\*`\ ), contains every element of the given :literal:`design\_type`.

      When querying a specific name, contains a single\-element list.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state is queried


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-id"></div>

      .. _ansible_collections.juniper.apstra.design_module__return-id:

      .. rst-class:: ansible-option-title

      **id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-id" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The ID of the design element.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


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

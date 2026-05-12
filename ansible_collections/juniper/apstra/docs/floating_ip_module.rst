.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. Anchors

.. _ansible_collections.juniper.apstra.floating_ip_module:

.. Anchors: short name for ansible.builtin

.. Title

juniper.apstra.floating_ip module -- Manage Floating IPs in an Apstra blueprint
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `juniper.apstra collection <https://galaxy.ansible.com/ui/repo/published/juniper/apstra/>`_ (version 1.0.6).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install juniper.apstra`.

    To use it in a playbook, specify: :code:`juniper.apstra.floating_ip`.

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

- Create, update, query, or delete Floating IP addresses within an Apstra blueprint.
- Floating IPs (VIP endpoints) are typically auto\-created by Apstra when Connectivity Templates assign them. This module also allows creating them manually, renaming them (\ :literal:`label`\ ), setting a :literal:`description`\ , and changing the IP address (\ :literal:`ipv4\_addr` / :literal:`ipv6\_addr`\ ).
- Use :literal:`state=queried` to list all floating IPs or retrieve a single one.
- Use :literal:`state=present` to create or update a floating IP (idempotent).
- Use :literal:`state=absent` to delete a floating IP.


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

      .. _ansible_collections.juniper.apstra.floating_ip_module__parameter-api_url:

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

      .. _ansible_collections.juniper.apstra.floating_ip_module__parameter-auth_token:

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

      .. _ansible_collections.juniper.apstra.floating_ip_module__parameter-body:

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

      Desired properties of the floating IP.

      :literal:`label` (str) — display name shown in the Apstra UI.

      :literal:`description` (str) — free\-text description.

      :literal:`ipv4\_addr` (str) — IPv4 address in CIDR format (e.g. :literal:`10.2.22.201/24`\ ).

      :literal:`ipv6\_addr` (str) — IPv6 address in CIDR format.

      :literal:`virtual\_network` (str) — Virtual network name or UUID. Used as a lookup key to find the floating IP that belongs to that VN. Particularly useful for auto\-created floating IPs which have no label.

      :literal:`virtual\_network\_id` (str) — UUID of the associated virtual network (create only).

      :literal:`vn\_endpoints` (list) — list of VN endpoint IDs (create only).

      :literal:`generic\_system\_ids` (list) — list of generic system IDs (create only).

      When :literal:`state=present`\ , only supplied fields are changed.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id"></div>

      .. _ansible_collections.juniper.apstra.floating_ip_module__parameter-id:

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

      Identifies the blueprint and optionally the floating IP node.

      :literal:`blueprint` (str, required) — blueprint name or UUID.

      :literal:`floating\_ip` (str, optional) — floating IP node UUID. If omitted, the module searches by :literal:`body.label` or :literal:`body.ipv4\_addr`. For creation, a UUID is auto\-generated when no existing floating IP is found.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.juniper.apstra.floating_ip_module__parameter-password:

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

      .. _ansible_collections.juniper.apstra.floating_ip_module__parameter-state:

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

      :literal:`present` — create or update the floating IP (idempotent).

      :literal:`absent` — delete the floating IP.

      :literal:`queried` — list all floating IPs or retrieve a single one (read\-only).


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

      .. _ansible_collections.juniper.apstra.floating_ip_module__parameter-username:

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

      .. _ansible_collections.juniper.apstra.floating_ip_module__parameter-verify_certificates:

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

    # List all floating IPs in a blueprint
    - name: List floating IPs
      juniper.apstra.floating_ip:
        id:
          blueprint: "my-blueprint"
        state: queried
      register: fip_result

    - name: Show floating IPs
      ansible.builtin.debug:
        var: fip_result.floating_ips

    # Get a single floating IP by node ID
    - name: Get floating IP by ID
      juniper.apstra.floating_ip:
        id:
          blueprint: "my-blueprint"
          floating_ip: "{{ fip_node_id }}"
        state: queried
      register: fip

    # Create a new floating IP (POST)
    - name: Create a floating IP
      juniper.apstra.floating_ip:
        id:
          blueprint: "my-blueprint"
        body:
          label: "Tenant5-VIP"
          description: "Primary VIP for Tenant5"
          ipv4_addr: "10.2.22.201/24"
        state: present
      register: fip_create

    # --- PATCH (update) examples ---
    # The module detects whether the floating IP already exists.
    # If it does, it issues a PATCH with only the changed fields.

    # PATCH by node ID — most explicit; supply id.floating_ip directly
    - name: Update floating IP label by node ID (PATCH)
      juniper.apstra.floating_ip:
        id:
          blueprint: "my-blueprint"
          floating_ip: "{{ fip_node_id }}"
        body:
          label: "Tenant5-VIP-renamed"
          description: "Updated description"
        state: present

    # PATCH by label — module looks up the node ID first, then PATCHes
    - name: Update floating IP address by label lookup (PATCH)
      juniper.apstra.floating_ip:
        id:
          blueprint: "my-blueprint"
        body:
          label: "Tenant5-VIP"          # used to FIND the floating IP
          ipv4_addr: "10.2.22.210/24"   # new address to set via PATCH
        state: present

    # PATCH by VN name — finds the floating IP that belongs to a virtual network.
    # Auto-created floating IPs have no label; use virtual_network to locate them.
    - name: Name an auto-created floating IP by its VN (PATCH)
      juniper.apstra.floating_ip:
        id:
          blueprint: "my-blueprint"
        body:
          virtual_network: "Tenant2-VLAN22"   # VN name or UUID — used to FIND the floating IP
          label: "Tenant2-VIP"                # new label to set via PATCH
          description: "Auto-created VIP for Tenant2"
        state: present

    # PATCH by IPv4 address — useful when label is unknown
    - name: Update floating IP description by ipv4_addr lookup (PATCH)
      juniper.apstra.floating_ip:
        id:
          blueprint: "my-blueprint"
        body:
          ipv4_addr: "10.2.22.201/24"   # used to FIND the floating IP
          description: "Found by IP"    # new description to set via PATCH
        state: present

    # Idempotent update — no change if values already match
    - name: Ensure floating IP has expected label (idempotent PATCH)
      juniper.apstra.floating_ip:
        id:
          blueprint: "my-blueprint"
          floating_ip: "{{ fip_node_id }}"
        body:
          label: "Tenant5-VIP"
        state: present

    # Delete a floating IP by label
    - name: Delete floating IP
      juniper.apstra.floating_ip:
        id:
          blueprint: "my-blueprint"
        body:
          label: "Tenant5-VIP"
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

      .. _ansible_collections.juniper.apstra.floating_ip_module__return-changed:

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

      Whether the floating IP was changed.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-floating_ip"></div>

      .. _ansible_collections.juniper.apstra.floating_ip_module__return-floating_ip:

      .. rst-class:: ansible-option-title

      **floating_ip**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-floating_ip" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The current state of the floating IP after the operation.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state is present and a single floating IP is targeted

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"description": "Primary VIP for Tenant5", "id": "abc123", "immutable": false, "ipv4\_addr": "10.2.22.201/24", "label": "Tenant5\-VIP"}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-floating_ips"></div>

      .. _ansible_collections.juniper.apstra.floating_ip_module__return-floating_ips:

      .. rst-class:: ansible-option-title

      **floating_ips**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-floating_ips" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of all floating IPs in the blueprint.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state is queried and no floating\_ip ID is specified


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.juniper.apstra.floating_ip_module__return-msg:

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

      Human\-readable result message.


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

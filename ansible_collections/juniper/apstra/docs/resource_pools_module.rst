.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. Anchors

.. _ansible_collections.juniper.apstra.resource_pools_module:

.. Anchors: short name for ansible.builtin

.. Title

juniper.apstra.resource_pools module -- Manage resource pools in Apstra
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `juniper.apstra collection <https://galaxy.ansible.com/ui/repo/published/juniper/apstra/>`_ (version 1.0.6).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install juniper.apstra`.

    To use it in a playbook, specify: :code:`juniper.apstra.resource_pools`.

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

- This module allows you to create, update, and delete resource pools in Apstra.
- Supported pool types are ASN, Integer, IP, IPv6, VLAN, and VNI.


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

      .. _ansible_collections.juniper.apstra.resource_pools_module__parameter-api_url:

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

      .. _ansible_collections.juniper.apstra.resource_pools_module__parameter-auth_token:

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

      .. _ansible_collections.juniper.apstra.resource_pools_module__parameter-body:

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

      Dictionary containing the resource pool object details.

      For ASN pools, use 'ranges' with 'first' and 'last' integer keys.

      For Integer pools, use 'ranges' with 'first' and 'last' integer keys.

      For IP pools, use 'subnets' with 'network' (CIDR notation) keys.

      For IPv6 pools, use 'subnets' with 'network' (CIDR notation) keys.

      For VLAN pools, use 'ranges' with 'first' and 'last' integer keys.

      For VNI pools, use 'ranges' with 'first' and 'last' integer keys.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id"></div>

      .. _ansible_collections.juniper.apstra.resource_pools_module__parameter-id:

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

      Dictionary containing the resource pool ID.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.juniper.apstra.resource_pools_module__parameter-password:

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

      .. _ansible_collections.juniper.apstra.resource_pools_module__parameter-state:

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

      Desired state of the resource pool.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"absent"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-type"></div>

      .. _ansible_collections.juniper.apstra.resource_pools_module__parameter-type:

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

      The type of resource pool to manage.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"asn"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"integer"`
      - :ansible-option-choices-entry:`"ip"`
      - :ansible-option-choices-entry:`"ipv6"`
      - :ansible-option-choices-entry:`"vlan"`
      - :ansible-option-choices-entry:`"vni"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.juniper.apstra.resource_pools_module__parameter-username:

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

      .. _ansible_collections.juniper.apstra.resource_pools_module__parameter-verify_certificates:

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

    # ── ASN Pool CRUD with Blueprint Assignment ─────────────────────────

    - name: Create an ASN pool (or update it if the display_name exists)
      juniper.apstra.resource_pools:
        type: asn
        body:
          display_name: "Test-ASN-Pool"
          ranges:
            - first: 65000
              last: 65100
        state: present
      register: asn_pool

    - name: Show ASN pool total and used_percentage
      ansible.builtin.debug:
        msg: "ASN Pool {{ item.key }} - total: {{ item.value.total }}, used_percentage: {{ item.value.used_percentage }}"
      loop: "{{ ansible_facts.apstra_facts.asn_pools | dict2items }}"
      loop_control:
        label: "{{ item.key }}"

    - name: Get resource groups from blueprint
      ansible.builtin.uri:
        url: "{{ apstra_api_url }}/blueprints/{{ blueprint_id }}/resource_groups"
        method: GET
        headers:
          AuthToken: "{{ auth_token }}"
        validate_certs: false
        status_code: 200
      register: resource_groups

    - name: Find ASN resource group
      ansible.builtin.set_fact:
        asn_resource_group: >-
          {{ resource_groups.json.items
             | selectattr('resource_type', 'equalto', 'asn')
             | first }}

    - name: Assign ASN pool to blueprint
      ansible.builtin.uri:
        url: "{{ apstra_api_url }}/blueprints/{{ blueprint_id }}/resource_groups/asn/{{ asn_resource_group.group_name }}"
        method: PUT
        headers:
          AuthToken: "{{ auth_token }}"
          Content-Type: "application/json"
        body_format: json
        body:
          pool_ids:
            - "{{ asn_pool.id.asn_pool }}"
        validate_certs: false
        status_code: [200, 202, 204]

    - name: Verify ASN pool is assigned to blueprint
      ansible.builtin.uri:
        url: "{{ apstra_api_url }}/blueprints/{{ blueprint_id }}/resource_groups/asn/{{ asn_resource_group.group_name }}"
        method: GET
        headers:
          AuthToken: "{{ auth_token }}"
        validate_certs: false
        status_code: 200
      register: asn_assignment

    - name: Update an ASN pool
      juniper.apstra.resource_pools:
        type: asn
        id:
          asn_pool: "{{ asn_pool.id.asn_pool }}"
        body:
          display_name: "Updated-ASN-Pool"
          ranges:
            - first: 65000
              last: 65200
        state: present

    - name: Unassign ASN pool from blueprint before deletion
      ansible.builtin.uri:
        url: "{{ apstra_api_url }}/blueprints/{{ blueprint_id }}/resource_groups/asn/{{ asn_resource_group.group_name }}"
        method: PUT
        headers:
          AuthToken: "{{ auth_token }}"
          Content-Type: "application/json"
        body_format: json
        body:
          pool_ids: []
        validate_certs: false
        status_code: [200, 202, 204]

    - name: Delete an ASN pool
      juniper.apstra.resource_pools:
        type: asn
        id:
          asn_pool: "{{ asn_pool.id.asn_pool }}"
        state: absent

    # ── IP Pool CRUD with Blueprint Assignment ──────────────────────────

    - name: Create an IP pool
      juniper.apstra.resource_pools:
        type: ip
        body:
          display_name: "Test-IP-Pool"
          subnets:
            - network: "10.100.0.0/16"
        state: present
      register: ip_pool

    - name: Show IP pool total and used_percentage
      ansible.builtin.debug:
        msg: "IP Pool {{ item.key }} - total: {{ item.value.total }}, used_percentage: {{ item.value.used_percentage }}"
      loop: "{{ ansible_facts.apstra_facts.ip_pools | dict2items }}"
      loop_control:
        label: "{{ item.key }}"

    - name: Find IP resource group
      ansible.builtin.set_fact:
        ip_resource_group: >-
          {{ resource_groups.json.items
             | selectattr('resource_type', 'equalto', 'ip')
             | first }}

    - name: Assign IP pool to blueprint
      ansible.builtin.uri:
        url: "{{ apstra_api_url }}/blueprints/{{ blueprint_id }}/resource_groups/ip/{{ ip_resource_group.group_name }}"
        method: PUT
        headers:
          AuthToken: "{{ auth_token }}"
          Content-Type: "application/json"
        body_format: json
        body:
          pool_ids:
            - "{{ ip_pool.id.ip_pool }}"
        validate_certs: false
        status_code: [200, 202, 204]

    - name: Update an IP pool
      juniper.apstra.resource_pools:
        type: ip
        id:
          ip_pool: "{{ ip_pool.id.ip_pool }}"
        body:
          display_name: "Updated-IP-Pool"
          subnets:
            - network: "10.100.0.0/16"
            - network: "10.200.0.0/16"
        state: present

    - name: Unassign IP pool from blueprint before deletion
      ansible.builtin.uri:
        url: "{{ apstra_api_url }}/blueprints/{{ blueprint_id }}/resource_groups/ip/{{ ip_resource_group.group_name }}"
        method: PUT
        headers:
          AuthToken: "{{ auth_token }}"
          Content-Type: "application/json"
        body_format: json
        body:
          pool_ids: []
        validate_certs: false
        status_code: [200, 202, 204]

    - name: Delete an IP pool
      juniper.apstra.resource_pools:
        type: ip
        id:
          ip_pool: "{{ ip_pool.id.ip_pool }}"
        state: absent

    # ── VLAN Pool CRUD with Blueprint Assignment ────────────────────────

    - name: Create a VLAN pool
      juniper.apstra.resource_pools:
        type: vlan
        body:
          display_name: "Test-VLAN-Pool"
          ranges:
            - first: 100
              last: 200
        state: present
      register: vlan_pool

    - name: Show VLAN pool total and used_percentage
      ansible.builtin.debug:
        msg: "VLAN Pool {{ item.key }} - total: {{ item.value.total }}, used_percentage: {{ item.value.used_percentage }}"
      loop: "{{ ansible_facts.apstra_facts.vlan_pools | dict2items }}"
      loop_control:
        label: "{{ item.key }}"

    - name: Find VLAN resource group
      ansible.builtin.set_fact:
        vlan_resource_group: >-
          {{ resource_groups.json.items
             | selectattr('resource_type', 'equalto', 'vlan')
             | first }}

    - name: Assign VLAN pool to blueprint
      ansible.builtin.uri:
        url: "{{ apstra_api_url }}/blueprints/{{ blueprint_id }}/resource_groups/vlan/{{ vlan_resource_group.group_name }}"
        method: PUT
        headers:
          AuthToken: "{{ auth_token }}"
          Content-Type: "application/json"
        body_format: json
        body:
          pool_ids:
            - "{{ vlan_pool.id.vlan_pool }}"
        validate_certs: false
        status_code: [200, 202, 204]

    - name: Update a VLAN pool
      juniper.apstra.resource_pools:
        type: vlan
        id:
          vlan_pool: "{{ vlan_pool.id.vlan_pool }}"
        body:
          display_name: "Updated-VLAN-Pool"
          ranges:
            - first: 100
              last: 300
        state: present

    - name: Unassign VLAN pool from blueprint before deletion
      ansible.builtin.uri:
        url: "{{ apstra_api_url }}/blueprints/{{ blueprint_id }}/resource_groups/vlan/{{ vlan_resource_group.group_name }}"
        method: PUT
        headers:
          AuthToken: "{{ auth_token }}"
          Content-Type: "application/json"
        body_format: json
        body:
          pool_ids: []
        validate_certs: false
        status_code: [200, 202, 204]

    - name: Delete a VLAN pool
      juniper.apstra.resource_pools:
        type: vlan
        id:
          vlan_pool: "{{ vlan_pool.id.vlan_pool }}"
        state: absent

    # ── IPv6 Pool CRUD with Blueprint Assignment ────────────────────────

    - name: Create an IPv6 pool
      juniper.apstra.resource_pools:
        type: ipv6
        body:
          display_name: "Test-IPv6-Pool"
          subnets:
            - network: "fc01:a05:fab::/48"
        state: present
      register: ipv6_pool

    - name: Show IPv6 pool total and used_percentage
      ansible.builtin.debug:
        msg: "IPv6 Pool {{ item.key }} - total: {{ item.value.total }}, used_percentage: {{ item.value.used_percentage }}"
      loop: "{{ ansible_facts.apstra_facts.ipv6_pools | dict2items }}"
      loop_control:
        label: "{{ item.key }}"

    - name: Find IPv6 resource group
      ansible.builtin.set_fact:
        ipv6_resource_group: >-
          {{ resource_groups.json.items
             | selectattr('resource_type', 'equalto', 'ipv6')
             | first }}

    - name: Assign IPv6 pool to blueprint
      ansible.builtin.uri:
        url: "{{ apstra_api_url }}/blueprints/{{ blueprint_id }}/resource_groups/ipv6/{{ ipv6_resource_group.group_name }}"
        method: PUT
        headers:
          AuthToken: "{{ auth_token }}"
          Content-Type: "application/json"
        body_format: json
        body:
          pool_ids:
            - "{{ ipv6_pool.id.ipv6_pool }}"
        validate_certs: false
        status_code: [200, 202, 204]

    - name: Update an IPv6 pool
      juniper.apstra.resource_pools:
        type: ipv6
        id:
          ipv6_pool: "{{ ipv6_pool.id.ipv6_pool }}"
        body:
          display_name: "Updated-IPv6-Pool"
          subnets:
            - network: "fc01:a05:fab::/48"
            - network: "fc01:a05:fac::/48"
        state: present

    - name: Unassign IPv6 pool from blueprint before deletion
      ansible.builtin.uri:
        url: "{{ apstra_api_url }}/blueprints/{{ blueprint_id }}/resource_groups/ipv6/{{ ipv6_resource_group.group_name }}"
        method: PUT
        headers:
          AuthToken: "{{ auth_token }}"
          Content-Type: "application/json"
        body_format: json
        body:
          pool_ids: []
        validate_certs: false
        status_code: [200, 202, 204]

    - name: Delete an IPv6 pool
      juniper.apstra.resource_pools:
        type: ipv6
        id:
          ipv6_pool: "{{ ipv6_pool.id.ipv6_pool }}"
        state: absent

    # ── Integer Pool CRUD ───────────────────────────────────────────────

    - name: Create an Integer pool
      juniper.apstra.resource_pools:
        type: integer
        body:
          display_name: "Test-Integer-Pool"
          ranges:
            - first: 1000
              last: 2000
        state: present
      register: integer_pool

    - name: Show Integer pool total and used_percentage
      ansible.builtin.debug:
        msg: "Integer Pool {{ item.key }} - total: {{ item.value.total }}, used_percentage: {{ item.value.used_percentage }}"
      loop: "{{ ansible_facts.apstra_facts.integer_pools | dict2items }}"
      loop_control:
        label: "{{ item.key }}"

    - name: Update an Integer pool
      juniper.apstra.resource_pools:
        type: integer
        id:
          integer_pool: "{{ integer_pool.id.integer_pool }}"
        body:
          display_name: "Updated-Integer-Pool"
          ranges:
            - first: 1000
              last: 2000
            - first: 3000
              last: 4000
        state: present

    - name: Delete an Integer pool
      juniper.apstra.resource_pools:
        type: integer
        id:
          integer_pool: "{{ integer_pool.id.integer_pool }}"
        state: absent

    # ── VNI Pool CRUD with Blueprint Assignment ─────────────────────────

    - name: Create a VNI pool
      juniper.apstra.resource_pools:
        type: vni
        body:
          display_name: "Test-VNI-Pool"
          ranges:
            - first: 5000
              last: 6000
        state: present
      register: vni_pool

    - name: Show VNI pool total and used_percentage
      ansible.builtin.debug:
        msg: "VNI Pool {{ item.key }} - total: {{ item.value.total }}, used_percentage: {{ item.value.used_percentage }}"
      loop: "{{ ansible_facts.apstra_facts.vni_pools | dict2items }}"
      loop_control:
        label: "{{ item.key }}"

    - name: Find VNI resource group
      ansible.builtin.set_fact:
        vni_resource_group: >-
          {{ resource_groups.json.items
             | selectattr('resource_type', 'equalto', 'vni')
             | first }}

    - name: Assign VNI pool to blueprint
      ansible.builtin.uri:
        url: "{{ apstra_api_url }}/blueprints/{{ blueprint_id }}/resource_groups/vni/{{ vni_resource_group.group_name }}"
        method: PUT
        headers:
          AuthToken: "{{ auth_token }}"
          Content-Type: "application/json"
        body_format: json
        body:
          pool_ids:
            - "{{ vni_pool.id.vni_pool }}"
        validate_certs: false
        status_code: [200, 202, 204]

    - name: Update a VNI pool
      juniper.apstra.resource_pools:
        type: vni
        id:
          vni_pool: "{{ vni_pool.id.vni_pool }}"
        body:
          display_name: "Updated-VNI-Pool"
          ranges:
            - first: 5000
              last: 7000
        state: present

    - name: Unassign VNI pool from blueprint before deletion
      ansible.builtin.uri:
        url: "{{ apstra_api_url }}/blueprints/{{ blueprint_id }}/resource_groups/vni/{{ vni_resource_group.group_name }}"
        method: PUT
        headers:
          AuthToken: "{{ auth_token }}"
          Content-Type: "application/json"
        body_format: json
        body:
          pool_ids: []
        validate_certs: false
        status_code: [200, 202, 204]

    - name: Delete a VNI pool
      juniper.apstra.resource_pools:
        type: vni
        id:
          vni_pool: "{{ vni_pool.id.vni_pool }}"
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

      .. _ansible_collections.juniper.apstra.resource_pools_module__return-changed:

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

      .. _ansible_collections.juniper.apstra.resource_pools_module__return-changes:

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

      .. _ansible_collections.juniper.apstra.resource_pools_module__return-id:

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

      The ID of the resource pool.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on create, or when object identified by display\_name

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"asn\_pool": "550e8400\-e29b\-41d4\-a716\-446655440000"}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.juniper.apstra.resource_pools_module__return-msg:

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

      .. _ansible_collections.juniper.apstra.resource_pools_module__return-response:

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

      The resource pool object details.


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

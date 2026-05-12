.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. Anchors

.. _ansible_collections.juniper.apstra.interconnect_gateway_module:

.. Anchors: short name for ansible.builtin

.. Title

juniper.apstra.interconnect_gateway module -- Manage EVPN Interconnect Domains and their Gateways in Apstra blueprints
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `juniper.apstra collection <https://galaxy.ansible.com/ui/repo/published/juniper/apstra/>`_ (version 1.0.6).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install juniper.apstra`.

    To use it in a playbook, specify: :code:`juniper.apstra.interconnect_gateway`.

.. version_added

.. rst-class:: ansible-version-added

New in juniper.apstra 0.2.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module manages both EVPN Interconnect Domains and Interconnect Domain Gateways within an Apstra blueprint.
- Use :literal:`type=domain` to manage Interconnect Domains (EVPN Interconnect Groups) that group sites for EVPN\-based DCI.
- Use :literal:`type=gateway` (the default) to manage Interconnect Domain Gateways — remote EVPN gateways linked to an Interconnect Domain.
- The equivalent Terraform resources are :literal:`apstra\_datacenter\_interconnect\_domain` and :literal:`apstra\_datacenter\_interconnect\_domain\_gateway`.


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

      .. _ansible_collections.juniper.apstra.interconnect_gateway_module__parameter-api_url:

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

      .. _ansible_collections.juniper.apstra.interconnect_gateway_module__parameter-auth_token:

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

      .. _ansible_collections.juniper.apstra.interconnect_gateway_module__parameter-body:

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

      Dictionary containing the resource details.

      For :literal:`type=domain`\ :

      :literal:`label` (string) \- Domain name (required for create).

      :literal:`route\_target` (string) \- Interconnect Route Target in :literal:`\<asn\>:\<nn\>` format (required for create).

      :literal:`esi\_mac` (string) \- Optional per\-site ESI MAC address.

      :literal:`security\_zones` (dict) \- DCI Layer\-3 (Type\-5) settings keyed by VRF label or ID (auto\-resolved). Each value is a dict with :literal:`routing\_policy\_id` (label or ID, auto\-resolved), :literal:`interconnect\_route\_target` (string), and :literal:`enabled\_for\_l3` (bool). Optional.

      :literal:`virtual\_networks` (dict) \- VN connection type settings keyed by virtual network label or ID (auto\-resolved). Each value is a dict with :literal:`l2` (bool), :literal:`l3` (bool), and :literal:`translation\_vni` (integer). Optional.

      For :literal:`type=gateway`\ :

      :literal:`gw\_name` (string) \- Gateway name (required for create).

      :literal:`gw\_ip` (string) \- Gateway IPv4 address (required for create).

      :literal:`gw\_asn` (integer) \- Gateway AS number, 1\-4294967295 (required for create).

      :literal:`local\_gw\_nodes` (list) \- IDs or labels of leaf switches that peer with this gateway (required for create).

      :literal:`evpn\_interconnect\_group\_id` (string) \- ID of the parent Interconnect Domain (required for create).

      :literal:`ttl` (integer) \- BGP TTL in hops (optional).

      :literal:`keepalive\_timer` (integer) \- BGP keepalive in seconds (optional).

      :literal:`holdtime\_timer` (integer) \- BGP hold time in seconds (optional).

      :literal:`password` (string) \- BGP session password (optional).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id"></div>

      .. _ansible_collections.juniper.apstra.interconnect_gateway_module__parameter-id:

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

      Dictionary containing the blueprint and resource IDs.

      :literal:`blueprint` is always required.

      For :literal:`type=domain`\ : :literal:`evpn\_interconnect\_group` is optional for create (looked up by :literal:`label` for idempotency), required for update/delete.

      For :literal:`type=gateway`\ : :literal:`remote\_gateway` is optional for create (looked up by :literal:`gw\_name` for idempotency), required for update/delete.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.juniper.apstra.interconnect_gateway_module__parameter-password:

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

      .. _ansible_collections.juniper.apstra.interconnect_gateway_module__parameter-state:

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

      Desired state of the resource.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"absent"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-type"></div>

      .. _ansible_collections.juniper.apstra.interconnect_gateway_module__parameter-type:

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

      The type of interconnect resource to manage.

      :literal:`domain` manages Interconnect Domains (EVPN Interconnect Groups). Body fields are :literal:`label`\ , :literal:`route\_target`\ , and optional :literal:`esi\_mac`.

      :literal:`gateway` manages Interconnect Domain Gateways (remote gateways linked to a domain). Body fields are :literal:`gw\_name`\ , :literal:`gw\_ip`\ , :literal:`gw\_asn`\ , :literal:`local\_gw\_nodes`\ , and :literal:`evpn\_interconnect\_group\_id`.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"domain"`
      - :ansible-option-choices-entry-default:`"gateway"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.juniper.apstra.interconnect_gateway_module__parameter-username:

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

      .. _ansible_collections.juniper.apstra.interconnect_gateway_module__parameter-verify_certificates:

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

    # ---- Interconnect Domain (type: domain) ----

    # Create an Interconnect Domain (blueprint may be name or UUID)
    - name: Create interconnect domain
      juniper.apstra.interconnect_gateway:
        type: domain
        id:
          blueprint: "my-datacenter-blueprint"
        body:
          label: "dci-domain-1"
          route_target: "65500:100"
        state: present
      register: icd

    # Create domain with ESI MAC
    - name: Create interconnect domain with ESI MAC
      juniper.apstra.interconnect_gateway:
        type: domain
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
        body:
          label: "dci-domain-2"
          route_target: "65500:200"
          esi_mac: "02:00:00:00:00:01"
        state: present
      register: icd_2

    # Update a domain by providing its ID
    - name: Update interconnect domain route_target by ID
      juniper.apstra.interconnect_gateway:
        type: domain
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
          evpn_interconnect_group: "{{ icd.id.evpn_interconnect_group }}"
        body:
          label: "dci-domain-1"
          route_target: "65500:101"
        state: present

    # Update a domain by label (no ID needed — looked up automatically)
    - name: Update interconnect domain by label
      juniper.apstra.interconnect_gateway:
        type: domain
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
        body:
          label: "dci-domain-1"
          route_target: "65500:102"
        state: present

    # Delete a domain by explicit ID
    - name: Delete interconnect domain by ID
      juniper.apstra.interconnect_gateway:
        type: domain
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
          evpn_interconnect_group: "{{ icd.id.evpn_interconnect_group }}"
        state: absent

    # Delete a domain by label (no evpn_interconnect_group ID needed)
    - name: Delete interconnect domain by label
      juniper.apstra.interconnect_gateway:
        type: domain
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
        body:
          label: "dci-domain-2"
        state: absent

    # ---- DCI Layer-3 (Type-5) via security_zones ----

    # Enable L3 DCI on a VRF with a routing policy and route target.
    # VRF labels and routing policy labels are resolved automatically.
    - name: Enable L3 DCI on interconnect domain
      juniper.apstra.interconnect_gateway:
        type: domain
        id:
          blueprint: "my-datacenter-blueprint"
        body:
          label: "dci-domain-1"
          route_target: "65500:100"
          security_zones:
            "my-vrf":
              routing_policy_id: "dci-l3-policy"
              interconnect_route_target: "65500:200"
              enabled_for_l3: true
        state: present

    # ---- VN Connection Type via virtual_networks ----

    # Set L2+L3 connection type and translation VNI for a virtual network.
    # VN labels are resolved automatically.
    - name: Set VN connection type with translation VNI
      juniper.apstra.interconnect_gateway:
        type: domain
        id:
          blueprint: "my-datacenter-blueprint"
        body:
          label: "dci-domain-1"
          route_target: "65500:100"
          virtual_networks:
            "my-virtual-network":
              l2: true
              l3: true
              translation_vni: 10100
        state: present

    # ---- Interconnect Domain Gateway (type: gateway) ----

    # Create a gateway — local_gw_nodes accepts system labels OR raw node IDs.
    # evpn_interconnect_group_id accepts the domain label OR its UUID.
    - name: Create interconnect gateway using system labels and domain label
      juniper.apstra.interconnect_gateway:
        id:
          blueprint: "my-datacenter-blueprint"
        body:
          gw_name: "remote-dc2-gw"
          gw_ip: "10.1.0.1"
          gw_asn: 65500
          evpn_interconnect_group_id: "dci-domain-1"
          local_gw_nodes:
            - "border-leaf-1"
            - "border-leaf-2"
          ttl: 2
          keepalive_timer: 10
          holdtime_timer: 30
        state: present
      register: icgw

    # Create a gateway using raw node IDs and domain UUID
    - name: Create interconnect gateway using raw IDs
      juniper.apstra.interconnect_gateway:
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
        body:
          gw_name: "remote-dc2-gw"
          gw_ip: "10.1.0.1"
          gw_asn: 65500
          evpn_interconnect_group_id: "{{ icd.id.evpn_interconnect_group }}"
          local_gw_nodes:
            - "PPbnMs25oIuO8WHldA"
            - "QCbnMs25oIuO8WHldB"
          ttl: 2
        state: present
      register: icgw

    # Update a gateway by providing its ID
    - name: Update interconnect gateway by ID
      juniper.apstra.interconnect_gateway:
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
          remote_gateway: "{{ icgw.id.remote_gateway }}"
        body:
          gw_name: "remote-dc2-gw"
          gw_ip: "10.1.0.2"
          gw_asn: 65500
          evpn_interconnect_group_id: "{{ icd.id.evpn_interconnect_group }}"
          local_gw_nodes:
            - "border-leaf-1"
        state: present

    # Update a gateway by name lookup (no remote_gateway ID needed)
    - name: Update interconnect gateway by gw_name
      juniper.apstra.interconnect_gateway:
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
        body:
          gw_name: "remote-dc2-gw"
          gw_ip: "10.1.0.3"
          gw_asn: 65500
          evpn_interconnect_group_id: "dci-domain-1"
          local_gw_nodes:
            - "border-leaf-1"
        state: present

    # Delete an interconnect gateway by ID
    - name: Delete interconnect gateway
      juniper.apstra.interconnect_gateway:
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
          remote_gateway: "{{ icgw.id.remote_gateway }}"
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

      .. _ansible_collections.juniper.apstra.interconnect_gateway_module__return-changed:

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

      .. _ansible_collections.juniper.apstra.interconnect_gateway_module__return-changes:

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
        <div class="ansibleOptionAnchor" id="return-evpn_interconnect_group"></div>

      .. _ansible_collections.juniper.apstra.interconnect_gateway_module__return-evpn_interconnect_group:

      .. rst-class:: ansible-option-title

      **evpn_interconnect_group**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-evpn_interconnect_group" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The interconnect domain object (type=domain).


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when type=domain and state=present


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-id"></div>

      .. _ansible_collections.juniper.apstra.interconnect_gateway_module__return-id:

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

      The ID dictionary. For type=domain contains :literal:`blueprint` and :literal:`evpn\_interconnect\_group`. For type=gateway contains :literal:`blueprint` and :literal:`remote\_gateway`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on create, or when object identified by label/gw\_name


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.juniper.apstra.interconnect_gateway_module__return-msg:

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
        <div class="ansibleOptionAnchor" id="return-remote_gateway"></div>

      .. _ansible_collections.juniper.apstra.interconnect_gateway_module__return-remote_gateway:

      .. rst-class:: ansible-option-title

      **remote_gateway**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-remote_gateway" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The interconnect gateway object (type=gateway).


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when type=gateway and state=present


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-response"></div>

      .. _ansible_collections.juniper.apstra.interconnect_gateway_module__return-response:

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

      The resource object details.


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

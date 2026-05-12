.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. Anchors

.. _ansible_collections.juniper.apstra.virtual_infra_manager_module:

.. Anchors: short name for ansible.builtin

.. Title

juniper.apstra.virtual_infra_manager module -- Manage Virtual Infrastructure Managers in Apstra
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `juniper.apstra collection <https://galaxy.ansible.com/ui/repo/published/juniper/apstra/>`_ (version 1.0.6).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install juniper.apstra`.

    To use it in a playbook, specify: :code:`juniper.apstra.virtual_infra_manager`.

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

- Provides create, read, update and delete operations for Virtual Infrastructure Managers (VIMs) in Apstra.
- Supports two scopes depending on whether :literal:`blueprint` is provided in the :literal:`id` parameter.
- :strong:`Global scope` (no :literal:`blueprint` in :literal:`id`\ ) manages VIM definitions in the :literal:`External Systems \> Virtual Infra Managers` catalog at :literal:`/api/virtual\-infra\-managers`. These are the connection definitions to vCenter, NSX, or Nutanix environments.
- :strong:`Blueprint scope` (\ :literal:`blueprint` in :literal:`id`\ ) manages the VIM nodes assigned to a specific blueprint at :literal:`/api/blueprints/{id}/virtual\_infra`. This is where a global VIM is linked to a blueprint, specifying :literal:`infra\_type` and :literal:`system\_id`.


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

      .. _ansible_collections.juniper.apstra.virtual_infra_manager_module__parameter-api_url:

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

      .. _ansible_collections.juniper.apstra.virtual_infra_manager_module__parameter-auth_token:

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

      .. _ansible_collections.juniper.apstra.virtual_infra_manager_module__parameter-body:

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

      Dictionary containing the configuration to create or update.

      :strong:`Global scope` key fields — :literal:`display\_name` (str) human\-readable name for the VIM; :literal:`virtual\_infra\_type` (str) platform type :literal:`vcenter`\ /\ :literal:`nsx`\ / :literal:`nutanix`\ ; :literal:`management\_ip` (str) management IP or hostname; :literal:`username` (str) and :literal:`password` (str) login credentials; :literal:`port` (int) optional management port.

      :strong:`Blueprint scope` key fields — :literal:`infra\_type` (str) one of :literal:`vcenter`\ , :literal:`nsxt`\ , :literal:`nutanix`\ , :literal:`nsx`\ ; :literal:`agent\_id` (str) the VIM UUID (\ :literal:`id.virtual\_infra\_manager` from the global VIM create); :literal:`system\_id` (str) the Apstra system identifier found in the VIM's top\-level :literal:`system\_id` field after the VIM connects to vCenter. Both :literal:`agent\_id` and :literal:`system\_id` are required when creating a blueprint virtual\_infra entry.

      :strong:`Shorthand` — instead of specifying :literal:`agent\_id` and :literal:`system\_id` manually, provide :literal:`vim\_ip` (the VIM's management IP address) and the module will look up the matching VIM automatically, resolving both :literal:`agent\_id` and :literal:`system\_id` from the global VIM list. Requires the VIM to be already connected to vCenter (so that :literal:`system\_id` is populated).

      :strong:`VLAN Remediation Policy` — when creating or updating a blueprint virtual\_infra node, include :literal:`vlan\_remediation\_policy` (str) in the body to set the VLAN remediation behaviour. Accepted values depend on the Apstra version; common values are :literal:`drop` (default) and :literal:`remediate`. This field is passed through to the API as\-is.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id"></div>

      .. _ansible_collections.juniper.apstra.virtual_infra_manager_module__parameter-id:

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

      Dictionary containing identifiers.

      :strong:`Global scope` — omit :literal:`blueprint`. Use :literal:`virtual\_infra\_manager` (UUID or display\_name) for get/update/delete.

      :strong:`Blueprint scope` — include :literal:`blueprint` (UUID or label). Use :literal:`virtual\_infra` (UUID) for get/update/delete an existing node.

      :strong:`vcenter scope` — when :literal:`scope=vcenter`\ , optionally include :literal:`vcenter` (UUID) to target a specific vCenter instance under the VIM. Omit :literal:`vcenter` to operate on the vCenters collection (list or create).

      :strong:`anomaly\_resolver scope` — blueprint only. Triggers the virtual\-infra VLAN\-match anomaly resolver at :literal:`/api/blueprints/{id}/virtual\_infra/predefined\_probes/virtual\_infra\_vlan\_match/anomaly\_resolver`. Requires :literal:`id.blueprint`. Body is passed through as\-is.

      :strong:`query\_vm scope` — blueprint only. Queries the VM inventory for a blueprint at :literal:`/api/blueprints/{id}/virtual\_infra/query/vm`. Requires :literal:`id.blueprint`. Body contains the query parameters.

      :strong:`vnet scope` — blueprint only. Retrieves virtual\-network details from the virtual\-infra layer at :literal:`/api/blueprints/{id}/virtual\_infra/vnet/{vnet\_id}`. Requires :literal:`id.blueprint` and :literal:`id.vnet` (UUID).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.juniper.apstra.virtual_infra_manager_module__parameter-password:

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

      The Apstra password for authentication.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-scope"></div>

      .. _ansible_collections.juniper.apstra.virtual_infra_manager_module__parameter-scope:

      .. rst-class:: ansible-option-title

      **scope**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-scope" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Selects the sub\-resource to operate on.

      :literal:`manager` (default) — the VIM itself at :literal:`/api/virtual\-infra\-managers/{id}`. Global scope only.

      :literal:`vcenter` — the vCenter instances at :literal:`/api/virtual\-infra\-managers/{id}/vcenters` and :literal:`/api/virtual\-infra\-managers/{id}/vcenters/{vcenter\_id}`. Requires :literal:`id.virtual\_infra\_manager` to be set. Supports full CRUD — list, create, get, PATCH, PUT, and delete — via direct API calls. Global scope only. :strong:`Note:`\  The :literal:`create` operation (\ :literal:`state=present` with a body and no :literal:`id.vcenter`\ ) is only supported for VIMs of type :literal:`virtual\_infra\_type=nsx`. For :literal:`vcenter`\ \-type VIMs the :literal:`/vcenters` endpoint is read\-only and Apstra returns HTTP 422 ("Vcenters can be added to virtual infra manager of the type NSX only"). List (\ :literal:`state=present` without a body) works for all VIM types.

      :literal:`anomaly\_resolver` — POSTs to :literal:`/api/blueprints/{id}/virtual\_infra/predefined\_probes/virtual\_infra\_vlan\_match/anomaly\_resolver` to trigger auto\-resolution of virtual\-infra VLAN\-match anomalies. Blueprint scope only (requires :literal:`id.blueprint`\ ).

      :literal:`query\_vm` — POSTs to :literal:`/api/blueprints/{id}/virtual\_infra/query/vm` to query the VM inventory visible through the blueprint's virtual\-infra layer. Returns :literal:`result.vms` list. Blueprint scope only.

      :literal:`vnet` — GETs :literal:`/api/blueprints/{id}/virtual\_infra/vnet/{vnet\_id}` to retrieve virtual\-network details from the virtual\-infra layer. Requires :literal:`id.vnet` (UUID). Blueprint scope only.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"manager"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"vcenter"`
      - :ansible-option-choices-entry:`"anomaly\_resolver"`
      - :ansible-option-choices-entry:`"query\_vm"`
      - :ansible-option-choices-entry:`"vnet"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.juniper.apstra.virtual_infra_manager_module__parameter-state:

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

      Desired state.

      :literal:`present` — create, or partially update (PATCH).

      :literal:`replaced` — fully replace an existing object (PUT). For :literal:`scope=manager` requires :literal:`id.virtual\_infra\_manager`. For :literal:`scope=vcenter` requires :literal:`id.vcenter`.

      :literal:`absent` — delete.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"replaced"`
      - :ansible-option-choices-entry:`"absent"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.juniper.apstra.virtual_infra_manager_module__parameter-username:

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

      The Apstra username for authentication.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-verify_certificates"></div>

      .. _ansible_collections.juniper.apstra.virtual_infra_manager_module__parameter-verify_certificates:

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

    # ── Global scope: create a vCenter VIM ───────────────────────────

    - name: Create global vCenter VIM
      juniper.apstra.virtual_infra_manager:
        body:
          display_name: "prod-vcenter"
          virtual_infra_type: "vcenter"
          management_ip: "vcenter.example.com"
          username: "administrator@vsphere.local"
          password: "S3cret!"
        state: present
      register: vim_result

    - name: Show created VIM ID
      ansible.builtin.debug:
        var: vim_result.id.virtual_infra_manager

    # ── Global scope: update by display_name ─────────────────────────

    - name: Update VIM management_ip by display_name (auto-resolved to ID)
      juniper.apstra.virtual_infra_manager:
        id:
          virtual_infra_manager: "prod-vcenter"   # display_name works
        body:
          management_ip: "vcenter2.example.com"
        state: present

    # ── Global scope: update by UUID ─────────────────────────────────

    - name: Update VIM by UUID
      juniper.apstra.virtual_infra_manager:
        id:
          virtual_infra_manager: "{{ vim_result.id.virtual_infra_manager }}"
        body:
          management_ip: "vcenter2.example.com"
        state: present

    # ── Global scope: delete ─────────────────────────────────────────

    - name: Delete global VIM by UUID
      juniper.apstra.virtual_infra_manager:
        id:
          virtual_infra_manager: "{{ vim_result.id.virtual_infra_manager }}"
        state: absent

    - name: Delete global VIM by display_name
      juniper.apstra.virtual_infra_manager:
        id:
          virtual_infra_manager: "prod-vcenter"
        state: absent

    # ── Global scope: full replace via PUT (state=replaced) ─────────

    - name: Fully replace a VIM definition (PUT)
      juniper.apstra.virtual_infra_manager:
        id:
          virtual_infra_manager: "{{ vim_result.id.virtual_infra_manager }}"
        body:
          display_name: "prod-vcenter"
          virtual_infra_type: "vcenter"
          management_ip: "vcenter3.example.com"
          username: "administrator@vsphere.local"
          password: "NewPass123!"
        state: replaced

    # ── Global scope: list vCenters for a VIM (scope=vcenter) ────────

    - name: List all vCenters under a VIM
      juniper.apstra.virtual_infra_manager:
        id:
          virtual_infra_manager: "{{ vim_result.id.virtual_infra_manager }}"
        scope: vcenter
        state: present
      register: vcenter_list

    - name: Show vCenters
      ansible.builtin.debug:
        var: vcenter_list.vcenters

    # ── Global scope: create a vCenter under a VIM ───────────────────

    - name: Add a vCenter instance to a VIM (NSX-type VIM only)
      juniper.apstra.virtual_infra_manager:
        id:
          virtual_infra_manager: "{{ vim_result.id.virtual_infra_manager }}"
        scope: vcenter
        body:
          management_ip: "vc1.example.com"
          username: "admin@vsphere.local"
          password: "VcPass!"
        state: present
      register: vcenter_created

    # ── Global scope: get a specific vCenter by ID ────────────────────

    - name: Get individual vCenter details
      juniper.apstra.virtual_infra_manager:
        id:
          virtual_infra_manager: "{{ vim_result.id.virtual_infra_manager }}"
          vcenter: "{{ vcenter_created.id.vcenter }}"
        scope: vcenter
        state: present
      register: vc_detail

    # ── Global scope: patch a specific vCenter ────────────────────────

    - name: Update vCenter credentials (PATCH)
      juniper.apstra.virtual_infra_manager:
        id:
          virtual_infra_manager: "{{ vim_result.id.virtual_infra_manager }}"
          vcenter: "{{ vcenter_created.id.vcenter }}"
        scope: vcenter
        body:
          password: "NewVcPass!"
        state: present

    # ── Global scope: replace a specific vCenter (PUT) ────────────────

    - name: Fully replace a vCenter definition (PUT)
      juniper.apstra.virtual_infra_manager:
        id:
          virtual_infra_manager: "{{ vim_result.id.virtual_infra_manager }}"
          vcenter: "{{ vcenter_created.id.vcenter }}"
        scope: vcenter
        body:
          management_ip: "vc2.example.com"
          username: "admin@vsphere.local"
          password: "VcPass!"
        state: replaced

    # ── Global scope: delete a specific vCenter ───────────────────────

    - name: Remove a vCenter from the VIM
      juniper.apstra.virtual_infra_manager:
        id:
          virtual_infra_manager: "{{ vim_result.id.virtual_infra_manager }}"
          vcenter: "{{ vcenter_created.id.vcenter }}"
        scope: vcenter
        state: absent

    # ── Blueprint scope: list all VIM nodes ─────────────────────────

    - name: List all virtual_infra nodes in a blueprint
      juniper.apstra.virtual_infra_manager:
        id:
          blueprint: "prod-dc1"
        state: present
        auth_token: "{{ auth_token }}"
      register: bp_vim_list

    - name: Show all blueprint VIM nodes
      ansible.builtin.debug:
        var: bp_vim_list.virtual_infra

    # ── Blueprint scope: assign VIM node to a blueprint ──────────────

    # Option A — explicit agent_id + system_id
    - name: Add virtual infra node to blueprint (explicit IDs)
      # agent_id = VIM UUID (id.virtual_infra_manager from the global VIM create)
      # system_id = VIM's own system_id field (returned after VIM connects to vCenter)
      # Both are REQUIRED by the Apstra API when creating a blueprint virtual_infra entry.
      juniper.apstra.virtual_infra_manager:
        id:
          blueprint: "prod-dc1"   # name or UUID
        body:
          infra_type: "vcenter"
          agent_id: "{{ vim_result.id.virtual_infra_manager }}"
          system_id: "{{ vim_result.virtual_infra_manager.system_id }}"
        state: present
      register: bp_vim

    # Option B — shorthand via vim_ip (auto-resolves agent_id + system_id)
    - name: Add virtual infra node to blueprint (by VIM IP — simpler)
      juniper.apstra.virtual_infra_manager:
        id:
          blueprint: "prod-dc1"
        body:
          infra_type: "vcenter"
          vim_ip: "10.0.0.100"   # management IP of the VIM — agent_id/system_id resolved automatically
        state: present
      register: bp_vim

    # ── Blueprint scope: assign VIM with VLAN Remediation Policy ──────

    - name: Add VIM to blueprint with VLAN remediation policy
      juniper.apstra.virtual_infra_manager:
        id:
          blueprint: "prod-dc1"
        body:
          infra_type: "vcenter"
          vim_ip: "10.0.0.100"
          vlan_remediation_policy: "remediate"   # or "drop" (default)
        state: present
      register: bp_vim

    # ── Blueprint scope: update VIM node ─────────────────────────────

    - name: Update blueprint VIM node
      juniper.apstra.virtual_infra_manager:
        id:
          blueprint: "prod-dc1"
          virtual_infra: "{{ bp_vim.id.virtual_infra }}"
        body:
          infra_type: "nsx"
        state: present

    # ── Blueprint scope: remove VIM node ─────────────────────────────

    - name: Remove virtual infra node from blueprint
      juniper.apstra.virtual_infra_manager:
        id:
          blueprint: "prod-dc1"
          virtual_infra: "{{ bp_vim.id.virtual_infra }}"
        state: absent
    # ── Blueprint scope: trigger VLAN match anomaly resolver ────────
    # POSTs to /virtual_infra/predefined_probes/virtual_infra_vlan_match/
    # anomaly_resolver and asks Apstra to auto-resolve VLAN mismatches.

    - name: Resolve virtual-infra VLAN match anomalies
      juniper.apstra.virtual_infra_manager:
        id:
          blueprint: "prod-dc1"
        scope: anomaly_resolver
        body:
          anomaly_ids: []   # empty list = resolve all
        state: present
      register: anomaly_result

    - name: Show resolver response
      ansible.builtin.debug:
        var: anomaly_result.response

    # ── Blueprint scope: query VM inventory ───────────────────────
    # POSTs a query to /virtual_infra/query/vm and returns matching VMs.

    - name: Query VMs in the virtual infra layer of a blueprint
      juniper.apstra.virtual_infra_manager:
        id:
          blueprint: "prod-dc1"
        scope: query_vm
        body:
          filter: {}
        state: present
      register: vm_query

    - name: Show VMs
      ansible.builtin.debug:
        var: vm_query.vms

    # ── Blueprint scope: get virtual-network from virtual infra layer ──
    # GETs /virtual_infra/vnet/{vnet_id} — needs id.vnet (UUID).

    - name: Get vnet details from virtual infra layer
      juniper.apstra.virtual_infra_manager:
        id:
          blueprint: "prod-dc1"
          vnet: "{{ vnet_uuid }}"
        scope: vnet
        state: present
      register: vnet_info

    - name: Show vnet
      ansible.builtin.debug:
        var: vnet_info.vnet



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

      .. _ansible_collections.juniper.apstra.virtual_infra_manager_module__return-changed:

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

      Indicates whether the module made any changes.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-changes"></div>

      .. _ansible_collections.juniper.apstra.virtual_infra_manager_module__return-changes:

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

      Dictionary of fields that were updated.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on update


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-id"></div>

      .. _ansible_collections.juniper.apstra.virtual_infra_manager_module__return-id:

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

      The resolved ID dictionary for the created or targeted object. For global scope: contains :literal:`virtual\_infra\_manager` key. For blueprint scope: contains :literal:`blueprint` and :literal:`virtual\_infra` keys.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on create or when object identified by name

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"virtual\_infra\_manager": "a1b2c3d4\-..."}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.juniper.apstra.virtual_infra_manager_module__return-msg:

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

      Human\-readable status message.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-resolved_from_vim_ip"></div>

      .. _ansible_collections.juniper.apstra.virtual_infra_manager_module__return-resolved_from_vim_ip:

      .. rst-class:: ansible-option-title

      **resolved_from_vim_ip**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-resolved_from_vim_ip" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      When :literal:`body.vim\_ip` is used, contains the resolved :literal:`vim\_ip`\ , :literal:`agent\_id`\ , and :literal:`system\_id` that were substituted into the request.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when body.vim\_ip is provided (blueprint scope)


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-response"></div>

      .. _ansible_collections.juniper.apstra.virtual_infra_manager_module__return-response:

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

      The full API response object returned on create or patch.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on create or update


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-vcenter"></div>

      .. _ansible_collections.juniper.apstra.virtual_infra_manager_module__return-vcenter:

      .. rst-class:: ansible-option-title

      **vcenter**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-vcenter" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A single vCenter instance details (scope=vcenter with id.vcenter).


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on present with scope=vcenter and id.vcenter and no body


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-vcenters"></div>

      .. _ansible_collections.juniper.apstra.virtual_infra_manager_module__return-vcenters:

      .. rst-class:: ansible-option-title

      **vcenters**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-vcenters" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of vCenter instances under the VIM (scope=vcenter, no id.vcenter).


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on present with scope=vcenter and no id.vcenter


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-virtual_infra"></div>

      .. _ansible_collections.juniper.apstra.virtual_infra_manager_module__return-virtual_infra:

      .. rst-class:: ansible-option-title

      **virtual_infra**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-virtual_infra" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`any`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Blueprint VIM node details (blueprint scope with :literal:`id.virtual\_infra`\ ), or list of all virtual\_infra nodes (blueprint scope without :literal:`id.virtual\_infra` and without body).


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on present (blueprint scope)


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-virtual_infra_manager"></div>

      .. _ansible_collections.juniper.apstra.virtual_infra_manager_module__return-virtual_infra_manager:

      .. rst-class:: ansible-option-title

      **virtual_infra_manager**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-virtual_infra_manager" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The VIM object details (global scope).


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on present (global scope)


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-vms"></div>

      .. _ansible_collections.juniper.apstra.virtual_infra_manager_module__return-vms:

      .. rst-class:: ansible-option-title

      **vms**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-vms" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of VMs returned by the scope=query\_vm POST.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on present with scope=query\_vm (blueprint scope)


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-vnet"></div>

      .. _ansible_collections.juniper.apstra.virtual_infra_manager_module__return-vnet:

      .. rst-class:: ansible-option-title

      **vnet**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-vnet" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Virtual\-network details from the virtual\-infra layer (scope=vnet).


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on present with scope=vnet (blueprint scope)


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Vijay Gavini (@vgavini)


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

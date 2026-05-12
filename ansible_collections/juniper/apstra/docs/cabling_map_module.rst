.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. Anchors

.. _ansible_collections.juniper.apstra.cabling_map_module:

.. Anchors: short name for ansible.builtin

.. Title

juniper.apstra.cabling_map module -- Manage and inspect the cabling map in an Apstra blueprint
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `juniper.apstra collection <https://galaxy.ansible.com/ui/repo/published/juniper/apstra/>`_ (version 1.0.6).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install juniper.apstra`.

    To use it in a playbook, specify: :code:`juniper.apstra.cabling_map`.

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

- Provides read and write access to the Apstra cabling map for a blueprint.
- Supports both :literal:`two\_stage\_l3clos` (datacenter) and :literal:`freeform` AOS reference designs.
- Four operations are available via the :literal:`state` parameter.
- :literal:`gathered` — return the full cabling map from :literal:`/experience/web/cabling\-map`.
- :literal:`lldp` — return raw LLDP data per system from :literal:`/cabling\-map/lldp`.
- :literal:`diff` — return the diff between LLDP data and the intended configuration from :literal:`/cabling\-map/diff`.
- :literal:`present` — update link configuration (speed, interface names, IP addresses) via :literal:`PATCH /cabling\-map`.


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

      .. _ansible_collections.juniper.apstra.cabling_map_module__parameter-api_url:

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

      .. _ansible_collections.juniper.apstra.cabling_map_module__parameter-auth_token:

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

      .. _ansible_collections.juniper.apstra.cabling_map_module__parameter-body:

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

      Parameters body for the operation.

      For :literal:`present`\ , requires a :literal:`links` list of link objects to update. Each link object must contain at least an :literal:`id` or :literal:`endpoints` key.

      For :literal:`gathered`\ , optional keys are :literal:`aggregate\_links` (bool) and :literal:`system\_node\_id` (str, UUID or system label) to filter results.

      For :literal:`lldp`\ , optional key :literal:`system\_id` (str) to filter by system. :literal:`update\_cabling\_map` (bool, default false) syncs the cabling map with LLDP\-discovered links. :literal:`create\_new\_generic` (bool, default false) creates generic systems found in LLDP but missing from the blueprint.

      For :literal:`diff`\ , optional key :literal:`check\_interface\_map` (bool, default true) to include interface map check.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`{}`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id"></div>

      .. _ansible_collections.juniper.apstra.cabling_map_module__parameter-id:

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

      Identifies the blueprint scope.

      Must contain the :literal:`blueprint` key with the blueprint ID or label.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id/blueprint"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.cabling_map_module__parameter-id/blueprint:

      .. rst-class:: ansible-option-title

      **blueprint**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-id/blueprint" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The ID or label of the blueprint.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.juniper.apstra.cabling_map_module__parameter-password:

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
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.juniper.apstra.cabling_map_module__parameter-state:

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

      The operation to perform.

      :literal:`gathered` returns the full cabling map (default).

      :literal:`lldp` returns LLDP data per system.

      :literal:`diff` returns the diff between LLDP and intended config.

      :literal:`present` updates one or more links via PATCH.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"gathered"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"lldp"`
      - :ansible-option-choices-entry:`"diff"`
      - :ansible-option-choices-entry:`"present"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.juniper.apstra.cabling_map_module__parameter-username:

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

      .. _ansible_collections.juniper.apstra.cabling_map_module__parameter-verify_certificates:

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

    # ── Gather full cabling map ───────────────────────────────────────

    - name: Get full cabling map
      juniper.apstra.cabling_map:
        id:
          blueprint: "my-blueprint"
        state: gathered
      register: cm

    - name: Show cabling map links
      ansible.builtin.debug:
        var: cm.links

    # ── Gather with filters ───────────────────────────────────────────

    - name: Get cabling map for a specific system
      juniper.apstra.cabling_map:
        id:
          blueprint: "my-blueprint"
        state: gathered
        body:
          system_node_id: "spine1"      # label or UUID
          aggregate_links: true
      register: cm_filtered

    # ── Get LLDP data ─────────────────────────────────────────────────

    - name: Get LLDP data for all systems
      juniper.apstra.cabling_map:
        id:
          blueprint: "my-blueprint"
        state: lldp
      register: lldp_data

    - name: Get LLDP data for a specific system
      juniper.apstra.cabling_map:
        id:
          blueprint: "my-blueprint"
        state: lldp
        body:
          system_id: "0C00DC7D8D00"
      register: lldp_system

    # ── Sync cabling map with LLDP data ──────────────────────────────

    - name: Update cabling map from LLDP discoveries
      juniper.apstra.cabling_map:
        id:
          blueprint: "my-blueprint"
        state: lldp
        body:
          update_cabling_map: true
      register: lldp_sync

    # ── Create new generic systems from LLDP ──────────────────────────

    - name: Create generic systems found by LLDP but missing from blueprint
      juniper.apstra.cabling_map:
        id:
          blueprint: "my-blueprint"
        state: lldp
        body:
          create_new_generic: true
      register: new_generics

    - name: Sync cabling map and create new generics in one pass
      juniper.apstra.cabling_map:
        id:
          blueprint: "my-blueprint"
        state: lldp
        body:
          update_cabling_map: true
          create_new_generic: true
      register: full_sync

    # ── Get LLDP vs intended diff ─────────────────────────────────────

    - name: Get cabling map diff (LLDP vs intended)
      juniper.apstra.cabling_map:
        id:
          blueprint: "my-blueprint"
        state: diff
      register: cm_diff

    # ── Update link configuration ─────────────────────────────────────

    - name: Update interface name on a link
      juniper.apstra.cabling_map:
        id:
          blueprint: "my-blueprint"
        state: present
        body:
          links:
            - endpoints:
                - interface:
                    id: "wZWAFd5z3k4XbkOf-g"
                    if_name: "ge-0/0/2"
                - interface:
                    id: "KcvvS_lwlG1mgPSIeA"
                    if_name: "ge-0/0/1"
      register: patch_result

    - name: Update multiple links with IP addresses
      juniper.apstra.cabling_map:
        id:
          blueprint: "my-blueprint"
        state: present
        body:
          links:
            - endpoints:
                - interface:
                    id: "op0XiI2mKpOtieV8vg"
                    if_name: "ge-0/0/2"
                    ipv4_addr: "10.10.0.4/31"
                - interface:
                    id: "LVIFCDchlHEV4V-K9g"
                    if_name: "ge-0/0/0"
                    ipv4_addr: "10.10.0.5/31"
      register: patch_result

    # ── Works with freeform blueprints ───────────────────────────────

    - name: Get cabling map for a freeform blueprint
      juniper.apstra.cabling_map:
        id:
          blueprint: "my-freeform-blueprint"
        state: gathered
      register: cm_freeform



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

      .. _ansible_collections.juniper.apstra.cabling_map_module__return-changed:

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
        <div class="ansibleOptionAnchor" id="return-links"></div>

      .. _ansible_collections.juniper.apstra.cabling_map_module__return-links:

      .. rst-class:: ansible-option-title

      **links**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-links" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of link objects returned by the operation. For :literal:`gathered`\ , contains the full cabling map links. For :literal:`lldp`\ , contains LLDP\-discovered link data. For :literal:`diff`\ , contains links with differences. For :literal:`present`\ , contains the updated cabling map links.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.juniper.apstra.cabling_map_module__return-msg:

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

      A human\-readable message describing what happened.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-new_generics"></div>

      .. _ansible_collections.juniper.apstra.cabling_map_module__return-new_generics:

      .. rst-class:: ansible-option-title

      **new_generics**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-new_generics" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of new generic system items that were created (or would be created in check mode). Only returned when :literal:`state=lldp` with :literal:`body.create\_new\_generic=true` and items exist.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state is lldp and create\_new\_generic is true


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-nodes"></div>

      .. _ansible_collections.juniper.apstra.cabling_map_module__return-nodes:

      .. rst-class:: ansible-option-title

      **nodes**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-nodes" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Dictionary of per\-system LLDP data keyed by node ID. Each value contains the LLDP telemetry reported by that system (hostname, management IP, system ID, interfaces, etc.). Only returned when :literal:`state=lldp`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state is lldp


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

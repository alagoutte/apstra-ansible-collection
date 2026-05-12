.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. Anchors

.. _ansible_collections.juniper.apstra.upgrade_group_module:

.. Anchors: short name for ansible.builtin

.. Title

juniper.apstra.upgrade_group module -- Manage Apstra OS upgrade groups
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `juniper.apstra collection <https://galaxy.ansible.com/ui/repo/published/juniper/apstra/>`_ (version 1.0.6).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install juniper.apstra`.

    To use it in a playbook, specify: :code:`juniper.apstra.upgrade_group`.

.. version_added

.. rst-class:: ansible-version-added

New in juniper.apstra 0.4.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Manages OS upgrade groups in Apstra 6.1+.
- Upgrade groups are implicit — they are string labels stored in each device's :literal:`user\_config.upgrade\_group` field. There is no dedicated group resource; creating a group means assigning devices to a named group label. Dissolving a group means resetting all its members to the :literal:`default` group.
- Requires Apstra 6.1 or later. On older versions the :literal:`user\_config` field is still present but the :literal:`upgrade\_group` key may be ignored; the module will still succeed at the API level.


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

      .. _ansible_collections.juniper.apstra.upgrade_group_module__parameter-api_url:

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

      The URL used to access the Apstra API.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-auth_token"></div>

      .. _ansible_collections.juniper.apstra.upgrade_group_module__parameter-auth_token:

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

      Authentication token (if already authenticated).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body"></div>

      .. _ansible_collections.juniper.apstra.upgrade_group_module__parameter-body:

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

      Parameters for the operation.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/members"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.upgrade_group_module__parameter-body/members:

      .. rst-class:: ansible-option-title

      **members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/members" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of devices to include in the group.

      Each entry may be a blueprint node label (requires :literal:`id.blueprint`\ ), management IP address, or device key (MAC/serial).

      Required for :literal:`state=present`.

      Optional for :literal:`state=absent` — when provided, only those specific devices are removed from the group (reset to :literal:`default`\ ). When omitted the entire group is dissolved.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id"></div>

      .. _ansible_collections.juniper.apstra.upgrade_group_module__parameter-id:

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

      Identifies the upgrade group to operate on.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id/blueprint"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.upgrade_group_module__parameter-id/blueprint:

      .. rst-class:: ansible-option-title

      **blueprint**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-id/blueprint" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Blueprint UUID or label used to resolve device node labels to system IDs.

      Optional but required when :literal:`body.members` contains device labels as they appear in an Apstra blueprint (e.g. :literal:`apstra\_esi\_001\_leaf1`\ ).

      Not needed if members are specified as management IPs or device keys (MAC/serial).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id/name"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.upgrade_group_module__parameter-id/name:

      .. rst-class:: ansible-option-title

      **name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-id/name" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The upgrade group name.

      Required for :literal:`state=present`\ , :literal:`state=absent`\ , and :literal:`state=impact\_report`.

      Omit for :literal:`state=gathered` to list all groups.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.juniper.apstra.upgrade_group_module__parameter-password:

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

      Apstra password for authentication.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.juniper.apstra.upgrade_group_module__parameter-state:

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

      Desired operation.

      :literal:`present` ensures the listed :literal:`body.members` belong to the named group. Devices already in the group are left unchanged (idempotent). Devices in the group that are NOT listed are NOT removed — use :literal:`state=absent` first to dissolve cleanly.

      :literal:`absent` dissolves the group. When :literal:`body.members` is provided, only those members are removed from the group (reset to :literal:`default`\ ). When omitted, every device currently in the group is reset to :literal:`default`\ , effectively deleting the group.

      :literal:`gathered` lists all upgrade groups and their current members. Read\-only, no changes made. When :literal:`id.name` is provided only that group is returned.

      :literal:`impact\_report` runs a pre\-upgrade impact assessment for all members of the named group. Read\-only, no device changes.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"absent"`
      - :ansible-option-choices-entry:`"gathered"`
      - :ansible-option-choices-entry:`"impact\_report"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.juniper.apstra.upgrade_group_module__parameter-username:

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

      Apstra username for authentication.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-verify_certificates"></div>

      .. _ansible_collections.juniper.apstra.upgrade_group_module__parameter-verify_certificates:

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

      If false, SSL certificates are not verified.


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

    # ── List all groups and members ──────────────────────────────────

    - name: Gather all upgrade groups
      juniper.apstra.upgrade_group:
        state: gathered
      register: groups_result

    - name: Show groups
      ansible.builtin.debug:
        var: groups_result.groups

    # ── List a specific group ─────────────────────────────────────────

    - name: Gather spines group
      juniper.apstra.upgrade_group:
        id:
          name: "spines"
        state: gathered
      register: spines_group

    # ── Create a group / add devices by blueprint label ───────────────

    - name: Create "spines" upgrade group
      juniper.apstra.upgrade_group:
        id:
          name: "spines"
          blueprint: "apstra-pod1"
        body:
          members:
            - "spine1"
            - "spine2"
        state: present

    # ── Create a group using management IPs (no blueprint needed) ─────

    - name: Create "leaves" upgrade group by IP
      juniper.apstra.upgrade_group:
        id:
          name: "leaves"
        body:
          members:
            - "172.20.34.13"
            - "172.20.34.14"
            - "172.20.34.15"
        state: present

    # ── Run upgrade-impact assessment for a group ─────────────────────

    - name: Assess upgrade impact for spines group
      juniper.apstra.upgrade_group:
        id:
          name: "spines"
        state: impact_report
      register: impact

    - name: Show impact
      ansible.builtin.debug:
        var: impact.impact_report

    # ── Remove specific devices from a group ─────────────────────────

    - name: Remove spine1 from spines group
      juniper.apstra.upgrade_group:
        id:
          name: "spines"
          blueprint: "apstra-pod1"
        body:
          members:
            - "spine1"
        state: absent

    # ── Dissolve an entire group ──────────────────────────────────────

    - name: Dissolve spines group (all members go back to default)
      juniper.apstra.upgrade_group:
        id:
          name: "spines"
        state: absent

    # ── Full upgrade-group workflow ───────────────────────────────────

    - name: 1 Create spines group
      juniper.apstra.upgrade_group:
        id:
          name: "spines"
          blueprint: "{{ bp_id }}"
        body:
          members: ["spine1", "spine2"]
        state: present

    - name: 2 Impact assessment before upgrade
      juniper.apstra.upgrade_group:
        id:
          name: "spines"
        state: impact_report
      register: impact

    - name: 3a Trigger upgrade SEQUENTIALLY (one device at a time — safe default)
      juniper.apstra.os_upgrade:
        id:
          blueprint: "{{ bp_id }}"
          system: "{{ item }}"
        body:
          image: "{{ target_image }}"
          wait_timeout: 1800
        state: present
      loop: "{{ impact.agent_ids }}"
      when: not impact.failed

    # ── OR ── parallel upgrade (matches WebUI behaviour) ─────────────

    - name: 3b Trigger upgrade IN PARALLEL (all devices simultaneously — like WebUI)
      juniper.apstra.os_upgrade:
        id:
          blueprint: "{{ bp_id }}"
          system: "{{ item }}"
        body:
          image: "{{ target_image }}"
          wait_timeout: 1800
        state: present
      loop: "{{ impact.agent_ids }}"
      when: not impact.failed
      async: 1800   # must be >= wait_timeout; tells Ansible to run the task asynchronously
      poll: 0       # fire and move on immediately — do not wait before launching next device
      register: upgrade_jobs

    - name: 3b Wait for all parallel upgrades to complete
      ansible.builtin.async_status:
        jid: "{{ item.ansible_job_id }}"
      loop: "{{ upgrade_jobs.results | selectattr('ansible_job_id', 'defined') | list }}"
      register: job_results
      until: job_results.finished
      retries: 120
      delay: 30
      when: not impact.failed

    - name: 4 Dissolve group after upgrade
      juniper.apstra.upgrade_group:
        id:
          name: "spines"
        state: absent

    # ── Mixed OS types in one group (JunOS + JunOS-EVO) ───────────────
    #
    # Option A (recommended): use separate upgrade groups per OS type so
    # each group maps cleanly to one image.  Create "spines-junos" and
    # "spines-evo", then run the workflow above for each group.
    #
    # Option B: single group, filter by os_family at playbook level.
    # The gathered member dicts include os_family / os_variant / os_version
    # so you can split agent_ids into two lists and apply different images.

    - name: Gather group members (includes os_family per device)
      juniper.apstra.upgrade_group:
        id:
          name: "mixed-spines"
        state: gathered
      register: grp

    - name: Build per-OS agent lists
      ansible.builtin.set_fact:
        junos_keys: "{{ grp.groups['mixed-spines'] | selectattr('os_variant', 'ne', 'qfx-ms-fixed') | map(attribute='device_key') | list }}"
        evo_keys: "{{ grp.groups['mixed-spines'] | selectattr('os_variant', 'equalto', 'qfx-ms-fixed') | map(attribute='device_key') | list }}"

    - name: Upgrade JunOS devices
      juniper.apstra.os_upgrade:
        id:
          blueprint: "{{ bp_id }}"
          system: "{{ item }}"
        body:
          image: "jinstall-host-qfx-5e-x86-64-23.4R2-S6.10-secure-signed.tgz"
          wait_timeout: 1800
        state: present
      loop: "{{ junos_keys }}"
      async: 1800
      poll: 0
      register: junos_jobs

    - name: Upgrade JunOS-EVO devices
      juniper.apstra.os_upgrade:
        id:
          blueprint: "{{ bp_id }}"
          system: "{{ item }}"
        body:
          image: "junos-evo-install-qfx-ms-x86-64-23.4R2-S6.9-EVO.iso"
          wait_timeout: 1800
        state: present
      loop: "{{ evo_keys }}"
      async: 1800
      poll: 0
      register: evo_jobs

    - name: Wait for all upgrades to complete
      ansible.builtin.async_status:
        jid: "{{ item.ansible_job_id }}"
      loop: >-
        {{ (junos_jobs.results | default([]) + evo_jobs.results | default([]))
           | selectattr('ansible_job_id', 'defined') | list }}
      register: all_results
      until: all_results.finished
      retries: 120
      delay: 30



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
        <div class="ansibleOptionAnchor" id="return-agent_ids"></div>

      .. _ansible_collections.juniper.apstra.upgrade_group_module__return-agent_ids:

      .. rst-class:: ansible-option-title

      **agent_ids**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-agent_ids" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Agent UUIDs that were included in the impact assessment.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state=impact\_report


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-changed"></div>

      .. _ansible_collections.juniper.apstra.upgrade_group_module__return-changed:

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

      True when one or more device group assignments were modified.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-group_name"></div>

      .. _ansible_collections.juniper.apstra.upgrade_group_module__return-group_name:

      .. rst-class:: ansible-option-title

      **group_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-group_name" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The upgrade group name operated on.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state=present, absent, or impact\_report


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-groups"></div>

      .. _ansible_collections.juniper.apstra.upgrade_group_module__return-groups:

      .. rst-class:: ansible-option-title

      **groups**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-groups" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Dict mapping group name → list of member dicts. Each member dict contains :literal:`device\_key`\ , :literal:`mgmt\_ip`\ , :literal:`hostname`\ , :literal:`upgrade\_group`\ , :literal:`os\_family`\ , :literal:`os\_variant`\ , :literal:`os\_version`\ , and :literal:`user\_config` (full).


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state=gathered


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-impact_report"></div>

      .. _ansible_collections.juniper.apstra.upgrade_group_module__return-impact_report:

      .. rst-class:: ansible-option-title

      **impact_report**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-impact_report" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The upgrade\-impact response from Apstra. Contains per\-device assessment data.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state=impact\_report


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-members_changed"></div>

      .. _ansible_collections.juniper.apstra.upgrade_group_module__return-members_changed:

      .. rst-class:: ansible-option-title

      **members_changed**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-members_changed" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of device\_keys whose group assignment was changed.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state=present or absent


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-members_current"></div>

      .. _ansible_collections.juniper.apstra.upgrade_group_module__return-members_current:

      .. rst-class:: ansible-option-title

      **members_current**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-members_current" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Current members of the group after the operation. Each item contains :literal:`device\_key`\ , :literal:`mgmt\_ip`\ , :literal:`hostname`\ , :literal:`os\_family`\ , :literal:`os\_variant`\ , :literal:`os\_version`\ , and :literal:`user\_config`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state=present or absent


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.juniper.apstra.upgrade_group_module__return-msg:

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

      Human\-readable summary of the operation.


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

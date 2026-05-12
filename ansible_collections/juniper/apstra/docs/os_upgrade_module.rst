.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. Anchors

.. _ansible_collections.juniper.apstra.os_upgrade_module:

.. Anchors: short name for ansible.builtin

.. Title

juniper.apstra.os_upgrade module -- Manage device OS upgrades in an Apstra blueprint
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `juniper.apstra collection <https://galaxy.ansible.com/ui/repo/published/juniper/apstra/>`_ (version 1.0.6).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install juniper.apstra`.

    To use it in a playbook, specify: :code:`juniper.apstra.os_upgrade`.

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

- Triggers a device OS upgrade (DOS) for a single device in an Apstra blueprint.
- Waits for the upgrade job to reach a terminal state (success or error).
- Can also run an upgrade\-impact assessment (\ :literal:`state=impact\_report`\ ) or list all globally available OS images (\ :literal:`state=gathered`\ ).
- Requires Apstra 6.0+ for single\-device upgrade. Upgrade groups (\ :literal:`upgrade\_group.py`\ ) require Apstra 6.1+.


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

      .. _ansible_collections.juniper.apstra.os_upgrade_module__parameter-api_url:

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

      .. _ansible_collections.juniper.apstra.os_upgrade_module__parameter-auth_token:

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

      .. _ansible_collections.juniper.apstra.os_upgrade_module__parameter-body:

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

      A dict with runtime parameters for the operation.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/agent_ids"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.os_upgrade_module__parameter-body/agent_ids:

      .. rst-class:: ansible-option-title

      **agent_ids**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/agent_ids" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Explicit list of system\-agent UUIDs to include in an :literal:`impact\_report`.

      Ignored for :literal:`state=present`.

      When omitted (and :literal:`id.system` is not set), all agents belonging to the blueprint are assessed.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/image"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.os_upgrade_module__parameter-body/image:

      .. rst-class:: ansible-option-title

      **image**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/image" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The target OS image — accepts an image UUID, image\_name (the .tgz/.iso filename shown in the UI), or description.

      Required for :literal:`state=present`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/wait_timeout"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.os_upgrade_module__parameter-body/wait_timeout:

      .. rst-class:: ansible-option-title

      **wait_timeout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/wait_timeout" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Maximum seconds to wait for the upgrade job to complete.

      Only used by :literal:`state=present`.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`600`

      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id"></div>

      .. _ansible_collections.juniper.apstra.os_upgrade_module__parameter-id:

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

      A dict identifying the target blueprint and (for most states) device.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id/blueprint"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.os_upgrade_module__parameter-id/blueprint:

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

      The blueprint UUID or label that owns the device.

      Required for all states.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id/system"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.os_upgrade_module__parameter-id/system:

      .. rst-class:: ansible-option-title

      **system**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-id/system" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Identifies the target system agent — accepts an agent UUID, device label, or management IP address.

      Required for :literal:`state=present`.

      When provided with :literal:`state=impact\_report`\ , the assessment is scoped to that single device. Omit to assess all blueprint devices.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.juniper.apstra.os_upgrade_module__parameter-password:

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

      .. _ansible_collections.juniper.apstra.os_upgrade_module__parameter-state:

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

      Desired operation to perform.

      :literal:`present` triggers an OS upgrade on the specified device and waits for the job to reach a terminal state (success or error). The module always triggers the upgrade (non\-idempotent) — use :literal:`impact\_report` first to assess readiness.

      :literal:`impact\_report` runs a pre\-upgrade impact assessment (read\-only) and returns the assessment report without changing any device state.

      :literal:`gathered` lists all OS images currently available globally in Apstra and returns their metadata. OS images are not tied to a blueprint — they are managed globally at \`\`/device\-os/images\`\`. No changes are made.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"impact\_report"`
      - :ansible-option-choices-entry:`"gathered"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.juniper.apstra.os_upgrade_module__parameter-username:

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

      .. _ansible_collections.juniper.apstra.os_upgrade_module__parameter-verify_certificates:

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

    # ── List available OS images ──────────────────────────────────────

    - name: Gather all available OS images (globally managed, not per-blueprint)
      juniper.apstra.os_upgrade:
        id:
          blueprint: "my-blueprint"
        state: gathered
      register: images_result

    - name: Show image list
      ansible.builtin.debug:
        var: images_result.images

    # ── Assess upgrade impact (all devices) ───────────────────────────

    - name: Run upgrade-impact for all blueprint devices
      juniper.apstra.os_upgrade:
        id:
          blueprint: "my-blueprint"
        state: impact_report
      register: impact

    - name: Show impact report
      ansible.builtin.debug:
        var: impact.impact_report

    # ── Assess upgrade impact (single device) ─────────────────────────

    - name: Run upgrade-impact for spine-1 only
      juniper.apstra.os_upgrade:
        id:
          blueprint: "my-blueprint"
          system: "spine-1"
        state: impact_report
      register: spine1_impact

    # ── Trigger upgrade on a single device ────────────────────────────

    - name: Upgrade spine-1 to a specific OS image
      juniper.apstra.os_upgrade:
        id:
          blueprint: "my-blueprint"
          system: "spine-1"
        body:
          image: "junos-21.4R3-S5.9-install-media.tgz"
          wait_timeout: 900
        state: present
      register: upgrade_result

    - name: Upgrade a device using UUIDs directly
      juniper.apstra.os_upgrade:
        id:
          blueprint: "ad1cb3c1-7c83-4834-8a85-953ccf113833"
          system: "f1e2d3c4-abcd-0000-0000-000000000001"
        body:
          image: "b5a4c3d2-1111-0000-0000-000000000099"
        state: present
      register: upgrade_result

    # ── Full upgrade workflow ────────────────────────────────────────

    - name: 1 — Assess impact before upgrading
      juniper.apstra.os_upgrade:
        id:
          blueprint: "{{ bp_id }}"
          system: "leaf-1"
        state: impact_report
      register: impact
      failed_when: impact.impact_report.warnings | default([]) | length > 0

    - name: 2 — Trigger upgrade
      juniper.apstra.os_upgrade:
        id:
          blueprint: "{{ bp_id }}"
          system: "leaf-1"
        body:
          image: "{{ target_image }}"
          wait_timeout: 900
        state: present
      register: upgrade
      when: not impact.failed



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
        <div class="ansibleOptionAnchor" id="return-agent"></div>

      .. _ansible_collections.juniper.apstra.os_upgrade_module__return-agent:

      .. rst-class:: ansible-option-title

      **agent**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-agent" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Full system\-agent response dict after the job completes.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state=present


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-agent_id"></div>

      .. _ansible_collections.juniper.apstra.os_upgrade_module__return-agent_id:

      .. rst-class:: ansible-option-title

      **agent_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-agent_id" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The system\-agent UUID that was upgraded.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state=present


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-agent_ids"></div>

      .. _ansible_collections.juniper.apstra.os_upgrade_module__return-agent_ids:

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

      List of agent UUIDs included in the impact assessment.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state=impact\_report


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-blueprint_id"></div>

      .. _ansible_collections.juniper.apstra.os_upgrade_module__return-blueprint_id:

      .. rst-class:: ansible-option-title

      **blueprint_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-blueprint_id" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The resolved blueprint UUID.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-changed"></div>

      .. _ansible_collections.juniper.apstra.os_upgrade_module__return-changed:

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

      True when an upgrade was triggered (\ :literal:`state=present` only).


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-image_id"></div>

      .. _ansible_collections.juniper.apstra.os_upgrade_module__return-image_id:

      .. rst-class:: ansible-option-title

      **image_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-image_id" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The resolved OS\-image UUID used for the upgrade.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state=present


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-images"></div>

      .. _ansible_collections.juniper.apstra.os_upgrade_module__return-images:

      .. rst-class:: ansible-option-title

      **images**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-images" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of OS images available globally in Apstra (not blueprint\-scoped). Each item contains :literal:`id`\ , :literal:`image\_name`\ , :literal:`description`\ , :literal:`platform`\ , :literal:`type`\ , :literal:`image\_url`\ , :literal:`image\_size`\ , and :literal:`checksum`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state=gathered


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-impact_report"></div>

      .. _ansible_collections.juniper.apstra.os_upgrade_module__return-impact_report:

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

      The upgrade\-impact response from Apstra. Contains per\-device assessment data including warnings and expected side\-effects.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state=impact\_report


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.juniper.apstra.os_upgrade_module__return-msg:

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


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-state"></div>

      .. _ansible_collections.juniper.apstra.os_upgrade_module__return-state:

      .. rst-class:: ansible-option-title

      **state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-state" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Terminal state of the upgrade job — :literal:`success` or :literal:`error`. Only returned for :literal:`state=present`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state=present


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

.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. Anchors

.. _ansible_collections.juniper.apstra.system_agents_module:

.. Anchors: short name for ansible.builtin

.. Title

juniper.apstra.system_agents module -- Manage system agents (device onboarding) in Apstra
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `juniper.apstra collection <https://galaxy.ansible.com/ui/repo/published/juniper/apstra/>`_ (version 1.0.6).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install juniper.apstra`.

    To use it in a playbook, specify: :code:`juniper.apstra.system_agents`.

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

- This module manages system agents in Apstra for onboarding and managing network devices.
- Supports creating (onboarding), updating, and deleting system agents.
- Uses the Apstra system\-agents API via the AOS SDK.
- Provides full idempotency. Agents are matched by :literal:`management\_ip` or :literal:`agent\_id` to prevent duplicates.
- After onboarding, the agent connection state can be checked to confirm the device is reachable and authenticated.


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

      .. _ansible_collections.juniper.apstra.system_agents_module__parameter-api_url:

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

      .. _ansible_collections.juniper.apstra.system_agents_module__parameter-auth_token:

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

      .. _ansible_collections.juniper.apstra.system_agents_module__parameter-body:

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

      A dict containing the system agent specification.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/agent_type"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.system_agents_module__parameter-body/agent_type:

      .. rst-class:: ansible-option-title

      **agent_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/agent_type" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The type of system agent.

      :literal:`offbox` runs the agent in an Apstra\-managed container.

      :literal:`onbox` installs the agent directly on the device.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"offbox"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"onbox"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/device_password"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.system_agents_module__parameter-body/device_password:

      .. rst-class:: ansible-option-title

      **device_password**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/device_password" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The password for authenticating to the managed device.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/device_username"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.system_agents_module__parameter-body/device_username:

      .. rst-class:: ansible-option-title

      **device_username**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/device_username" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The username for authenticating to the managed device.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/force_package_install"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.system_agents_module__parameter-body/force_package_install:

      .. rst-class:: ansible-option-title

      **force_package_install**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/force_package_install" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Force reinstallation of agent packages.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/job_on_create"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.system_agents_module__parameter-body/job_on_create:

      .. rst-class:: ansible-option-title

      **job_on_create**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/job_on_create" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Action to trigger automatically when the agent is created.

      :literal:`check` validates device reachability; :literal:`install` deploys the agent.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"check"`
      - :ansible-option-choices-entry:`"install"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/label"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.system_agents_module__parameter-body/label:

      .. rst-class:: ansible-option-title

      **label**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/label" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      A human\-readable label for the system agent.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/management_ip"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.system_agents_module__parameter-body/management_ip:

      .. rst-class:: ansible-option-title

      **management_ip**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/management_ip" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The management IP address or hostname of the device to onboard.

      Used to create a new agent and for idempotent matching of existing agents.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/open_options"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.system_agents_module__parameter-body/open_options:

      .. rst-class:: ansible-option-title

      **open_options**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/open_options" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Device driver options passed to the agent.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/operation_mode"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.system_agents_module__parameter-body/operation_mode:

      .. rst-class:: ansible-option-title

      **operation_mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/operation_mode" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The operation mode for the agent.

      :literal:`full\_control` allows Apstra to manage the device configuration.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"full\_control"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/platform"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.system_agents_module__parameter-body/platform:

      .. rst-class:: ansible-option-title

      **platform**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/platform" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The device platform/OS family.

      Required when creating an agent without a :literal:`profile`.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"junos"`
      - :ansible-option-choices-entry:`"eos"`
      - :ansible-option-choices-entry:`"nxos"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/profile"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.system_agents_module__parameter-body/profile:

      .. rst-class:: ansible-option-title

      **profile**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/profile" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The system agent profile ID to use.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/wait_for_connection"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.system_agents_module__parameter-body/wait_for_connection:

      .. rst-class:: ansible-option-title

      **wait_for_connection**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/wait_for_connection" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      If true, wait for the agent to reach :literal:`connected` state after creation or update.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/wait_timeout"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.system_agents_module__parameter-body/wait_timeout:

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

      Maximum time in seconds to wait for the agent to connect.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`120`

      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id"></div>

      .. _ansible_collections.juniper.apstra.system_agents_module__parameter-id:

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

      A dict identifying an existing system agent.

      Not required for :literal:`state=gathered`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id/agent_id"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.system_agents_module__parameter-id/agent_id:

      .. rst-class:: ansible-option-title

      **agent_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-id/agent_id" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The ID of an existing system agent.

      Required for update and delete operations when :literal:`management\_ip` is not specified in :literal:`body`.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.juniper.apstra.system_agents_module__parameter-password:

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

      .. _ansible_collections.juniper.apstra.system_agents_module__parameter-state:

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

      Desired state of the system agent.

      :literal:`present` will create or update the agent.

      :literal:`absent` will uninstall the agent container (if running) and then delete the agent. The uninstall job runs asynchronously; the module waits up to :literal:`uninstall\_timeout` seconds for it to complete before issuing the delete.

      :literal:`gathered` lists all agents and returns their details including system\_id (device serial number). Useful for building device\-to\-serial mappings without raw API calls.

      :literal:`installed` triggers install\-agent on agents whose containers are not yet running. Accepts :literal:`body.wait\_for\_connection` and :literal:`body.wait\_timeout` to poll until all agents reach connected.

      :literal:`acknowledged` discovers unacknowledged (OOS\-QUARANTINED) systems and approves them (sets admin\_state=normal) so they become OOS\-READY for blueprint assignment.

      When :literal:`state=acknowledged` and :literal:`body.management\_ip` is provided, only the device matching that IP will be acknowledged. Without :literal:`management\_ip`\ , all unacknowledged devices are acknowledged.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"absent"`
      - :ansible-option-choices-entry:`"gathered"`
      - :ansible-option-choices-entry:`"installed"`
      - :ansible-option-choices-entry:`"acknowledged"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-uninstall_timeout"></div>

      .. _ansible_collections.juniper.apstra.system_agents_module__parameter-uninstall_timeout:

      .. rst-class:: ansible-option-title

      **uninstall_timeout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-uninstall_timeout" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Maximum time in seconds to wait for the uninstall job to finish before attempting to delete the agent.

      Only used when :literal:`state=absent` and the agent container is running.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`120`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.juniper.apstra.system_agents_module__parameter-username:

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

      .. _ansible_collections.juniper.apstra.system_agents_module__parameter-verify_certificates:

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

    # ── Onboard a device (offbox agent) ───────────────────────────────

    - name: Onboard a Junos switch
      juniper.apstra.system_agents:
        body:
          management_ip: "10.0.0.1"
          agent_type: "offbox"
          label: "spine-1"
          operation_mode: "full_control"
          device_username: "admin"
          device_password: "admin@123"
          job_on_create: "check"
        state: present
      register: agent

    # ── Onboard with platform hint ────────────────────────────────────

    - name: Onboard an EOS switch
      juniper.apstra.system_agents:
        body:
          management_ip: "10.0.0.2"
          agent_type: "offbox"
          label: "leaf-1"
          device_username: "admin"
          device_password: "Arista123"
          platform: "eos"
        state: present

    # ── Update agent label ────────────────────────────────────────────

    - name: Update agent label
      juniper.apstra.system_agents:
        id:
          agent_id: "{{ agent.agent_id }}"
        body:
          label: "spine-1-updated"
        state: present

    # ── Delete an agent ───────────────────────────────────────────────

    - name: Delete system agent
      juniper.apstra.system_agents:
        id:
          agent_id: "{{ agent.agent_id }}"
        state: absent

    # ── Delete agent by management IP ─────────────────────────────────

    - name: Delete system agent by IP
      juniper.apstra.system_agents:
        body:
          management_ip: "10.0.0.1"
        state: absent

    # ── Onboard and wait for connection ───────────────────────────────

    - name: Onboard and wait for device to connect
      juniper.apstra.system_agents:
        body:
          management_ip: "10.0.0.3"
          agent_type: "offbox"
          label: "leaf-2"
          device_username: "admin"
          device_password: "admin@123"
          wait_for_connection: true
          wait_timeout: 180
        state: present

    # ── List all agents (gather serial numbers) ───────────────────────

    - name: Gather all system agents
      juniper.apstra.system_agents:
        state: gathered
      register: all_agents

    - name: Build label-to-serial map
      ansible.builtin.set_fact:
        serial_map: >-
          {{ dict(all_agents.agents
             | selectattr('system_id')
             | map(attribute='label')
             | zip(all_agents.agents
                   | selectattr('system_id')
                   | map(attribute='system_id'))
             | list) }}
    # ── Trigger install-agent + wait for all agents to connect ────

    - name: Install agents and wait for connection
      juniper.apstra.system_agents:
        body:
          wait_for_connection: true
          wait_timeout: 180
        state: installed
      register: install_result

    # ── Acknowledge unacknowledged devices ────────────────────────

    - name: Acknowledge all quarantined devices
      juniper.apstra.system_agents:
        state: acknowledged
      register: ack_result

    # ── Acknowledge a single device by management IP ─────────────

    - name: Acknowledge one device by IP
      juniper.apstra.system_agents:
        body:
          management_ip: "10.0.0.1"
        state: acknowledged
      register: ack_one



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
        <div class="ansibleOptionAnchor" id="return-acknowledged_systems"></div>

      .. _ansible_collections.juniper.apstra.system_agents_module__return-acknowledged_systems:

      .. rst-class:: ansible-option-title

      **acknowledged_systems**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-acknowledged_systems" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of device\_key values that were acknowledged.

      Only returned when :literal:`state=acknowledged`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state=acknowledged


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-agent"></div>

      .. _ansible_collections.juniper.apstra.system_agents_module__return-agent:

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

      Full agent details from the API.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when agent exists


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-agent_id"></div>

      .. _ansible_collections.juniper.apstra.system_agents_module__return-agent_id:

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

      The ID of the system agent.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on create or when agent is found


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-agents"></div>

      .. _ansible_collections.juniper.apstra.system_agents_module__return-agents:

      .. rst-class:: ansible-option-title

      **agents**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-agents" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of all system agents with their details.

      Only returned when :literal:`state=gathered`.

      Each entry contains agent\_id, label, management\_ip, system\_id, and connection\_state.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state=gathered

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`[{"agent\_id": "abc\-123", "connection\_state": "connected", "label": "spine\-1", "management\_ip": "10.0.0.1", "system\_id": "SERIAL123"}]`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-changed"></div>

      .. _ansible_collections.juniper.apstra.system_agents_module__return-changed:

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
        <div class="ansibleOptionAnchor" id="return-connection_state"></div>

      .. _ansible_collections.juniper.apstra.system_agents_module__return-connection_state:

      .. rst-class:: ansible-option-title

      **connection_state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-connection_state" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The connection state of the agent.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when agent exists

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"connected"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-installed_agents"></div>

      .. _ansible_collections.juniper.apstra.system_agents_module__return-installed_agents:

      .. rst-class:: ansible-option-title

      **installed_agents**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-installed_agents" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of agent IDs that had install\-agent triggered.

      Only returned when :literal:`state=installed`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state=installed


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-management_ip"></div>

      .. _ansible_collections.juniper.apstra.system_agents_module__return-management_ip:

      .. rst-class:: ansible-option-title

      **management_ip**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-management_ip" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The management IP of the agent.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when agent exists


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.juniper.apstra.system_agents_module__return-msg:

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
        <div class="ansibleOptionAnchor" id="return-system_id"></div>

      .. _ansible_collections.juniper.apstra.system_agents_module__return-system_id:

      .. rst-class:: ansible-option-title

      **system_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-system_id" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The system ID of the managed device (once acknowledged).


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when device is acknowledged


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

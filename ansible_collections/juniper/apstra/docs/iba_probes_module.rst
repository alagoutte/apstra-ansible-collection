.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. Anchors

.. _ansible_collections.juniper.apstra.iba_probes_module:

.. Anchors: short name for ansible.builtin

.. Title

juniper.apstra.iba_probes module -- Manage IBA (Intent\-Based Analytics) probes in Apstra
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `juniper.apstra collection <https://galaxy.ansible.com/ui/repo/published/juniper/apstra/>`_ (version 1.0.6).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install juniper.apstra`.

    To use it in a playbook, specify: :code:`juniper.apstra.iba_probes`.

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

- This module allows you to create, update, delete, and query IBA probes in Apstra blueprints.
- Supports instantiation of predefined (built\-in) probes as well as custom probe definitions.
- Also manages IBA dashboards for probe visualisation.
- Predefined probes are instantiated from a catalog of 48+ built\-in probe types including bgp\_session, traffic, device\_health, ecmp\_imbalance, lag\_imbalance, and many more.
- Custom probes can be created with user\-defined processors and stages.
- Probes monitor fabric health, traffic patterns, anomalies, and more.


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

      .. _ansible_collections.juniper.apstra.iba_probes_module__parameter-api_url:

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

      .. _ansible_collections.juniper.apstra.iba_probes_module__parameter-auth_token:

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

      .. _ansible_collections.juniper.apstra.iba_probes_module__parameter-body:

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

      For predefined probes, :literal:`predefined\_probe` is the probe name (e.g. :literal:`bgp\_session`\ ), and additional keys are the schema parameters (\ :literal:`label`\ , :literal:`duration`\ , etc.).

      For custom probes, keys include :literal:`label`\ , :literal:`description`\ , :literal:`disabled`\ , and :literal:`processors`.

      For dashboards, keys include :literal:`label` and :literal:`description`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id"></div>

      .. _ansible_collections.juniper.apstra.iba_probes_module__parameter-id:

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

      Dictionary containing resource identifiers.

      Always requires :literal:`blueprint` key with the blueprint UUID or label.

      For existing probes, include :literal:`probe` key with probe UUID or label.

      For dashboards, include :literal:`dashboard` key with dashboard UUID or label.

      Name/label resolution is supported for :literal:`blueprint`\ , :literal:`probe`\ , and :literal:`dashboard` keys.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.juniper.apstra.iba_probes_module__parameter-password:

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

      .. _ansible_collections.juniper.apstra.iba_probes_module__parameter-state:

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

      :literal:`present` creates or updates the resource.

      :literal:`absent` deletes the resource.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"absent"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-type"></div>

      .. _ansible_collections.juniper.apstra.iba_probes_module__parameter-type:

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

      The type of IBA resource to manage.

      :literal:`predefined` instantiates a probe from the Apstra predefined probe catalog.

      :literal:`probe` manages custom (raw) probes directly.

      :literal:`dashboard` manages IBA dashboards.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"predefined"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"probe"`
      - :ansible-option-choices-entry:`"dashboard"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.juniper.apstra.iba_probes_module__parameter-username:

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

      .. _ansible_collections.juniper.apstra.iba_probes_module__parameter-verify_certificates:

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

    # ── Predefined Probes ───────────────────────────────────────────────

    - name: Authenticate to Apstra
      juniper.apstra.authenticate:
        logout: false
      register: auth

    - name: Create a BGP Session probe from predefined
      juniper.apstra.iba_probes:
        type: predefined
        id:
          blueprint: "my-blueprint"
        body:
          predefined_probe: bgp_session
          label: "BGP Monitoring"
          duration: 300
          threshold: 40
        auth_token: "{{ auth.token }}"
      register: bgp_probe

    - name: Create a Device Traffic probe
      juniper.apstra.iba_probes:
        type: predefined
        id:
          blueprint: "my-blueprint"
        body:
          predefined_probe: traffic
          label: "Device Traffic"
        auth_token: "{{ auth.token }}"

    - name: Create a Device System Health probe
      juniper.apstra.iba_probes:
        type: predefined
        id:
          blueprint: "my-blueprint"
        body:
          predefined_probe: device_health
          label: "Device System Health"
          raise_switch_anomaly: true
          raise_server_anomaly: true
          history_duration: 2592000
        auth_token: "{{ auth.token }}"

    - name: Create an ECMP Imbalance probe (fabric)
      juniper.apstra.iba_probes:
        type: predefined
        id:
          blueprint: "my-blueprint"
        body:
          predefined_probe: fabric_ecmp_imbalance
          label: "ECMP Imbalance (Fabric Interfaces)"
        auth_token: "{{ auth.token }}"

    - name: Create a LAG Imbalance probe
      juniper.apstra.iba_probes:
        type: predefined
        id:
          blueprint: "my-blueprint"
        body:
          predefined_probe: lag_imbalance
          label: "LAG Imbalance"
        auth_token: "{{ auth.token }}"

    - name: Create a Control Plane Policing probe
      juniper.apstra.iba_probes:
        type: predefined
        id:
          blueprint: "my-blueprint"
        body:
          predefined_probe: copp
          label: "Control Plane Policing"
          aggregation_period: 300
          collection_interval: 120
          history_duration: 2592000
          drop_count_threshold: 1
        auth_token: "{{ auth.token }}"

    - name: Create a Device Telemetry Health probe
      juniper.apstra.iba_probes:
        type: predefined
        id:
          blueprint: "my-blueprint"
        body:
          predefined_probe: device_telemetry_health
          label: "Device Telemetry Health"
        auth_token: "{{ auth.token }}"

    - name: Create an ESI Imbalance probe
      juniper.apstra.iba_probes:
        type: predefined
        id:
          blueprint: "my-blueprint"
        body:
          predefined_probe: esi_imbalance
          label: "ESI Imbalance"
        auth_token: "{{ auth.token }}"

    - name: Create a MAC Monitor probe
      juniper.apstra.iba_probes:
        type: predefined
        id:
          blueprint: "my-blueprint"
        body:
          predefined_probe: mac_monitor
          label: "MAC Monitor"
        auth_token: "{{ auth.token }}"

    - name: Create a Bandwidth Utilization probe
      juniper.apstra.iba_probes:
        type: predefined
        id:
          blueprint: "my-blueprint"
        body:
          predefined_probe: bandwidth_utilization
          label: "Bandwidth Utilization"
          first_summary_average_period: 120
          first_summary_total_duration: 3600
          second_summary_average_period: 3600
          second_summary_total_duration: 2592000
        auth_token: "{{ auth.token }}"

    - name: Create a Spine Fault Tolerance probe
      juniper.apstra.iba_probes:
        type: predefined
        id:
          blueprint: "my-blueprint"
        body:
          predefined_probe: spine_fault_tolerance
          label: "Spine Fault Tolerance"
        auth_token: "{{ auth.token }}"

    - name: Create an Optical Transceivers probe
      juniper.apstra.iba_probes:
        type: predefined
        id:
          blueprint: "my-blueprint"
        body:
          predefined_probe: optical_transceivers
          label: "Optical Transceivers"
        auth_token: "{{ auth.token }}"

    - name: Create an Interface Flapping probe (fabric)
      juniper.apstra.iba_probes:
        type: predefined
        id:
          blueprint: "my-blueprint"
        body:
          predefined_probe: fabric_interface_flapping
          label: "Interface Flapping (Fabric)"
        auth_token: "{{ auth.token }}"

    - name: Create an EVPN Host Flapping probe
      juniper.apstra.iba_probes:
        type: predefined
        id:
          blueprint: "my-blueprint"
        body:
          predefined_probe: evpn_host_flapping
          label: "EVPN Host Flapping"
        auth_token: "{{ auth.token }}"

    - name: Create a Packet Discard Percentage probe
      juniper.apstra.iba_probes:
        type: predefined
        id:
          blueprint: "my-blueprint"
        body:
          predefined_probe: packet_discard_percentage
          label: "Packet Discard Percentage"
        auth_token: "{{ auth.token }}"

    - name: Create an East-West Traffic probe
      juniper.apstra.iba_probes:
        type: predefined
        id:
          blueprint: "my-blueprint"
        body:
          predefined_probe: eastwest_traffic
          label: "East-West Traffic"
        auth_token: "{{ auth.token }}"

    - name: Create an External Routes probe
      juniper.apstra.iba_probes:
        type: predefined
        id:
          blueprint: "my-blueprint"
        body:
          predefined_probe: external_routes
          label: "External Routes"
        auth_token: "{{ auth.token }}"

    # ── Update / Delete Probes ──────────────────────────────────────────

    - name: Update a probe's label (by current label lookup)
      juniper.apstra.iba_probes:
        type: probe
        id:
          blueprint: "my-blueprint"
        body:
          label: "BGP Monitoring"
          description: "Updated BGP probe description"
        state: present
        auth_token: "{{ auth.token }}"

    - name: Delete a probe by ID
      juniper.apstra.iba_probes:
        type: probe
        id:
          blueprint: "my-blueprint"
          probe: "{{ bgp_probe.id.probe }}"
        state: absent
        auth_token: "{{ auth.token }}"

    - name: Delete a probe by label (via id.probe)
      juniper.apstra.iba_probes:
        type: probe
        id:
          blueprint: "my-blueprint"
          probe: "BGP Monitoring"
        state: absent
        auth_token: "{{ auth.token }}"

    - name: Read a probe by label (via id.probe)
      juniper.apstra.iba_probes:
        type: probe
        id:
          blueprint: "my-blueprint"
          probe: "BGP Monitoring"
        state: present
        auth_token: "{{ auth.token }}"

    - name: Delete a probe by label (via body.label fallback)
      juniper.apstra.iba_probes:
        type: probe
        id:
          blueprint: "my-blueprint"
        body:
          label: "BGP Monitoring"
        state: absent
        auth_token: "{{ auth.token }}"

    # ── IBA Dashboards ──────────────────────────────────────────────────

    - name: Create an IBA dashboard
      juniper.apstra.iba_probes:
        type: dashboard
        id:
          blueprint: "my-blueprint"
        body:
          label: "Fabric Health Dashboard"
          description: "Overview of fabric health probes"
        state: present
        auth_token: "{{ auth.token }}"
      register: dash

    - name: Delete an IBA dashboard by ID
      juniper.apstra.iba_probes:
        type: dashboard
        id:
          blueprint: "my-blueprint"
          dashboard: "{{ dash.id.dashboard }}"
        state: absent
        auth_token: "{{ auth.token }}"

    - name: Delete an IBA dashboard by label
      juniper.apstra.iba_probes:
        type: dashboard
        id:
          blueprint: "my-blueprint"
          dashboard: "Fabric Health Dashboard"
        state: absent
        auth_token: "{{ auth.token }}"

    - name: Read an IBA dashboard by label
      juniper.apstra.iba_probes:
        type: dashboard
        id:
          blueprint: "my-blueprint"
          dashboard: "Fabric Health Dashboard"
        state: present
        auth_token: "{{ auth.token }}"



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

      .. _ansible_collections.juniper.apstra.iba_probes_module__return-changed:

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

      .. _ansible_collections.juniper.apstra.iba_probes_module__return-changes:

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
        <div class="ansibleOptionAnchor" id="return-dashboard"></div>

      .. _ansible_collections.juniper.apstra.iba_probes_module__return-dashboard:

      .. rst-class:: ansible-option-title

      **dashboard**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-dashboard" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The full dashboard object details.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when type is dashboard with state present


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-id"></div>

      .. _ansible_collections.juniper.apstra.iba_probes_module__return-id:

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

      Dictionary of resource identifiers.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on create or when found by label

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"blueprint": "54bd9839\-275e\-4444\-8ef2\-5093f49e08b7", "probe": "99a47423\-c172\-4006\-b55a\-da37102f73e4"}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.juniper.apstra.iba_probes_module__return-msg:

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
        <div class="ansibleOptionAnchor" id="return-predefined_probes"></div>

      .. _ansible_collections.juniper.apstra.iba_probes_module__return-predefined_probes:

      .. rst-class:: ansible-option-title

      **predefined_probes**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-predefined_probes" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of available predefined probe names (when listing).


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state is present and type is predefined with no body


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-probe"></div>

      .. _ansible_collections.juniper.apstra.iba_probes_module__return-probe:

      .. rst-class:: ansible-option-title

      **probe**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-probe" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The full probe object details.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when type is predefined or probe with state present


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

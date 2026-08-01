.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. Anchors

.. _ansible_collections.juniper.apstra.ztp_config_module:

.. Anchors: short name for ansible.builtin

.. Title

juniper.apstra.ztp_config module -- Manage ZTP VM configuration (DHCP, firmware, passwords)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `juniper.apstra collection <https://galaxy.ansible.com/ui/repo/published/juniper/apstra/>`_ (version 1.1.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install juniper.apstra`.

    To use it in a playbook, specify: :code:`juniper.apstra.ztp_config`.

.. version_added

.. rst-class:: ansible-version-added

New in juniper.apstra 1.1.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module manages the Apstra ZTP VM configuration including DHCP host\-reservations, subnets, pools, firmware mappings, and passwords.
- The ZTP VM is a separate appliance from the Apstra server and requires its own connection parameters (\ :literal:`ztp\_url`\ , :literal:`ztp\_username`\ , :literal:`ztp\_password`\ ).
- Two configuration scopes are supported via the :literal:`scope` parameter.
- :literal:`dhcp\_configurator` manages DHCP subnets, pools, host\-reservations, and global DHCP options via the :literal:`/api/ztp/config/dhcp/configurator` endpoint.
- :literal:`ztp\_config` manages firmware mappings, default passwords, and ZTP workflow settings via the :literal:`/api/ztp/config/ztpjson` endpoint.
- :literal:`password` changes the ZTP web UI admin password via :literal:`/api/ztp/aaa/change\-password`.
- The module is idempotent — it reads the current configuration, compares it with the desired state, and only applies changes when differences exist.


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
        <div class="ansibleOptionAnchor" id="parameter-firmware"></div>

      .. _ansible_collections.juniper.apstra.ztp_config_module__parameter-firmware:

      .. rst-class:: ansible-option-title

      **firmware**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-firmware" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Firmware/ZTP configuration data (the full ZTP JSON config dict).

      This is the content of the ZTP JSON configuration, keyed by platform (e.g., :literal:`defaults`\ , :literal:`junos`\ , :literal:`nxos`\ , :literal:`eos`\ ).

      Used with :literal:`scope=ztp\_config`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-global_host_reservations"></div>

      .. _ansible_collections.juniper.apstra.ztp_config_module__parameter-global_host_reservations:

      .. rst-class:: ansible-option-title

      **global_host_reservations**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-global_host_reservations" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of global (outside\-subnet) host reservations.

      Same format as :literal:`host\_reservations`.

      Used with :literal:`scope=dhcp\_configurator`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-host_reservations"></div>

      .. _ansible_collections.juniper.apstra.ztp_config_module__parameter-host_reservations:

      .. rst-class:: ansible-option-title

      **host_reservations**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-host_reservations" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of MAC\-to\-IP host reservations for DHCP.

      Each entry must include :literal:`hw\-address` (MAC address) and :literal:`ip\-address` (IP to assign).

      Optional :literal:`hostname` for the reservation.

      Optional :literal:`subnet` to target a specific existing subnet instead of using the first configured subnet.

      Optional :literal:`pool\-range\-start` and :literal:`pool\-range\-end` to target a specific pool within the selected subnet. These selector keys are used only by the module and are not sent to the ZTP API.

      Used with :literal:`scope=dhcp\_configurator`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-new_password"></div>

      .. _ansible_collections.juniper.apstra.ztp_config_module__parameter-new_password:

      .. rst-class:: ansible-option-title

      **new_password**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-new_password" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      New ZTP web UI password (required for :literal:`scope=password`\ ).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-old_password"></div>

      .. _ansible_collections.juniper.apstra.ztp_config_module__parameter-old_password:

      .. rst-class:: ansible-option-title

      **old_password**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-old_password" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Current ZTP web UI password (required for :literal:`scope=password`\ ).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-options"></div>

      .. _ansible_collections.juniper.apstra.ztp_config_module__parameter-options:

      .. rst-class:: ansible-option-title

      **options**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-options" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      DHCP options to set globally.

      Supported keys include :literal:`domain\-name`\ , :literal:`domain\-search`\ , :literal:`domain\-name\-servers` (list of IPs), :literal:`tftp\-server\-name`.

      Used with :literal:`scope=dhcp\_configurator`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-reservation_mode_default"></div>

      .. _ansible_collections.juniper.apstra.ztp_config_module__parameter-reservation_mode_default:

      .. rst-class:: ansible-option-title

      **reservation_mode_default**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-reservation_mode_default" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Default reservation mode for DHCP.

      Valid values are :literal:`all`\ , :literal:`global`\ , :literal:`out\-of\-pool`\ , :literal:`disabled`.

      Used with :literal:`scope=dhcp\_configurator`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-scope"></div>

      .. _ansible_collections.juniper.apstra.ztp_config_module__parameter-scope:

      .. rst-class:: ansible-option-title

      **scope**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-scope" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The configuration scope to manage.

      :literal:`dhcp\_configurator` — manage DHCP subnets, pools, host\-reservations, and DHCP options.

      :literal:`ztp\_config` — manage firmware mappings, default passwords, and ZTP workflow settings.

      :literal:`password` — change the ZTP web UI admin password.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"dhcp\_configurator"`
      - :ansible-option-choices-entry:`"ztp\_config"`
      - :ansible-option-choices-entry:`"password"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.juniper.apstra.ztp_config_module__parameter-state:

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

      Desired state of the configuration.

      :literal:`present` — create or update the configuration to match the desired state.

      :literal:`absent` — remove specific items (host\-reservations, subnets). Only applicable for :literal:`dhcp\_configurator` scope.

      :literal:`query` — retrieve the current configuration without making changes.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"absent"`
      - :ansible-option-choices-entry:`"query"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-subnets"></div>

      .. _ansible_collections.juniper.apstra.ztp_config_module__parameter-subnets:

      .. rst-class:: ansible-option-title

      **subnets**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-subnets" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of subnet definitions for DHCP configuration.

      Each subnet must include :literal:`subnet` (CIDR notation), :literal:`router` (gateway IP), and :literal:`pools` (list of IP ranges).

      Used with :literal:`scope=dhcp\_configurator`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ztp_auth_token"></div>

      .. _ansible_collections.juniper.apstra.ztp_config_module__parameter-ztp_auth_token:

      .. rst-class:: ansible-option-title

      **ztp_auth_token**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ztp_auth_token" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Pre\-existing auth token for the ZTP VM.

      Can also be set via the :literal:`ZTP\_AUTH\_TOKEN` environment variable.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ztp_password"></div>

      .. _ansible_collections.juniper.apstra.ztp_config_module__parameter-ztp_password:

      .. rst-class:: ansible-option-title

      **ztp_password**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ztp_password" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Password for ZTP VM authentication.

      Can also be set via the :literal:`ZTP\_PASSWORD` environment variable.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ztp_url"></div>

      .. _ansible_collections.juniper.apstra.ztp_config_module__parameter-ztp_url:

      .. rst-class:: ansible-option-title

      **ztp_url**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ztp_url" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Base URL of the ZTP VM (e.g., :literal:`https://10.204.22.128`\ ).

      Required because the ZTP VM is typically a separate appliance from the Apstra server.

      Can also be set via the :literal:`ZTP\_URL` environment variable.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ztp_username"></div>

      .. _ansible_collections.juniper.apstra.ztp_config_module__parameter-ztp_username:

      .. rst-class:: ansible-option-title

      **ztp_username**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ztp_username" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Username for ZTP VM authentication.

      Can also be set via the :literal:`ZTP\_USERNAME` environment variable.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ztp_verify_certificates"></div>

      .. _ansible_collections.juniper.apstra.ztp_config_module__parameter-ztp_verify_certificates:

      .. rst-class:: ansible-option-title

      **ztp_verify_certificates**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ztp_verify_certificates" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Whether to verify SSL certificates when connecting to the ZTP VM.


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

    # =============================================================================
    # DHCP CONFIGURATOR SCOPE — Query, Update, Reservations
    # =============================================================================

    # Query current DHCP configurator state
    - name: Get current DHCP configuration
      juniper.apstra.ztp_config:
        scope: dhcp_configurator
        state: query
      register: dhcp_config

    - name: Show DHCP config
      ansible.builtin.debug:
        var: dhcp_config.config

    # Configure DHCP subnets, pools, options, and host-reservations
    # This example shows all available DHCP options
    - name: Configure DHCP with all options
      juniper.apstra.ztp_config:
        scope: dhcp_configurator
        state: present
        options:
          domain-name: "ztplab.local"
          domain-search: "ztplab.local"
          domain-name-servers:
            - "8.8.8.8"
            - "8.8.4.4"
          tftp-server-name: "192.168.50.2"
        subnets:
          - subnet: "192.168.50.0/24"
            router: "192.168.50.1"
            pools:
              - range-start: "192.168.50.10"
                range-end: "192.168.50.50"
            host-reservations:
              - hw-address: "aa:bb:cc:dd:ee:01"
                ip-address: "192.168.50.100"
                hostname: "switch1"
              - hw-address: "aa:bb:cc:dd:ee:02"
                ip-address: "192.168.50.101"
                hostname: "switch2"
            reservation-mode:
              - "all"

    # Configure multiple DHCP subnets with separate pools
    - name: Configure multiple subnets
      juniper.apstra.ztp_config:
        scope: dhcp_configurator
        state: present
        subnets:
          - subnet: "192.168.50.0/24"
            router: "192.168.50.1"
            pools:
              - range-start: "192.168.50.10"
                range-end: "192.168.50.50"
          - subnet: "10.0.0.0/24"
            router: "10.0.0.1"
            pools:
              - range-start: "10.0.0.10"
                range-end: "10.0.0.100"

    # Add a host-reservation to a specific pool in an existing subnet
    - name: Add host reservation to a selected pool
      juniper.apstra.ztp_config:
        scope: dhcp_configurator
        state: present
        host_reservations:
          - subnet: "192.168.50.0/24"
            pool-range-start: "192.168.50.60"
            pool-range-end: "192.168.50.80"
            hw-address: "aa:bb:cc:dd:ee:03"
            ip-address: "192.168.50.65"
            hostname: "switch3"

    # Add a host-reservation to a specific subnet without replacing others
    - name: Add host reservation to a selected subnet
      juniper.apstra.ztp_config:
        scope: dhcp_configurator
        state: present
        host_reservations:
          - subnet: "10.0.0.0/24"
          - hw-address: "aa:bb:cc:dd:ee:03"
            ip-address: "10.0.0.25"
            hostname: "switch3-alt"

    # Add global host reservations (outside any subnet)
    - name: Add global host reservation
      juniper.apstra.ztp_config:
        scope: dhcp_configurator
        state: present
        global_host_reservations:
          - hw-address: "aa:bb:cc:dd:ee:ff"
            ip-address: "10.10.10.100"
            hostname: "global-device"

    # Set default reservation mode
    - name: Set reservation mode
      juniper.apstra.ztp_config:
        scope: dhcp_configurator
        state: present
        reservation_mode_default:
          - "all"

    # Remove a host-reservation by MAC address
    - name: Remove host reservation
      juniper.apstra.ztp_config:
        scope: dhcp_configurator
        state: absent
        host_reservations:
          - hw-address: "aa:bb:cc:dd:ee:03"
            ip-address: "192.168.50.102"

    # Remove an entire subnet
    - name: Remove a subnet
      juniper.apstra.ztp_config:
        scope: dhcp_configurator
        state: absent
        subnets:
          - subnet: "10.0.0.0/24"

    # =============================================================================
    # ZTP CONFIG SCOPE — Query, Update firmware/password/agent settings
    # =============================================================================

    # Query current ZTP JSON config
    - name: Get ZTP firmware config
      juniper.apstra.ztp_config:
        scope: ztp_config
        state: query
      register: ztp_fw

    - name: Show ZTP config
      ansible.builtin.debug:
        var: ztp_fw.config

    # Configure complete ZTP JSON with all platform blocks
    # This manages the full ztp.json used by the ZTP VM for device provisioning
    - name: Configure complete ZTP JSON
      juniper.apstra.ztp_config:
        scope: ztp_config
        state: present
        firmware:
          defaults:
            device-root-password: "admin"
            device-user: "aosadmin"
            device-user-password: "aosadmin"
            dual-routing-engine: false
            junos-versions:
              - "25.4R1.12"
            junos-evo-image: "http://server/path/to/junos-evo-install.tgz"
            junos-evo-versions:
              - "junos-evo-version1"
            eos-image: "aos_eos_image.bin"
            eos-versions:
              - "eos-version1"
              - "eos-version2"
            nxos-image: "aos_nxos_image.bin"
            nxos-versions:
              - "nxos-version1"
            sonic-image: "http://server/path/to/sonic.bin"
            sonic-versions:
              - "sonic-version1"
              - "sonic-version2"
            management-subnet-prefixlen: 0
            system-agent-params:
              agent_type: "onbox"
          junos:
            device-root-password: "Juniper123"
            device-user-password: "Juniper123"
            system-agent-params:
              agent_type: "offbox"
              job_on_create: "install"
              platform: "junos"
          junos-evo:
            device-root-password: "root123"
            device-user-password: "aosadmin123"
            system-agent-params:
              agent_type: "offbox"
              job_on_create: "install"
              platform: "junos"
          eos:
            custom-config: "eos_custom.sh"
          nxos:
            device-root-password: "admin123"
            system-agent-params:
              agent_type: "onbox"

    # Update only Junos settings (other platforms are preserved)
    # The module does a deep merge — only specified keys are updated
    - name: Update Junos ZTP settings only
      juniper.apstra.ztp_config:
        scope: ztp_config
        state: present
        firmware:
          junos:
            device-root-password: "{{ junos_root_password }}"
            device-user-password: "{{ junos_user_password }}"
            system-agent-params:
              agent_type: "offbox"
              job_on_create: "install"
              platform: "junos"

    # Update default settings only
    - name: Update default ZTP settings
      juniper.apstra.ztp_config:
        scope: ztp_config
        state: present
        firmware:
          defaults:
            device-root-password: "{{ default_root_password }}"
            device-user: "{{ device_user }}"
            device-user-password: "{{ device_user_password }}"
            junos-versions:
              - "25.4R1.12"

    # =============================================================================
    # PASSWORD SCOPE — Change ZTP web UI admin password
    # =============================================================================

    # Change ZTP web UI password
    - name: Change ZTP admin password
      juniper.apstra.ztp_config:
        scope: password
        old_password: "{{ current_ztp_password }}"
        new_password: "{{ new_ztp_password }}"



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

      .. _ansible_collections.juniper.apstra.ztp_config_module__return-changed:

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

      Whether any changes were made.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-changes"></div>

      .. _ansible_collections.juniper.apstra.ztp_config_module__return-changes:

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

      Summary of changes applied.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when changes were made


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-config"></div>

      .. _ansible_collections.juniper.apstra.ztp_config_module__return-config:

      .. rst-class:: ansible-option-title

      **config**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-config" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The current or resulting configuration.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when scope is dhcp\_configurator or ztp\_config


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.juniper.apstra.ztp_config_module__return-msg:

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

      Human\-readable message describing the outcome.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Prabhanjan KV (@kvp-hpe)


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

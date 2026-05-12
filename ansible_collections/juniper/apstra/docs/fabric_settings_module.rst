.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. Anchors

.. _ansible_collections.juniper.apstra.fabric_settings_module:

.. Anchors: short name for ansible.builtin

.. Title

juniper.apstra.fabric_settings module -- Manage fabric settings in an Apstra blueprint
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `juniper.apstra collection <https://galaxy.ansible.com/ui/repo/published/juniper/apstra/>`_ (version 1.0.6).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install juniper.apstra`.

    To use it in a playbook, specify: :code:`juniper.apstra.fabric_settings`.

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

- This module manages fabric\-wide settings within an Apstra blueprint.
- Settings include MTU values, EVPN parameters, overlay protocol, anti\-affinity policies, default SVI/anycast configuration, and more.
- Uses the Apstra fabric\-settings API via the AOS SDK.
- Provides full idempotency. Current settings are fetched and compared before updating.
- Only the settings specified in :literal:`settings` are modified; other fabric settings remain unchanged.


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

      .. _ansible_collections.juniper.apstra.fabric_settings_module__parameter-api_url:

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

      .. _ansible_collections.juniper.apstra.fabric_settings_module__parameter-auth_token:

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

      .. _ansible_collections.juniper.apstra.fabric_settings_module__parameter-body:

      .. rst-class:: ansible-option-title

      **body**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A dictionary of fabric settings to apply.

      Only the keys provided will be updated; unspecified keys remain unchanged.

      Common keys include :literal:`external\_router\_mtu`\ , :literal:`fabric\_l3\_mtu`\ , :literal:`spine\_leaf\_links\_mtu`\ , :literal:`esi\_mac\_msb`\ , :literal:`anti\_affinity`\ , :literal:`junos\_evpn\_max\_nexthop\_count`\ , :literal:`junos\_evpn\_routing\_instance\_mode\_allowed`\ , :literal:`max\_evpn\_routes`\ , :literal:`overlay\_control\_protocol`\ , :literal:`default\_svi\_l3\_mtu`\ , :literal:`default\_anycast\_gw\_mac`\ , etc.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id"></div>

      .. _ansible_collections.juniper.apstra.fabric_settings_module__parameter-id:

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

      Must contain :literal:`blueprint` key with the blueprint ID.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id/blueprint"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.fabric_settings_module__parameter-id/blueprint:

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

      The ID of the blueprint in which to manage fabric settings.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.juniper.apstra.fabric_settings_module__parameter-password:

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
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.juniper.apstra.fabric_settings_module__parameter-username:

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

      .. _ansible_collections.juniper.apstra.fabric_settings_module__parameter-verify_certificates:

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

    # ── Set fabric MTU ────────────────────────────────────────────────

    - name: Configure fabric L3 MTU
      juniper.apstra.fabric_settings:
        id:
          blueprint: "{{ blueprint_id }}"
        body:
          fabric_l3_mtu: 9170
          spine_leaf_links_mtu: 9170
          external_router_mtu: 9100

    # ── Configure EVPN settings ──────────────────────────────────────

    - name: Set EVPN overlay parameters
      juniper.apstra.fabric_settings:
        id:
          blueprint: "{{ blueprint_id }}"
        body:
          overlay_control_protocol: "evpn"
          max_evpn_routes: 10000
          junos_evpn_max_nexthop_count: 2

    # ── Set anycast gateway MAC ───────────────────────────────────────

    - name: Configure default anycast GW MAC
      juniper.apstra.fabric_settings:
        id:
          blueprint: "{{ blueprint_id }}"
        body:
          default_anycast_gw_mac: "00:00:5e:00:01:01"

    # ── Set anti-affinity policy ─────────────────────────────────────

    - name: Configure anti-affinity settings
      juniper.apstra.fabric_settings:
        id:
          blueprint: "{{ blueprint_id }}"
        body:
          anti_affinity:
            algorithm: "heuristic_enabled"
            max_links_count_per_slot: 1
            max_links_per_slot: 1
            max_svi_inter_count: 0

    # ── ESI MAC configuration ────────────────────────────────────────

    - name: Set ESI MAC MSB
      juniper.apstra.fabric_settings:
        id:
          blueprint: "{{ blueprint_id }}"
        body:
          esi_mac_msb: 2

    # ── Full fabric settings for a new blueprint ─────────────────────

    - name: Apply full fabric settings
      juniper.apstra.fabric_settings:
        id:
          blueprint: "{{ blueprint_id }}"
        body:
          fabric_l3_mtu: 9170
          spine_leaf_links_mtu: 9170
          external_router_mtu: 9100
          overlay_control_protocol: "evpn"
          default_anycast_gw_mac: "00:00:5e:00:01:01"
          esi_mac_msb: 2



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

      .. _ansible_collections.juniper.apstra.fabric_settings_module__return-changed:

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
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.juniper.apstra.fabric_settings_module__return-msg:

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
        <div class="ansibleOptionAnchor" id="return-settings"></div>

      .. _ansible_collections.juniper.apstra.fabric_settings_module__return-settings:

      .. rst-class:: ansible-option-title

      **settings**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-settings" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The complete fabric settings after the operation.


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

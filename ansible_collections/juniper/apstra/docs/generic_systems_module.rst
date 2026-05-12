.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. Anchors

.. _ansible_collections.juniper.apstra.generic_systems_module:

.. Anchors: short name for ansible.builtin

.. Title

juniper.apstra.generic_systems module -- Manage datacenter generic systems in Apstra blueprints
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `juniper.apstra collection <https://galaxy.ansible.com/ui/repo/published/juniper/apstra/>`_ (version 1.0.6).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install juniper.apstra`.

    To use it in a playbook, specify: :code:`juniper.apstra.generic_systems`.

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

- This module manages generic systems in Apstra datacenter blueprints using an :literal:`id` / :literal:`body` / :literal:`state` parameter model.
- The :literal:`id` dict contains the blueprint ID and optional system\_id for identifying which generic system to manage.
- The :literal:`body` dict contains all desired properties including name, hostname, tags, links, deploy\_mode, ASN, loopback IPs, port\-channel ID range, external flag, and clear\_cts\_on\_destroy.
- Supports creating, updating, and deleting generic systems with their links to switches.
- Links are defined as a list in :literal:`body.links`\ , each specifying the target switch, interface name, interface transform, optional LAG mode, group label, and per\-link tags.
- Uses the :literal:`switch\-system\-links` API to create in\-rack generic systems and the :literal:`external\-generic\-systems` API for external systems.
- Provides full idempotency — create, update, and delete operations are safe to re\-run.
- Requires a blueprint to already exist and leaf switches to have interface maps assigned before creating generic systems.


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

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-api_url:

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

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-auth_token:

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

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-body:

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

      Dictionary of desired properties for the generic system.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/asn"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-body/asn:

      .. rst-class:: ansible-option-title

      **asn**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/asn" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The ASN to assign to the generic system.

      Set to :literal:`null` to clear the ASN.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/clear_cts_on_destroy"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-body/clear_cts_on_destroy:

      .. rst-class:: ansible-option-title

      **clear_cts_on_destroy**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/clear_cts_on_destroy" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      If true, clear all connectivity templates from the system's links before deleting the generic system.

      Useful when CTs are applied and deletion would otherwise fail.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/deploy_mode"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-body/deploy_mode:

      .. rst-class:: ansible-option-title

      **deploy_mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/deploy_mode" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The deploy mode for the generic system.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"deploy"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"ready"`
      - :ansible-option-choices-entry:`"drain"`
      - :ansible-option-choices-entry:`"undeploy"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/external"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-body/external:

      .. rst-class:: ansible-option-title

      **external**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/external" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Whether this is an external generic system (outside of racks).

      External systems use a different API for creation and deletion.

      When set on an existing system, the external flag will be updated via allow\_unsafe PATCH.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/hostname"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-body/hostname:

      .. rst-class:: ansible-option-title

      **hostname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/hostname" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The hostname of the generic system.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/links"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-body/links:

      .. rst-class:: ansible-option-title

      **links**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/links" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of link definitions connecting switches to the generic system.

      Each link is a dictionary with the keys described below.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/links/group_label"></div>

      .. raw:: latex

        \hspace{0.04\textwidth}\begin{minipage}[t]{0.28\textwidth}

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-body/links/group_label:

      .. rst-class:: ansible-option-title

      **group_label**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/links/group_label" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Label used to group multiple links into a single LAG.

      All links sharing the same :literal:`group\_label` and :literal:`lag\_mode` form one LAG.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/links/lag_mode"></div>

      .. raw:: latex

        \hspace{0.04\textwidth}\begin{minipage}[t]{0.28\textwidth}

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-body/links/lag_mode:

      .. rst-class:: ansible-option-title

      **lag_mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/links/lag_mode" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      LAG mode for this link.

      Use :literal:`null` or omit for a standalone (non\-LAG) link.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"lacp\_active"`
      - :ansible-option-choices-entry:`"lacp\_passive"`
      - :ansible-option-choices-entry:`"static\_lag"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/links/tags"></div>

      .. raw:: latex

        \hspace{0.04\textwidth}\begin{minipage}[t]{0.28\textwidth}

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-body/links/tags:

      .. rst-class:: ansible-option-title

      **tags**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/links/tags" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of tags to apply to this individual link.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/links/target_switch_id"></div>

      .. raw:: latex

        \hspace{0.04\textwidth}\begin{minipage}[t]{0.28\textwidth}

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-body/links/target_switch_id:

      .. rst-class:: ansible-option-title

      **target_switch_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/links/target_switch_id" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The graph node ID of the target leaf/access switch.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/links/target_switch_if_name"></div>

      .. raw:: latex

        \hspace{0.04\textwidth}\begin{minipage}[t]{0.28\textwidth}

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-body/links/target_switch_if_name:

      .. rst-class:: ansible-option-title

      **target_switch_if_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/links/target_switch_if_name" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The physical interface name on the target switch (e.g. :literal:`xe\-0/0/6`\ ).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/links/target_switch_if_transform_id"></div>

      .. raw:: latex

        \hspace{0.04\textwidth}\begin{minipage}[t]{0.28\textwidth}

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-body/links/target_switch_if_transform_id:

      .. rst-class:: ansible-option-title

      **target_switch_if_transform_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/links/target_switch_if_transform_id" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer` / :ansible-option-required:`required`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The interface transform ID controlling speed/breakout mode.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/loopback_ipv4"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-body/loopback_ipv4:

      .. rst-class:: ansible-option-title

      **loopback_ipv4**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/loopback_ipv4" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The IPv4 loopback address (CIDR notation) for the generic system.

      Set to :literal:`null` to clear the loopback.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/loopback_ipv6"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-body/loopback_ipv6:

      .. rst-class:: ansible-option-title

      **loopback_ipv6**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/loopback_ipv6" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The IPv6 loopback address (CIDR notation) for the generic system.

      Set to :literal:`null` to clear the loopback.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/name"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-body/name:

      .. rst-class:: ansible-option-title

      **name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/name" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The display name (label) of the generic system.

      Corresponds to :literal:`Name` / :literal:`label` in the Apstra graph.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/port_channel_id_max"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-body/port_channel_id_max:

      .. rst-class:: ansible-option-title

      **port_channel_id_max**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/port_channel_id_max" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Maximum port\-channel ID for the generic system.

      Set to 0 to disable.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`0`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/port_channel_id_min"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-body/port_channel_id_min:

      .. rst-class:: ansible-option-title

      **port_channel_id_min**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/port_channel_id_min" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Minimum port\-channel ID for the generic system.

      Set to 0 to disable.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`0`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-body/tags"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-body/tags:

      .. rst-class:: ansible-option-title

      **tags**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-body/tags" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of tags to apply to the generic system node.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id"></div>

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-id:

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

      Dictionary identifying the generic system within a blueprint.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id/blueprint"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-id/blueprint:

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

      The ID of the datacenter blueprint.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id/system_id"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-id/system_id:

      .. rst-class:: ansible-option-title

      **system_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-id/system_id" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The node ID of an existing generic system within the blueprint.

      Required for update and delete operations.

      Returned after create operations.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-password:

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

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-state:

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

      Desired state of the generic system.

      :literal:`present` will create or update the generic system.

      :literal:`absent` will delete the generic system.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"absent"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-username:

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

      .. _ansible_collections.juniper.apstra.generic_systems_module__parameter-verify_certificates:

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

    # ── Create a generic system with a single link ─────────────────────

    - name: Create a generic system connected to a leaf switch
      juniper.apstra.generic_systems:
        id:
          blueprint: "{{ blueprint_id }}"
        body:
          name: "my-server-01"
          hostname: "my-server-01.example.com"
          tags:
            - "server"
            - "prod"
          deploy_mode: "deploy"
          links:
            - target_switch_id: "{{ leaf_id }}"
              target_switch_if_name: "xe-0/0/7"
              target_switch_if_transform_id: 1
              tags:
                - "10G"
        state: present
      register: gs_create

    # ── Create using switch label instead of node ID ──────────────────

    - name: Create a generic system using switch name
      juniper.apstra.generic_systems:
        id:
          blueprint: "my-blueprint"
        body:
          name: "my-server-02"
          hostname: "my-server-02.example.com"
          links:
            - target_switch_id: "leaf-1"
              target_switch_if_name: "xe-0/0/8"
              target_switch_if_transform_id: 1
        state: present

    # ── Create a generic system with dual LAG links ───────────────────

    - name: Create a 4x10G server with two LAG bonds
      juniper.apstra.generic_systems:
        id:
          blueprint: "{{ blueprint_id }}"
        body:
          name: "lag-server-01"
          hostname: "lag-server-01.example.com"
          tags:
            - "server"
            - "production"
          links:
            - target_switch_id: "{{ leaf_ids[0] }}"
              target_switch_if_name: "xe-0/0/6"
              target_switch_if_transform_id: 1
              lag_mode: "lacp_active"
              group_label: "bond0"
              tags: ["10G", "bond0"]
            - target_switch_id: "{{ leaf_ids[1] }}"
              target_switch_if_name: "xe-0/0/6"
              target_switch_if_transform_id: 1
              lag_mode: "lacp_active"
              group_label: "bond0"
              tags: ["10G", "bond0"]
            - target_switch_id: "{{ leaf_ids[0] }}"
              target_switch_if_name: "xe-0/0/7"
              target_switch_if_transform_id: 1
              lag_mode: "lacp_active"
              group_label: "bond1"
              tags: ["10G", "bond1"]
            - target_switch_id: "{{ leaf_ids[1] }}"
              target_switch_if_name: "xe-0/0/7"
              target_switch_if_transform_id: 1
              lag_mode: "lacp_active"
              group_label: "bond1"
              tags: ["10G", "bond1"]
        state: present
      register: lag_server

    # ── Update a generic system ────────────────────────────────────────

    - name: Update generic system hostname and deploy mode
      juniper.apstra.generic_systems:
        id:
          blueprint: "{{ blueprint_id }}"
          system_id: "{{ gs_create.system_id }}"
        body:
          name: "my-server-01-updated"
          hostname: "my-server-01-updated.example.com"
          deploy_mode: "ready"
        state: present
      register: gs_update

    # ── Set ASN and loopback addresses ─────────────────────────────────

    - name: Configure system with ASN and loopbacks
      juniper.apstra.generic_systems:
        id:
          blueprint: "{{ blueprint_id }}"
          system_id: "{{ gs_create.system_id }}"
        body:
          asn: 65001
          loopback_ipv4: "10.0.0.1/32"
          loopback_ipv6: "fd00::1/128"
          port_channel_id_min: 1
          port_channel_id_max: 128
        state: present
      register: gs_props

    # ── Create an external generic system ──────────────────────────────

    - name: Create external generic system
      juniper.apstra.generic_systems:
        id:
          blueprint: "{{ blueprint_id }}"
        body:
          name: "external-server-01"
          hostname: "external-server-01.example.com"
          external: true
        state: present
      register: ext_gs

    # ── Delete a generic system ────────────────────────────────────────

    - name: Delete a generic system
      juniper.apstra.generic_systems:
        id:
          blueprint: "{{ blueprint_id }}"
          system_id: "{{ gs_create.system_id }}"
        state: absent

    # ── Delete with connectivity template cleanup ──────────────────────

    - name: Delete generic system and clear CTs first
      juniper.apstra.generic_systems:
        id:
          blueprint: "{{ blueprint_id }}"
          system_id: "{{ gs_create.system_id }}"
        body:
          clear_cts_on_destroy: true
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
        <div class="ansibleOptionAnchor" id="return-asn"></div>

      .. _ansible_collections.juniper.apstra.generic_systems_module__return-asn:

      .. rst-class:: ansible-option-title

      **asn**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-asn" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The ASN assigned to the generic system.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when system exists and ASN is set


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-blueprint_id"></div>

      .. _ansible_collections.juniper.apstra.generic_systems_module__return-blueprint_id:

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

      The blueprint ID.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-changed"></div>

      .. _ansible_collections.juniper.apstra.generic_systems_module__return-changed:

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

      .. _ansible_collections.juniper.apstra.generic_systems_module__return-changes:

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

      Dictionary of changes made during an update.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on update when changes are made


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-deploy_mode"></div>

      .. _ansible_collections.juniper.apstra.generic_systems_module__return-deploy_mode:

      .. rst-class:: ansible-option-title

      **deploy_mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-deploy_mode" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The deploy mode of the generic system.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when system exists


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-external"></div>

      .. _ansible_collections.juniper.apstra.generic_systems_module__return-external:

      .. rst-class:: ansible-option-title

      **external**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-external" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Whether this is an external generic system.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when system exists


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-hostname"></div>

      .. _ansible_collections.juniper.apstra.generic_systems_module__return-hostname:

      .. rst-class:: ansible-option-title

      **hostname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-hostname" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The hostname of the generic system.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when system exists


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-links"></div>

      .. _ansible_collections.juniper.apstra.generic_systems_module__return-links:

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

      List of link IDs associated with the generic system.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on create


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-loopback_ipv4"></div>

      .. _ansible_collections.juniper.apstra.generic_systems_module__return-loopback_ipv4:

      .. rst-class:: ansible-option-title

      **loopback_ipv4**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-loopback_ipv4" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The IPv4 loopback address of the generic system.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when system exists and loopback is set


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-loopback_ipv6"></div>

      .. _ansible_collections.juniper.apstra.generic_systems_module__return-loopback_ipv6:

      .. rst-class:: ansible-option-title

      **loopback_ipv6**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-loopback_ipv6" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The IPv6 loopback address of the generic system.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when system exists and loopback is set


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.juniper.apstra.generic_systems_module__return-msg:

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
        <div class="ansibleOptionAnchor" id="return-name"></div>

      .. _ansible_collections.juniper.apstra.generic_systems_module__return-name:

      .. rst-class:: ansible-option-title

      **name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-name" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The display name (label) of the generic system.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when system exists


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-port_channel_id_max"></div>

      .. _ansible_collections.juniper.apstra.generic_systems_module__return-port_channel_id_max:

      .. rst-class:: ansible-option-title

      **port_channel_id_max**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-port_channel_id_max" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Maximum port\-channel ID.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when system exists


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-port_channel_id_min"></div>

      .. _ansible_collections.juniper.apstra.generic_systems_module__return-port_channel_id_min:

      .. rst-class:: ansible-option-title

      **port_channel_id_min**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-port_channel_id_min" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Minimum port\-channel ID.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when system exists


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-system_id"></div>

      .. _ansible_collections.juniper.apstra.generic_systems_module__return-system_id:

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

      The graph node ID of the generic system.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on create or when identified


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-tags"></div>

      .. _ansible_collections.juniper.apstra.generic_systems_module__return-tags:

      .. rst-class:: ansible-option-title

      **tags**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-tags" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The tags applied to the generic system node.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when system exists


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

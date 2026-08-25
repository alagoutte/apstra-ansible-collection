.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. Anchors

.. _ansible_collections.juniper.apstra.blueprint_module:

.. Anchors: short name for ansible.builtin

.. Title

juniper.apstra.blueprint module -- Manage Apstra blueprints
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `juniper.apstra collection <https://galaxy.ansible.com/ui/repo/published/juniper/apstra/>`_ (version 1.1.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install juniper.apstra`.

    To use it in a playbook, specify: :code:`juniper.apstra.blueprint`.

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

- Create, commit, lock, unlock, and delete Apstra blueprints.
- Run graph queries (QE) to discover nodes and interfaces within a blueprint using :literal:`state=queried`.
- Patch individual node properties such as system\_id and deploy\_mode using :literal:`state=node\_updated`.
- Run commit checks (dry\-run validation) and collect build errors and deploy diagnostics using :literal:`state=commit\_check`.
- The QE query and node utilities are also available as importable helpers in :literal:`module\_utils/apstra/bp\_query.py` and :literal:`module\_utils/apstra/bp\_nodes.py` for use by other modules.


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
        <div class="ansibleOptionAnchor" id="parameter-admin_state"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-admin_state:

      .. rst-class:: ansible-option-title

      **admin_state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-admin_state" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Desired administrative state of the interface.

      :literal:`up` enables the interface (no\-shut).

      :literal:`down` disables the interface (shut).

      Only used when :literal:`state=interface\_updated` in single\-interface mode.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"up"`
      - :ansible-option-choices-entry:`"down"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-api_url"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-api_url:

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
        <div class="ansibleOptionAnchor" id="parameter-assignment"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-assignment:

      .. rst-class:: ansible-option-title

      **assignment**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-assignment" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Dict mapping blueprint node labels to physical device serial numbers (\ :literal:`system\_id`\ ) for bulk assignment.

      Example: :literal:`{spine1: SERIAL001, spine2: SERIAL002, leaf1: SERIAL003}`.

      When :literal:`deploy\_mode` is also specified, it is applied to every node in the dict.

      Mutually exclusive with :literal:`node\_id`.

      Only used when :literal:`state=node\_updated`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-auth_token"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-auth_token:

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

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-body:

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

      A dictionary representing the blueprint to create.

      Must include :literal:`label` and :literal:`design`.

      Supported designs: :literal:`two\_stage\_l3clos` (spine\-leaf), :literal:`three\_stage\_l3clos` (5\-stage), :literal:`freeform`\ , :literal:`collapsed`.

      Optional keys: :literal:`init\_type` (e.g. :literal:`template\_reference`\ ), :literal:`template\_id`.

      :literal:`template\_id` accepts either the template ID (e.g. :literal:`L2\_Virtual\_EVPN`\ ) or the template display name (e.g. :literal:`L2 Virtual EVPN`\ ). When a display name is provided, the module resolves it to the corresponding template ID automatically.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-commit_description"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-commit_description:

      .. rst-class:: ansible-option-title

      **commit_description**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-commit_description" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Optional description for the commit, visible in the Apstra revision history (same as the :literal:`Description` field in the Web UI).

      Only used when :literal:`state=committed`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-commit_timeout"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-commit_timeout:

      .. rst-class:: ansible-option-title

      **commit_timeout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-commit_timeout" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The timeout in seconds for committing the blueprint.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`30`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-current_label"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-current_label:

      .. rst-class:: ansible-option-title

      **current_label**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-current_label" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Current label (display name) of the node to update.

      Used as an alternative to :literal:`node\_id` — the module resolves the label to a node UUID automatically.

      Mutually exclusive with :literal:`node\_id`.

      Only used when :literal:`state=node\_updated`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-deploy_mode"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-deploy_mode:

      .. rst-class:: ansible-option-title

      **deploy_mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-deploy_mode" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Deploy mode to set on the node.

      Only used when :literal:`state=node\_updated`.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"deploy"`
      - :ansible-option-choices-entry:`"undeploy"`
      - :ansible-option-choices-entry:`"drain"`
      - :ansible-option-choices-entry:`"ready"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-host_labels"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-host_labels:

      .. rst-class:: ansible-option-title

      **host_labels**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-host_labels" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Host labels filter (\ :literal:`query\_type=host\_bond\_interfaces`\ ).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-hostname"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-hostname:

      .. rst-class:: ansible-option-title

      **hostname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-hostname" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Hostname to set on the node.

      Only used when :literal:`state=node\_updated`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-id:

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

      The ID of the blueprint.

      Example: :literal:`{blueprint: abc\-123}`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-if_type"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-if_type:

      .. rst-class:: ansible-option-title

      **if_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-if_type" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Interface type filter (\ :literal:`query\_type=interfaces\_by\_neighbor`\ ).


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"ethernet"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-include_warnings"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-include_warnings:

      .. rst-class:: ansible-option-title

      **include_warnings**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-include_warnings" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Include warnings in the commit check output.

      Only used when :literal:`state=commit\_check`.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-interface_name"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-interface_name:

      .. rst-class:: ansible-option-title

      **interface_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-interface_name" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The interface name on the system (e.g. :literal:`ge\-0/0/0`\ , :literal:`ae4`\ ).

      Required when :literal:`state=interface\_updated`\ , :literal:`state=interface\_tagged`\ , or :literal:`state=lag\_updated`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-interfaces"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-interfaces:

      .. rst-class:: ansible-option-title

      **interfaces**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-interfaces" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of interfaces to update in a single task (batch mode).

      Only used when :literal:`state=interface\_updated`.

      Each entry must have :literal:`system\_name`\ , :literal:`interface\_name`\ , and :literal:`admin\_state`.

      Mutually exclusive with single\-interface mode (\ :literal:`system\_name` / :literal:`interface\_name` / :literal:`admin\_state`\ ).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lag_mode"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-lag_mode:

      .. rst-class:: ansible-option-title

      **lag_mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lag_mode" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      LAG mode to set on a port\-channel interface of a managed switch.

      Only used when :literal:`state=lag\_updated`.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"lacp\_active"`
      - :ansible-option-choices-entry:`"lacp\_passive"`
      - :ansible-option-choices-entry:`"static\_lag"`
      - :ansible-option-choices-entry:`"none"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-local_role"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-local_role:

      .. rst-class:: ansible-option-title

      **local_role**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-local_role" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Local switch role (\ :literal:`query\_type=interfaces\_by\_neighbor`\ ).


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"leaf"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lock_state"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-lock_state:

      .. rst-class:: ansible-option-title

      **lock_state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lock_state" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Status to transition lock to.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"locked"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"unlocked"`
      - :ansible-option-choices-entry:`"ignore"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lock_timeout"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-lock_timeout:

      .. rst-class:: ansible-option-title

      **lock_timeout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lock_timeout" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The timeout in seconds for locking the blueprint.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`60`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-neighbor_labels"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-neighbor_labels:

      .. rst-class:: ansible-option-title

      **neighbor_labels**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-neighbor_labels" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Neighbor labels to match (\ :literal:`query\_type=interfaces\_by\_neighbor`\ ).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-neighbor_system_type"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-neighbor_system_type:

      .. rst-class:: ansible-option-title

      **neighbor_system_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-neighbor_system_type" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Neighbor system\_type (\ :literal:`query\_type=interfaces\_by\_neighbor`\ ).


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"server"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-node_id"></div>
        <div class="ansibleOptionAnchor" id="parameter-rack_id"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-node_id:
      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-rack_id:

      .. rst-class:: ansible-option-title

      **node_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-node_id" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-aliases:`aliases: rack_id`

        :ansible-option-type:`any`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The blueprint node(s) to patch in :literal:`state=node\_updated`.

      Accepts a single value or a list of values.

      Each value may be a node UUID, a graph\-node short ID, or a device label (e.g. :literal:`leaf1`\ ). Labels are resolved to their graph\-node UUID automatically.

      Mutually exclusive with :literal:`assignment`.

      Only used when :literal:`state=node\_updated`.

      Alias :literal:`rack\_id` can be used for rack operations.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-node_label"></div>
        <div class="ansibleOptionAnchor" id="parameter-rack_label"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-node_label:
      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-rack_label:

      .. rst-class:: ansible-option-title

      **node_label**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-node_label" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-aliases:`aliases: rack_label`

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Label to set on the node.

      Only used when :literal:`state=node\_updated`.

      Alias :literal:`rack\_label` can be used for rack operations.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-node_properties"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-node_properties:

      .. rst-class:: ansible-option-title

      **node_properties**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-node_properties" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Arbitrary dict of node properties to patch.

      Only used when :literal:`state=node\_updated`.

      Use this for fields not covered by the dedicated params (e.g. :literal:`if\_name`\ , :literal:`external`\ ).

      Fields requiring :literal:`allow\_unsafe=true` are handled automatically.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-node_type"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-node_type:

      .. rst-class:: ansible-option-title

      **node_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-node_type" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Node type filter used when resolving :literal:`current\_label` to a node UUID.

      When set (e.g. :literal:`rack`\ , :literal:`system`\ ), only nodes of that type are considered during label lookup, avoiding false matches when nodes of different types share the same label.

      Only used when :literal:`state=node\_updated` together with :literal:`current\_label`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-password:

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
        <div class="ansibleOptionAnchor" id="parameter-port_channel_id"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-port_channel_id:

      .. rst-class:: ansible-option-title

      **port_channel_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-port_channel_id" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Optional port\-channel interface number (e.g. :literal:`4` for :literal:`ae4`\ ).

      When set, updates the :literal:`port\_channel\_id` field alongside :literal:`lag\_mode`.

      Only used when :literal:`state=lag\_updated`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-query"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-query:

      .. rst-class:: ansible-option-title

      **query**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-query" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A raw QE query string.

      Only used when :literal:`state=queried`.

      Uses Apstra graph query syntax, for example :literal:`node('system', role='spine', name='system'`\ ).

      Mutually exclusive with :literal:`query\_type`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-query_type"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-query_type:

      .. rst-class:: ansible-option-title

      **query_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-query_type" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A built\-in convenience query.

      Only used when :literal:`state=queried`.

      :literal:`nodes\_by\_role` returns system nodes filtered by :literal:`roles`.

      :literal:`nodes\_by\_type` returns system nodes filtered by :literal:`system\_type`.

      :literal:`interfaces\_by\_neighbor` returns switch interfaces linked to systems whose labels are in :literal:`neighbor\_labels`.

      :literal:`host\_bond\_interfaces` returns port\-channel interfaces on host generic systems, optionally filtered by :literal:`host\_labels`.

      :literal:`host\_evpn\_interfaces` returns ESI\-LAG group interfaces (EVPN port\-channels) for host systems, optionally filtered by :literal:`host\_labels`. These are the correct application points for VN endpoint\-policy assignment in dual\-homed topologies.

      Mutually exclusive with :literal:`query`.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"nodes\_by\_role"`
      - :ansible-option-choices-entry:`"nodes\_by\_type"`
      - :ansible-option-choices-entry:`"interfaces\_by\_neighbor"`
      - :ansible-option-choices-entry:`"host\_bond\_interfaces"`
      - :ansible-option-choices-entry:`"host\_evpn\_interfaces"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-rack_count"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-rack_count:

      .. rst-class:: ansible-option-title

      **rack_count**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-rack_count" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Desired total number of racks of :literal:`rack\_type` to exist in the blueprint.

      Declarative/idempotent behavior the module only adds missing racks until the desired total is reached.

      Mutually exclusive with :literal:`racks\_to\_add`.

      Only used when :literal:`state=rack\_added`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-rack_type"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-rack_type:

      .. rst-class:: ansible-option-title

      **rack_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-rack_type" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Rack type reference for :literal:`state=rack\_added`.

      Accepts either rack type ID (for example :literal:`L2\_Virtual`\ ) or display name (for example :literal:`L2 Virtual`\ ).

      Required when :literal:`state=rack\_added`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-racks_to_add"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-racks_to_add:

      .. rst-class:: ansible-option-title

      **racks_to_add**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-racks_to_add" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Number of racks to add in this run.

      Imperative/non\-idempotent behavior (WebUI\-style) each run adds this many racks regardless of current count.

      Mutually exclusive with :literal:`rack\_count`.

      Only used when :literal:`state=rack\_added`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-roles"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-roles:

      .. rst-class:: ansible-option-title

      **roles**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-roles" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of system roles to filter (\ :literal:`query\_type=nodes\_by\_role`\ ).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-state:

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

      The desired state of the blueprint.

      :literal:`present` creates or verifies the blueprint exists.

      :literal:`committed` deploys (commits) the blueprint.

      :literal:`absent` deletes the blueprint.

      :literal:`queried` runs a graph query against the blueprint (read\-only, never modifies the blueprint).

      :literal:`node\_updated` patches properties on one or more blueprint nodes. Use :literal:`node\_id` to target a single node by UUID, or :literal:`assignment` to assign multiple nodes by label in one task.

      :literal:`rack\_added` adds racks of a rack type using either :literal:`rack\_count` (desired total, idempotent) or :literal:`racks\_to\_add` (delta, non\-idempotent).

      :literal:`rack\_deleted` deletes rack(s) by :literal:`rack\_id` / :literal:`node\_id`.

      :literal:`commit\_check` runs a dry\-run validation and collects build errors and deploy diagnostics without deploying (read\-only).

      :literal:`interface\_updated` sets the admin state (shut/no\-shut) of a blueprint interface node. Use :literal:`system\_name`\ , :literal:`interface\_name`\ , and :literal:`admin\_state` to target and configure the interface.

      :literal:`interface\_tagged` adds or removes tags on a blueprint interface node. Use :literal:`system\_name`\ , :literal:`interface\_name`\ , :literal:`tags`\ , and :literal:`state=interface\_tagged` with :literal:`tag\_state=present/absent`.

      :literal:`lag\_updated` sets :literal:`lag\_mode` (and optionally :literal:`port\_channel\_id`\ ) on a port\-channel interface of a managed switch.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"committed"`
      - :ansible-option-choices-entry:`"absent"`
      - :ansible-option-choices-entry:`"queried"`
      - :ansible-option-choices-entry:`"node\_updated"`
      - :ansible-option-choices-entry:`"rack\_added"`
      - :ansible-option-choices-entry:`"rack\_deleted"`
      - :ansible-option-choices-entry:`"commit\_check"`
      - :ansible-option-choices-entry:`"interface\_updated"`
      - :ansible-option-choices-entry:`"interface\_tagged"`
      - :ansible-option-choices-entry:`"lag\_updated"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-system_id"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-system_id:

      .. rst-class:: ansible-option-title

      **system_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-system_id" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Physical device serial to assign to the node.

      Only used when :literal:`state=node\_updated`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-system_name"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-system_name:

      .. rst-class:: ansible-option-title

      **system_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-system_name" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The label of the system (switch/server) node in the blueprint.

      Required when :literal:`state=interface\_updated`\ , :literal:`state=interface\_tagged`\ , or :literal:`state=lag\_updated`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-system_type"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-system_type:

      .. rst-class:: ansible-option-title

      **system_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-system_type" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      System type filter (\ :literal:`query\_type=nodes\_by\_type`\ ).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tag_state"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-tag_state:

      .. rst-class:: ansible-option-title

      **tag_state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-tag_state" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Whether to add or remove the specified :literal:`tags` on the interface.

      :literal:`present` ensures the tags exist on the interface node.

      :literal:`absent` removes the tags from the interface node.

      Only used when :literal:`state=interface\_tagged`.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"absent"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tags"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-tags:

      .. rst-class:: ansible-option-title

      **tags**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-tags" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of tag labels to add or remove on the interface node.

      Only used when :literal:`state=interface\_tagged`.

      Combined with :literal:`tag\_state` to determine whether tags are added or removed.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-unlock"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-unlock:

      .. rst-class:: ansible-option-title

      **unlock**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-unlock" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      When set to :literal:`true`\ , unlocks the blueprint after the operation completes.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-username:

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

      .. _ansible_collections.juniper.apstra.blueprint_module__parameter-verify_certificates:

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

    # Create a new blueprint (using template ID)
    - name: Create blueprint
      juniper.apstra.blueprint:
        body:
          label: my-blueprint
          design: two_stage_l3clos
          init_type: template_reference
          template_id: L2_Virtual_EVPN
        state: present
      register: bp

    # Create a new blueprint (using template display name)
    - name: Create blueprint by template name
      juniper.apstra.blueprint:
        body:
          label: my-blueprint
          design: two_stage_l3clos
          init_type: template_reference
          template_id: "L2 Virtual EVPN"
        state: present
      register: bp

    # Commit (deploy) a blueprint
    - name: Deploy blueprint
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ bp.id.blueprint }}"
        lock_state: ignore
        state: committed

    # Commit with a description (visible in revision history)
    - name: Deploy blueprint with description
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ bp.id.blueprint }}"
        lock_state: ignore
        commit_description: "Push spine/leaf IP addressing changes"
        state: committed

    # Delete a blueprint
    - name: Delete blueprint
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        state: absent

    # Run a raw QE query
    - name: Query all spine nodes
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        query: "node('system', role='spine', name='system')"
        state: queried
      register: spines

    # Discover nodes by role (convenience query)
    - name: Get all spine and leaf nodes
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        query_type: nodes_by_role
        roles:
          - spine
          - leaf
        state: queried
      register: switch_nodes

    # Find SRX-facing interfaces for CT assignment
    - name: Find interfaces connected to SRX systems
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        query_type: interfaces_by_neighbor
        neighbor_labels:
          - srx1
          - srx2
        state: queried
      register: srx_intfs

    # Find host bond interfaces
    - name: Find all host port-channel interfaces
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        query_type: host_bond_interfaces
        host_labels:
          - host1
          - host2
        state: queried
      register: host_intfs

    # Bulk-assign serials to multiple nodes by label in one task
    - name: Assign devices to all fabric nodes
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        assignment:
          spine1: "SERIAL001"
          spine2: "SERIAL002"
          leaf1: "SERIAL003"
          leaf2: "SERIAL004"
        deploy_mode: deploy
        state: node_updated
      register: assigned

    # Assign system_id to a single blueprint node (by UUID)
    - name: Bind device serial to spine1
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        node_id: "{{ spine1_node_id }}"
        system_id: "SERIAL12345"
        state: node_updated

    # Set deploy mode on a node by label (no UUID lookup needed)
    - name: Set leaf1 to drain mode by label
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        node_id: "leaf1"
        deploy_mode: drain
        state: node_updated

    # Set deploy mode on multiple nodes by label (list form)
    - name: Set leaf1 and leaf2 to drain mode
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        node_id:
          - "leaf1"
          - "leaf2"
        deploy_mode: drain
        state: node_updated

    # Set deploy mode on a node (legacy UUID form still works)
    - name: Set leaf1 to deploy mode
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        node_id: "{{ leaf1_node_id }}"
        deploy_mode: deploy
        state: node_updated

    # Set arbitrary node properties (e.g. interface name)
    - name: Set interface name on SRX
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        node_id: "{{ srx_intf_id }}"
        node_properties:
          if_name: ge-0/0/0
        state: node_updated

    # Update device name and hostname by current label (no node_id needed)
    - name: Rename leaf1 and update its hostname
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        current_label: "leaf1"
        node_label: "leaf1-new"
        hostname: "leaf1-new.example.com"
        state: node_updated

    # Rename a rack by its current label (use node_type to target rack nodes)
    - name: Rename rack from 'da_rack_001' to 'border-rack-1'
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        current_label: "da_rack_001"
        rack_label: "border-rack-1"
        node_type: rack
        state: node_updated


    # Add 2 racks (WebUI-style, non-idempotent)
    - name: Add 2 racks of type 'AOS-2x10-1' (non-idempotent)
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        rack_type: "AOS-2x10-1"
        racks_to_add: 2
        state: rack_added
      register: racks_result

    # Ensure at least 1 rack exists (idempotent)
    - name: Ensure at least 1 rack of type 'AOS-2x10-1' exists (idempotent)
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        rack_type: "AOS-2x10-1"
        rack_count: 1
        state: rack_added

    # Delete a rack by its blueprint rack ID
    - name: Remove a rack from the blueprint
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        rack_id: "{{ rack_node_id }}"
        state: rack_deleted

    # Delete a rack by its label (name resolution handled automatically)
    - name: Remove rack by label
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        rack_id: "da_rack_001"
        state: rack_deleted

    # Run commit checks (dry-run validation) before deploying
    - name: Validate blueprint before deploying
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        include_warnings: true
        state: commit_check
      register: check_result

    - name: Verify commit check output fields
      ansible.builtin.assert:
        that:
          - check_result.changed == false
          - check_result.errors is defined
          - check_result.errors_count is defined
          - check_result.warnings_count is defined
          - check_result.commit_warnings is defined
          - check_result.deploy_ready is defined
          - check_result.diagnostics is defined

    # Run commit checks without warnings
    - name: Check for errors only (no warnings)
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        state: commit_check
        include_warnings: false
      register: check_errors_only

    - name: Verify warnings are excluded
      ansible.builtin.assert:
        that:
          - check_errors_only.commit_warnings is not defined
          - check_errors_only.errors is defined
          - check_errors_only.deploy_ready is defined

    # Commit check is read-only/idempotent
    - name: Run commit check again (default include_warnings=true)
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        state: commit_check
      register: check_again

    - name: Verify commit check remains read-only
      ansible.builtin.assert:
        that:
          - check_again.changed == false
          - check_again.commit_warnings is defined

    # Shut down an interface (admin down)
    - name: Shut leaf1 ge-0/0/0 interface
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        system_name: "leaf1"
        interface_name: "ge-0/0/0"
        admin_state: "down"
        state: interface_updated
      register: intf_shut

    # Re-enable a shut-down interface
    - name: No-shut leaf1 ge-0/0/0
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        system_name: "leaf1"
        interface_name: "ge-0/0/0"
        admin_state: "up"
        state: interface_updated

    # Batch shut multiple interfaces in one task
    - name: Shut down multiple spine interfaces
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        interfaces:
          - system_name: "spine1"
            interface_name: "et-0/0/0"
            admin_state: "down"
          - system_name: "spine1"
            interface_name: "et-0/0/1"
            admin_state: "down"
          - system_name: "spine2"
            interface_name: "et-0/0/0"
            admin_state: "up"
        state: interface_updated

    # Add tags to an ethernet interface
    - name: Tag leaf1 ge-0/0/0 as 'uplink' and 'production'
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        system_name: "leaf1"
        interface_name: "ge-0/0/0"
        tags:
          - uplink
          - production
        tag_state: present
        state: interface_tagged

    # Remove a tag from an interface
    - name: Remove 'uplink' tag from leaf1 ge-0/0/0
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        system_name: "leaf1"
        interface_name: "ge-0/0/0"
        tags:
          - uplink
        tag_state: absent
        state: interface_tagged

    # Change LAG mode on a port-channel interface
    - name: Set leaf1 ae4 to lacp_passive
      juniper.apstra.blueprint:
        id:
          blueprint: "{{ blueprint_id }}"
        system_name: "leaf1"
        interface_name: "ae4"
        lag_mode: "lacp_passive"
        state: lag_updated



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
        <div class="ansibleOptionAnchor" id="return-admin_state"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-admin_state:

      .. rst-class:: ansible-option-title

      **admin_state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-admin_state" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The resolved admin state of the interface after the operation.

      Returned by :literal:`state=interface\_updated`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when using interface\_updated

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"down"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-changed"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-changed:

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

      Whether the blueprint was changed.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`true`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-commit_warnings"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-commit_warnings:

      .. rst-class:: ansible-option-title

      **commit_warnings**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-commit_warnings" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of categorized warning dicts.

      Returned by :literal:`state=commit\_check` when :literal:`include\_warnings=true`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when using commit\_check with include\_warnings


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-deploy_ready"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-deploy_ready:

      .. rst-class:: ansible-option-title

      **deploy_ready**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-deploy_ready" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Whether the blueprint is ready for deployment.

      Returned by :literal:`state=commit\_check`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when using commit\_check

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`true`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-diagnostics"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-diagnostics:

      .. rst-class:: ansible-option-title

      **diagnostics**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-diagnostics" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Raw deploy diagnostics data from the Apstra API.

      Returned by :literal:`state=commit\_check`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when using commit\_check


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-errors"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-errors:

      .. rst-class:: ansible-option-title

      **errors**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-errors" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of categorized build error dicts.

      Returned by :literal:`state=commit\_check`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when using commit\_check

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`[{"message": "BGP session failed", "node": "spine1", "severity": "error", "type": "config\_error"}]`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-errors_count"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-errors_count:

      .. rst-class:: ansible-option-title

      **errors_count**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-errors_count" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Total number of errors found.

      Returned by :literal:`state=commit\_check`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when using commit\_check


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-host_interfaces"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-host_interfaces:

      .. rst-class:: ansible-option-title

      **host_interfaces**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-host_interfaces" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Mapping of host label to port\-channel interface ID.

      Returned by :literal:`host\_bond\_interfaces`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when using host\_bond\_interfaces


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-id"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-id:

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

      The ID of the created blueprint.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on create

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"blueprint": "blueprint\-123"}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-interface_ids"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-interface_ids:

      .. rst-class:: ansible-option-title

      **interface_ids**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-interface_ids" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Flat list of interface IDs for easy consumption.

      Returned by :literal:`interfaces\_by\_neighbor`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when using interfaces\_by\_neighbor


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-interface_node_id"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-interface_node_id:

      .. rst-class:: ansible-option-title

      **interface_node_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-interface_node_id" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The blueprint node UUID of the interface that was targeted.

      Returned by :literal:`state=interface\_updated`\ , :literal:`state=interface\_tagged`\ , and :literal:`state=lag\_updated`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when using interface management states


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-interface_tags"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-interface_tags:

      .. rst-class:: ansible-option-title

      **interface_tags**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-interface_tags" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Final list of tag labels on the interface node after the operation.

      Returned by :literal:`state=interface\_tagged`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when using interface\_tagged


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-interfaces"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-interfaces:

      .. rst-class:: ansible-option-title

      **interfaces**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-interfaces" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of interface dicts.

      Returned by :literal:`interfaces\_by\_neighbor`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when using interfaces\_by\_neighbor


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-lag_mode"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-lag_mode:

      .. rst-class:: ansible-option-title

      **lag_mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-lag_mode" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The final :literal:`lag\_mode` on the interface node after the operation.

      Returned by :literal:`state=lag\_updated`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when using lag\_updated

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"lacp\_passive"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-lock_state"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-lock_state:

      .. rst-class:: ansible-option-title

      **lock_state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-lock_state" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      State of the blueprint lock.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on present/committed/absent

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"locked"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-msg:

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

      A message describing the result.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"blueprint created successfully"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-node"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-node:

      .. rst-class:: ansible-option-title

      **node**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-node" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Node properties after patch.

      Returned by :literal:`state=node\_updated`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when using node\_updated


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-nodes"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-nodes:

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

      Mapping of node label to node properties.

      Returned by :literal:`nodes\_by\_role` and :literal:`nodes\_by\_type`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when using nodes\_by\_role or nodes\_by\_type

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"spine1": {"id": "abc\-123", "role": "spine"}}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-nodes_unchanged"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-nodes_unchanged:

      .. rst-class:: ansible-option-title

      **nodes_unchanged**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-nodes_unchanged" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of node labels that were already at the desired state (no patch needed) during a bulk :literal:`assignment` call.

      Returned by :literal:`state=node\_updated` with :literal:`assignment`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when using assignment


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-nodes_updated"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-nodes_updated:

      .. rst-class:: ansible-option-title

      **nodes_updated**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-nodes_updated" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Mapping of node label to final node properties for every node that was patched during a bulk :literal:`assignment` call.

      Returned by :literal:`state=node\_updated` with :literal:`assignment`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when using assignment


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-operation_state"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-operation_state:

      .. rst-class:: ansible-option-title

      **operation_state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-operation_state" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The raw Apstra :literal:`operation\_state` value on the interface node.

      :literal:`"up"` means enabled; :literal:`"admin\_down"` means shut.

      Returned by :literal:`state=interface\_updated`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when using interface\_updated

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"admin\_down"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-rack_type_id"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-rack_type_id:

      .. rst-class:: ansible-option-title

      **rack_type_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-rack_type_id" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Resolved rack type ID used for the operation.

      Returned by :literal:`state=rack\_added`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when using rack\_added


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-racks"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-racks:

      .. rst-class:: ansible-option-title

      **racks**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-racks" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of rack dicts currently in the blueprint for the requested rack type after the operation.

      Returned by :literal:`state=rack\_added`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when using rack\_added


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-racks_added"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-racks_added:

      .. rst-class:: ansible-option-title

      **racks_added**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-racks_added" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Number of racks added during this run.

      Returned by :literal:`state=rack\_added` when :literal:`changed=true`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when racks were added


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-racks_deleted"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-racks_deleted:

      .. rst-class:: ansible-option-title

      **racks_deleted**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-racks_deleted" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of rack node IDs that were deleted.

      Returned by :literal:`state=rack\_deleted` when :literal:`changed=true`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when racks were deleted


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-response"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-response:

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

      The response from the Apstra API.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on create


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-results"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-results:

      .. rst-class:: ansible-option-title

      **results**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-results" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Raw QE query results (list of dicts).

      Returned when :literal:`state=queried` with :literal:`query`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when using raw query


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-warnings_count"></div>

      .. _ansible_collections.juniper.apstra.blueprint_module__return-warnings_count:

      .. rst-class:: ansible-option-title

      **warnings_count**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-warnings_count" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Total number of warnings found.

      Returned by :literal:`state=commit\_check`.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when using commit\_check


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Edwin Jacques (@edwinpjacques)
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

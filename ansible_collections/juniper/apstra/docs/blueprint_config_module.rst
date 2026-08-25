.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. Anchors

.. _ansible_collections.juniper.apstra.blueprint_config_module:

.. Anchors: short name for ansible.builtin

.. Title

juniper.apstra.blueprint_config module -- Collect rendered device configurations from an Apstra blueprint
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `juniper.apstra collection <https://galaxy.ansible.com/ui/repo/published/juniper/apstra/>`_ (version 1.1.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install juniper.apstra`.
    You need further requirements to be able to use this module,
    see :ref:`Requirements <ansible_collections.juniper.apstra.blueprint_config_module_requirements>` for details.

    To use it in a playbook, specify: :code:`juniper.apstra.blueprint_config`.

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

- This module collects the rendered configuration from devices in an Apstra blueprint for external storage, backup, compliance auditing, or version control.
- Configurations are retrieved per device via the :literal:`/api/blueprints/{id}/nodes/{node\_id}/config\-rendering` API endpoint.
- Supports filtering by device name, device role (spine, leaf, etc.), or an explicit list of device names.
- Optionally saves rendered configs to local files (one file per device).


.. Aliases


.. Requirements

.. _ansible_collections.juniper.apstra.blueprint_config_module_requirements:

Requirements
------------
The below requirements are needed on the host that executes this module.

- python \>= 3.10
- aos\-sdk \>= 0.1.0






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

      .. _ansible_collections.juniper.apstra.blueprint_config_module__parameter-api_url:

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

      .. _ansible_collections.juniper.apstra.blueprint_config_module__parameter-auth_token:

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
        <div class="ansibleOptionAnchor" id="parameter-devices"></div>

      .. _ansible_collections.juniper.apstra.blueprint_config_module__parameter-devices:

      .. rst-class:: ansible-option-title

      **devices**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-devices" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of device hostnames to collect configs for.

      If omitted, configs are collected for all devices in the blueprint.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-filename_pattern"></div>

      .. _ansible_collections.juniper.apstra.blueprint_config_module__parameter-filename_pattern:

      .. rst-class:: ansible-option-title

      **filename_pattern**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-filename_pattern" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Pattern for output filenames when :literal:`output\_dir` is specified.

      Supports :literal:`{hostname}` placeholder.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"{hostname}.conf"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id"></div>

      .. _ansible_collections.juniper.apstra.blueprint_config_module__parameter-id:

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

      Dictionary containing the blueprint identifier.

      :literal:`blueprint` is the blueprint ID or label.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-output_dir"></div>

      .. _ansible_collections.juniper.apstra.blueprint_config_module__parameter-output_dir:

      .. rst-class:: ansible-option-title

      **output_dir**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-output_dir" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Directory path to save rendered config files.

      One file per device will be created.

      Directory will be created if it does not exist.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.juniper.apstra.blueprint_config_module__parameter-password:

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
        <div class="ansibleOptionAnchor" id="parameter-role"></div>

      .. _ansible_collections.juniper.apstra.blueprint_config_module__parameter-role:

      .. rst-class:: ansible-option-title

      **role**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-role" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Filter devices by role.

      Common roles include :literal:`spine`\ , :literal:`leaf`\ , :literal:`superspine`\ , :literal:`access`.

      Cannot be used together with :literal:`devices`.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"spine"`
      - :ansible-option-choices-entry:`"leaf"`
      - :ansible-option-choices-entry:`"superspine"`
      - :ansible-option-choices-entry:`"access"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.juniper.apstra.blueprint_config_module__parameter-state:

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

      The action to perform.

      :literal:`collected` retrieves rendered configurations.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"collected"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.juniper.apstra.blueprint_config_module__parameter-username:

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

      .. _ansible_collections.juniper.apstra.blueprint_config_module__parameter-verify_certificates:

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

    - name: Collect rendered config for all devices in a blueprint
      juniper.apstra.blueprint_config:
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
        auth_token: "{{ auth.token }}"
      register: result

    - name: Collect config for specific devices
      juniper.apstra.blueprint_config:
        id:
          blueprint: "my-blueprint"
        devices:
          - spine1
          - leaf1
        auth_token: "{{ auth.token }}"
      register: result

    - name: Collect config for all spine devices
      juniper.apstra.blueprint_config:
        id:
          blueprint: "my-blueprint"
        role: spine
        auth_token: "{{ auth.token }}"
      register: result

    - name: Collect and save configs to files
      juniper.apstra.blueprint_config:
        id:
          blueprint: "my-blueprint"
        output_dir: "/tmp/configs"
        filename_pattern: "{hostname}.conf"
        auth_token: "{{ auth.token }}"
      register: result

    - name: Collect configs for leaf devices and save to files
      juniper.apstra.blueprint_config:
        id:
          blueprint: "my-blueprint"
        role: leaf
        output_dir: "/tmp/leaf-configs"
        auth_token: "{{ auth.token }}"
      register: result



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

      .. _ansible_collections.juniper.apstra.blueprint_config_module__return-changed:

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

      Always false since this is a read\-only module.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`false`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-configs"></div>

      .. _ansible_collections.juniper.apstra.blueprint_config_module__return-configs:

      .. rst-class:: ansible-option-title

      **configs**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-configs" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Dictionary of rendered configurations keyed by device hostname. Each entry contains the hostname, rendered config text, and NOS type.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"leaf1": {"config": "hostname leaf1...", "hostname": "leaf1", "role": "leaf", "system\_id": "def456"}, "spine1": {"config": "set system host\-name spine1...", "hostname": "spine1", "role": "spine", "system\_id": "abc123"}}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-device_count"></div>

      .. _ansible_collections.juniper.apstra.blueprint_config_module__return-device_count:

      .. rst-class:: ansible-option-title

      **device_count**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-device_count" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Number of devices for which configs were collected.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`4`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-files_written"></div>

      .. _ansible_collections.juniper.apstra.blueprint_config_module__return-files_written:

      .. rst-class:: ansible-option-title

      **files_written**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-files_written" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of file paths written when output\_dir is specified.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when output\_dir is specified

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`["/tmp/configs/spine1.conf", "/tmp/configs/leaf1.conf"]`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.juniper.apstra.blueprint_config_module__return-msg:

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

      Status message.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


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

.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. Anchors

.. _ansible_collections.juniper.apstra.blueprint_health_module:

.. Anchors: short name for ansible.builtin

.. Title

juniper.apstra.blueprint_health module -- Collect anomalies and build errors from an Apstra blueprint
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `juniper.apstra collection <https://galaxy.ansible.com/ui/repo/published/juniper/apstra/>`_ (version 1.1.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install juniper.apstra`.

    To use it in a playbook, specify: :code:`juniper.apstra.blueprint_health`.

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

- This module collects anomalies and build errors/warnings from an Apstra blueprint as structured data for monitoring, alerting, and reporting.
- Anomalies are retrieved via :literal:`GET /api/blueprints/{id}/anomalies`.
- Build errors are retrieved via :literal:`GET /api/blueprints/{id}/errors`.
- Results can be filtered by scope, severity, anomaly type, and node.


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
        <div class="ansibleOptionAnchor" id="parameter-anomaly_type"></div>

      .. _ansible_collections.juniper.apstra.blueprint_health_module__parameter-anomaly_type:

      .. rst-class:: ansible-option-title

      **anomaly_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-anomaly_type" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Filter anomalies by anomaly type (e.g. :literal:`cabling`\ , :literal:`config`\ , :literal:`interface`\ , :literal:`bgp`\ , :literal:`route`\ , :literal:`arp`\ , :literal:`mac`\ , :literal:`series`\ , :literal:`streaming`\ , :literal:`hostname`\ , :literal:`liveness`\ , :literal:`deployment`\ ).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-api_url"></div>

      .. _ansible_collections.juniper.apstra.blueprint_health_module__parameter-api_url:

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

      .. _ansible_collections.juniper.apstra.blueprint_health_module__parameter-auth_token:

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
        <div class="ansibleOptionAnchor" id="parameter-id"></div>

      .. _ansible_collections.juniper.apstra.blueprint_health_module__parameter-id:

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

      Must include a :literal:`blueprint` key with the blueprint ID or label.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-node_filter"></div>

      .. _ansible_collections.juniper.apstra.blueprint_health_module__parameter-node_filter:

      .. rst-class:: ansible-option-title

      **node_filter**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-node_filter" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Filter anomalies by system/node name or ID.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.juniper.apstra.blueprint_health_module__parameter-password:

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
        <div class="ansibleOptionAnchor" id="parameter-scope"></div>

      .. _ansible_collections.juniper.apstra.blueprint_health_module__parameter-scope:

      .. rst-class:: ansible-option-title

      **scope**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-scope" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The type of health data to collect.

      :literal:`anomalies` collects blueprint anomalies only.

      :literal:`errors` collects build errors and warnings only.

      :literal:`all` collects both anomalies and build errors.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"anomalies"`
      - :ansible-option-choices-entry:`"errors"`
      - :ansible-option-choices-entry-default:`"all"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-severity"></div>

      .. _ansible_collections.juniper.apstra.blueprint_health_module__parameter-severity:

      .. rst-class:: ansible-option-title

      **severity**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-severity" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Filter results by severity level.

      Only applies to anomalies.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"critical"`
      - :ansible-option-choices-entry:`"warning"`
      - :ansible-option-choices-entry:`"info"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.juniper.apstra.blueprint_health_module__parameter-username:

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

      .. _ansible_collections.juniper.apstra.blueprint_health_module__parameter-verify_certificates:

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

    - name: Collect all health data from a blueprint
      juniper.apstra.blueprint_health:
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
      register: health

    - name: Collect anomalies only
      juniper.apstra.blueprint_health:
        id:
          blueprint: "my-blueprint-label"
        scope: anomalies
      register: anomalies

    - name: Collect only critical anomalies
      juniper.apstra.blueprint_health:
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
        scope: anomalies
        severity: critical
      register: critical_anomalies

    - name: Collect anomalies for a specific node
      juniper.apstra.blueprint_health:
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
        scope: anomalies
        node_filter: "leaf1"
      register: node_anomalies

    - name: Collect build errors only
      juniper.apstra.blueprint_health:
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
        scope: errors
      register: build_errors

    - name: Filter anomalies by type
      juniper.apstra.blueprint_health:
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
        scope: anomalies
        anomaly_type: "cabling"
      register: cabling_anomalies

    - name: Filter anomalies by type for a specific node
      juniper.apstra.blueprint_health:
        id:
          blueprint: "5f2a77f6-1f33-4e11-8d59-6f9c26f16962"
        scope: anomalies
        node_filter: "leaf1"
        anomaly_type: "cabling"
      register: leaf1_cabling_anomalies



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
        <div class="ansibleOptionAnchor" id="return-anomalies"></div>

      .. _ansible_collections.juniper.apstra.blueprint_health_module__return-anomalies:

      .. rst-class:: ansible-option-title

      **anomalies**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-anomalies" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Anomaly data from the blueprint.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when scope is 'anomalies' or 'all'

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"count": 5, "items": [{"message": "Interface mismatch detected", "node": "leaf1", "severity": "error", "type": "cabling"}]}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-changed"></div>

      .. _ansible_collections.juniper.apstra.blueprint_health_module__return-changed:

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
        <div class="ansibleOptionAnchor" id="return-errors"></div>

      .. _ansible_collections.juniper.apstra.blueprint_health_module__return-errors:

      .. rst-class:: ansible-option-title

      **errors**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-errors" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Build errors and warnings from the blueprint.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when scope is 'errors' or 'all'

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"errors\_count": 2, "warnings\_count": 1}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.juniper.apstra.blueprint_health_module__return-msg:

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

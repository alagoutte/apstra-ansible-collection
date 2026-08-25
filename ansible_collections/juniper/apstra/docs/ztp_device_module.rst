.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. Anchors

.. _ansible_collections.juniper.apstra.ztp_device_module:

.. Anchors: short name for ansible.builtin

.. Title

juniper.apstra.ztp_device module -- Manage ZTP (Zero Touch Provisioning) devices in Apstra
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `juniper.apstra collection <https://galaxy.ansible.com/ui/repo/published/juniper/apstra/>`_ (version 1.1.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install juniper.apstra`.

    To use it in a playbook, specify: :code:`juniper.apstra.ztp_device`.

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

- This module allows you to create, delete, and check the status of ZTP (Zero Touch Provisioning) devices in Apstra.
- ZTP devices are managed via the :literal:`/api/ztp/device` API endpoint.
- Device status can be retrieved using the :literal:`/api/ztp/device/{ip\_addr}/status` API endpoint by setting :literal:`state` to :literal:`status`.
- The :literal:`create\_agent` state calls the ZTP VM's :literal:`/api/ztp/create\_agent` endpoint to create a system agent AND track it in ZTP. This requires ZTP VM connection parameters.
- The :literal:`update\_status` state calls the ZTP VM's :literal:`/api/ztp/device/log` endpoint to update the device provisioning status. Setting task to :literal:`Device Ready` marks it as completed.
- The module uses the Apstra SDK when available, falling back to direct API calls if necessary.


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

      .. _ansible_collections.juniper.apstra.ztp_device_module__parameter-api_url:

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

      .. _ansible_collections.juniper.apstra.ztp_device_module__parameter-auth_token:

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

      .. _ansible_collections.juniper.apstra.ztp_device_module__parameter-body:

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

      Dictionary containing the ZTP device details.

      Used for create and update operations.

      :literal:`ip\_addr` (string) \- Management IP address of the device (required for create).

      :literal:`system\_id` (string) \- System identifier for the device (required for create).

      For :literal:`create\_agent` state, the following fields are used.

      :literal:`management\_ip` (string) \- Device management IP (required).

      :literal:`username` (string) \- SSH username for device (required).

      :literal:`password` (string) \- SSH password for device (required).

      :literal:`agent\_type` (string) \- Agent type, default :literal:`offbox`.

      :literal:`job\_on\_create` (string) \- Job to run on create, default :literal:`install`.

      :literal:`platform` (string) \- Device platform, default :literal:`junos`.

      For :literal:`update\_status` state, the following fields are used.

      :literal:`ip` (string) \- Device IP address (required).

      :literal:`system\_id` (string) \- Device system ID.

      :literal:`platform` (string) \- Device platform.

      :literal:`task` (string) \- Task name. :literal:`Device Ready` marks completed.

      :literal:`log` (string) \- Log message.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id"></div>

      .. _ansible_collections.juniper.apstra.ztp_device_module__parameter-id:

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

      Dictionary containing the ZTP device identifier.

      :literal:`ip\_addr` is the management IP address of the device.

      :literal:`system\_id` is the system identifier of the device.

      For :literal:`status`\ , either :literal:`ip\_addr` or :literal:`system\_id` must be provided.

      For :literal:`absent`\ , :literal:`ip\_addr` is required.

      For create, :literal:`ip\_addr` can be provided in the :literal:`body` instead.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.juniper.apstra.ztp_device_module__parameter-password:

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

      .. _ansible_collections.juniper.apstra.ztp_device_module__parameter-state:

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

      Desired state of the ZTP device.

      :literal:`present` will create the device (or update via delete+recreate).

      :literal:`absent` will delete the device.

      :literal:`status` will retrieve the ZTP status of the device (requires :literal:`ip\_addr` or :literal:`system\_id` in :literal:`id`\ ).

      :literal:`create\_agent` will create a system agent via the ZTP VM's :literal:`/api/ztp/create\_agent` endpoint. Requires ZTP VM connection parameters and device credentials in :literal:`body`.

      :literal:`update\_status` will update device status via the ZTP VM's :literal:`/api/ztp/device/log` endpoint. Requires ZTP VM connection parameters and status fields in :literal:`body`.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"absent"`
      - :ansible-option-choices-entry:`"status"`
      - :ansible-option-choices-entry:`"create\_agent"`
      - :ansible-option-choices-entry:`"update\_status"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.juniper.apstra.ztp_device_module__parameter-username:

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

      .. _ansible_collections.juniper.apstra.ztp_device_module__parameter-verify_certificates:

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

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ztp_auth_token"></div>

      .. _ansible_collections.juniper.apstra.ztp_device_module__parameter-ztp_auth_token:

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

      .. _ansible_collections.juniper.apstra.ztp_device_module__parameter-ztp_password:

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

      .. _ansible_collections.juniper.apstra.ztp_device_module__parameter-ztp_url:

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

      .. _ansible_collections.juniper.apstra.ztp_device_module__parameter-ztp_username:

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

      .. _ansible_collections.juniper.apstra.ztp_device_module__parameter-ztp_verify_certificates:

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

    # Check ZTP device status by IP address
    # Fails with an error if the IP address is not registered
    - name: Get ZTP device status by IP
      juniper.apstra.ztp_device:
        id:
          ip_addr: "192.168.50.10"
        state: status
      register: ztp_status

    - name: Show provisioning status (e.g. completed / unknown / in_progress)
      ansible.builtin.debug:
        msg: "ZTP status is {{ ztp_status.status }}"

    # Create agent via ZTP VM (handles both ZTP tracking and Apstra agent creation)
    - name: Create system agent via ZTP VM
      juniper.apstra.ztp_device:
        state: create_agent
        body:
          management_ip: "{{ device_mgmt_ip }}"
          username: "{{ device_username }}"
          password: "{{ device_password }}"
          agent_type: offbox
          job_on_create: install
          platform: junos
      register: agent_result

    # Update ZTP device status to completed
    - name: Mark device as completed in ZTP
      juniper.apstra.ztp_device:
        state: update_status
        body:
          ip: "{{ device_mgmt_ip }}"
          system_id: "{{ device_system_id }}"
          platform: junos
          task: "Device Ready"
          log: "Agent installed and connected successfully"



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
        <div class="ansibleOptionAnchor" id="return-agent_id"></div>

      .. _ansible_collections.juniper.apstra.ztp_device_module__return-agent_id:

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

      The Apstra system agent UUID returned by create\_agent.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state is create\_agent

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"acc45b14\-2ae0\-4c35\-8cd5\-2cb0228c7ad6"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-changed"></div>

      .. _ansible_collections.juniper.apstra.ztp_device_module__return-changed:

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

      .. _ansible_collections.juniper.apstra.ztp_device_module__return-changes:

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

      Dictionary of fields that were updated (present only on update).


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state is present and an update was applied


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-id"></div>

      .. _ansible_collections.juniper.apstra.ztp_device_module__return-id:

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

      The identifier of the ZTP device (ip\_addr).


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always when a device is targeted

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"ip\_addr": "192.168.50.10"}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.juniper.apstra.ztp_device_module__return-msg:

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


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-response"></div>

      .. _ansible_collections.juniper.apstra.ztp_device_module__return-response:

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

      Raw response from the API on create or update.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state is present and changes are made


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-status"></div>

      .. _ansible_collections.juniper.apstra.ztp_device_module__return-status:

      .. rst-class:: ansible-option-title

      **status**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-status" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The ZTP provisioning status string of the device. One of :literal:`completed`\ , :literal:`unknown`\ , or :literal:`in\_progress`. Module fails if the device is not found.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state is status

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"completed"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-ztp_device"></div>

      .. _ansible_collections.juniper.apstra.ztp_device_module__return-ztp_device:

      .. rst-class:: ansible-option-title

      **ztp_device**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-ztp_device" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Full ZTP device details retrieved from the status endpoint.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on create, update, or status check

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"ip\_addr": "192.168.50.10", "last\_log": "Device is ready to be used", "last\_updated\_at": "2026\-01\-01T00:00:00.000000Z", "status": "completed", "system\_id": "device\-001", "task": "Device Ready"}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-ztp_devices"></div>

      .. _ansible_collections.juniper.apstra.ztp_device_module__return-ztp_devices:

      .. rst-class:: ansible-option-title

      **ztp_devices**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-ztp_devices" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of all registered ZTP devices.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when state is present with no id and no body

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`[{"ip\_addr": "192.168.50.10", "last\_log": "Device is ready to be used", "last\_updated\_at": "2026\-01\-01T00:00:00.000000Z", "status": "completed", "system\_id": "device\-001", "task": "Device Ready"}]`


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

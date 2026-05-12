.. _plugins_in_juniper.apstra:

Juniper.Apstra
==============

Collection version 1.0.6

.. contents::
   :local:
   :depth: 1

Description
-----------

This collection provides modules to interact with Apstra.

**Authors:**

* Pratik Dave <pratikd@juniper.net>
* Edwin Jacques <ejacques@juniper.net>

**Supported ansible-core versions:**

* 2.16.0 or newer

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




.. toctree::
    :maxdepth: 1

.. _plugin_index_for_juniper.apstra:

Plugin Index
------------

These are the plugins in the juniper.apstra collection:

.. _module_plugins_in_juniper.apstra:

Modules
~~~~~~~

* :ansplugin:`apstra_facts module <juniper.apstra.apstra_facts#module>` -- Gather facts from Apstra AOS
* :ansplugin:`authenticate module <juniper.apstra.authenticate#module>` -- Apstra authentication
* :ansplugin:`blueprint module <juniper.apstra.blueprint#module>` -- Manage Apstra blueprints
* :ansplugin:`cabling_map module <juniper.apstra.cabling_map#module>` -- Manage and inspect the cabling map in an Apstra blueprint
* :ansplugin:`configlets module <juniper.apstra.configlets#module>` -- Manage configlets in Apstra
* :ansplugin:`connectivity_template module <juniper.apstra.connectivity_template#module>` -- Manage Connectivity Templates in Apstra blueprints
* :ansplugin:`connectivity_template_assignment module <juniper.apstra.connectivity_template_assignment#module>` -- Assign or unassign Connectivity Templates to application points
* :ansplugin:`design module <juniper.apstra.design#module>` -- Manage Apstra design elements (logical devices, rack types, templates)
* :ansplugin:`endpoint_policy module <juniper.apstra.endpoint_policy#module>` -- Manage endpoint policies in Apstra
* :ansplugin:`external_gateway module <juniper.apstra.external_gateway#module>` -- Manage external (remote) EVPN gateways in Apstra blueprints
* :ansplugin:`fabric_settings module <juniper.apstra.fabric_settings#module>` -- Manage fabric settings in an Apstra blueprint
* :ansplugin:`floating_ip module <juniper.apstra.floating_ip#module>` -- Manage Floating IPs in an Apstra blueprint
* :ansplugin:`generic_systems module <juniper.apstra.generic_systems#module>` -- Manage datacenter generic systems in Apstra blueprints
* :ansplugin:`iba_probes module <juniper.apstra.iba_probes#module>` -- Manage IBA (Intent\-Based Analytics) probes in Apstra
* :ansplugin:`interconnect_gateway module <juniper.apstra.interconnect_gateway#module>` -- Manage EVPN Interconnect Domains and their Gateways in Apstra blueprints
* :ansplugin:`interface_map module <juniper.apstra.interface_map#module>` -- Manage interface map assignments in an Apstra blueprint
* :ansplugin:`os_upgrade module <juniper.apstra.os_upgrade#module>` -- Manage device OS upgrades in an Apstra blueprint
* :ansplugin:`property_set module <juniper.apstra.property_set#module>` -- Manage property sets in Apstra
* :ansplugin:`resource_group module <juniper.apstra.resource_group#module>` -- Manage resource groups in Apstra
* :ansplugin:`resource_pools module <juniper.apstra.resource_pools#module>` -- Manage resource pools in Apstra
* :ansplugin:`rollback module <juniper.apstra.rollback#module>` -- Manage blueprint rollback and revisions in Apstra
* :ansplugin:`routing_policy module <juniper.apstra.routing_policy#module>` -- Manage routing policies in Apstra
* :ansplugin:`security_zone module <juniper.apstra.security_zone#module>` -- Manage security zones in Apstra
* :ansplugin:`system_agents module <juniper.apstra.system_agents#module>` -- Manage system agents (device onboarding) in Apstra
* :ansplugin:`tag module <juniper.apstra.tag#module>` -- Manage tags in Apstra
* :ansplugin:`upgrade_group module <juniper.apstra.upgrade_group#module>` -- Manage Apstra OS upgrade groups
* :ansplugin:`virtual_infra_manager module <juniper.apstra.virtual_infra_manager#module>` -- Manage Virtual Infrastructure Managers in Apstra
* :ansplugin:`virtual_network module <juniper.apstra.virtual_network#module>` -- Manage virtual networks in Apstra
* :ansplugin:`ztp_device module <juniper.apstra.ztp_device#module>` -- Manage ZTP (Zero Touch Provisioning) devices in Apstra

.. toctree::
    :maxdepth: 1
    :hidden:

    apstra_facts_module
    authenticate_module
    blueprint_module
    cabling_map_module
    configlets_module
    connectivity_template_module
    connectivity_template_assignment_module
    design_module
    endpoint_policy_module
    external_gateway_module
    fabric_settings_module
    floating_ip_module
    generic_systems_module
    iba_probes_module
    interconnect_gateway_module
    interface_map_module
    os_upgrade_module
    property_set_module
    resource_group_module
    resource_pools_module
    rollback_module
    routing_policy_module
    security_zone_module
    system_agents_module
    tag_module
    upgrade_group_module
    virtual_infra_manager_module
    virtual_network_module
    ztp_device_module

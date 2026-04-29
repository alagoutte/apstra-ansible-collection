# Copyright (c) 2024, Juniper Networks
# BSD 3-Clause License

"""Blueprint cabling-map LLDP utilities.

Provides reusable helpers for fetching LLDP node data from the
cabling-map endpoint.  The SDK's ``cabling_map.lldp.get()`` only
returns ``response['links']``, discarding the ``nodes`` dict.
This module uses ``raw_request`` to retrieve the full LLDP response
and extract the ``nodes`` portion — following the same pattern as
``bp_configlets.py``.

API endpoint::

    GET /api/blueprints/{bp_id}/cabling-map/lldp  → { nodes: {}, links: [] }

Usage inside a module::

    from ansible_collections.juniper.apstra.plugins.module_utils.apstra.bp_cabling_map import (
        get_lldp_nodes,
    )

    nodes = get_lldp_nodes(client_factory, bp_id)
    nodes = get_lldp_nodes(client_factory, bp_id, system_id="0C009B3C6D00")
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


def get_lldp_nodes(client_factory, blueprint_id, system_id=None):
    """Fetch per-system LLDP node data from the cabling-map endpoint.

    The SDK's ``cabling_map.lldp.get()`` extracts only
    ``response['links']``, so the ``nodes`` dict is lost.  This
    helper calls the REST API directly via ``raw_request`` to
    retrieve the ``nodes`` portion.

    Args:
        client_factory: An ``ApstraClientFactory`` instance.
        blueprint_id: The blueprint UUID.
        system_id: Optional system ID (MAC) to filter results.

    Returns:
        dict: The ``nodes`` dict from the LLDP response, keyed by
        node ID.  Returns empty dict on error or when no LLDP node
        data exists.
    """
    base = client_factory.get_base_client()
    url = f"/blueprints/{blueprint_id}/cabling-map/lldp"
    params = {"system_id": system_id} if system_id else {}
    resp = base.raw_request(url, params=params)
    if resp.status_code == 200:
        data = resp.json()
        return data.get("nodes", {})
    return {}

# -*- coding: utf-8 -*-

# Copyright (c) 2024, Juniper Networks
# Apache License, Version 2.0 (see https://www.apache.org/licenses/LICENSE-2.0)

class ModuleDocFragment:
    DOCUMENTATION = r'''
options:

  ztp_url:
    description:
      - Base URL of the ZTP VM (e.g., C(https://10.204.22.128)).
      - Required because the ZTP VM is typically a separate appliance
        from the Apstra server.
      - Can also be set via the C(ZTP_URL) environment variable.
    type: str
    required: false

  ztp_username:
    description:
      - Username for ZTP VM authentication.
      - Can also be set via the C(ZTP_USERNAME) environment variable.
    type: str
    required: false

  ztp_password:
    description:
      - Password for ZTP VM authentication.
      - Can also be set via the C(ZTP_PASSWORD) environment variable.
    type: str
    required: false

  ztp_auth_token:
    description:
      - Pre-existing auth token for the ZTP VM.
      - Can also be set via the C(ZTP_AUTH_TOKEN) environment variable.
    type: str
    required: false

  ztp_verify_certificates:
    description:
      - Whether to verify SSL certificates when connecting to the ZTP VM.
    type: bool
    required: false
    default: true
'''

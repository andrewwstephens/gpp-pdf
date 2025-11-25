#!/usr/bin/env python3
import os
__version__ = '2025-Jun-12'

GPP_VER = os.environ.get('GPP_VER')
if GPP_VER not in ['DEV', 'STG', 'PRD']:
    raise SystemExit('Error: the GPP_VER environment variable must be DEV, STG, or PRD.')

GPP_KEY = os.environ.get('GPP_KEY')
if GPP_KEY is None:
    raise SystemExit('Error: the GPP_KEY environment variable must be defined with an API key.')

if GPP_VER == 'DEV':  # Development
    ATT_URL = 'https://lucuma-postgres-odb-dev.herokuapp.com/attachment'
    ITC_URL = 'https://itc-dev.lucuma.xyz/itc'
    ODB_URL = 'https://lucuma-postgres-odb-dev.herokuapp.com/odb'
    WSS_URL = 'wss://lucuma-postgres-odb-dev.herokuapp.com/ws'
elif GPP_VER == 'STG':  # Staging
    ATT_URL = 'https://lucuma-postgres-odb-staging.herokuapp.com/attachment'
    ITC_URL = 'https://itc-staging.lucuma.xyz/itc'
    ODB_URL = 'https://lucuma-postgres-odb-staging.herokuapp.com/odb'
    WSS_URL = 'wss://lucuma-postgres-odb-staging.herokuapp.com/ws'
elif GPP_VER == 'PRD':  # Production
    ATT_URL = 'https://lucuma-postgres-odb-production.herokuapp.com/attachment'
    ITC_URL = 'https://itc-production.lucuma.xyz/itc'
    ODB_URL = 'https://lucuma-postgres-odb-production.herokuapp.com/odb'
    WSS_URL = 'wss://lucuma-postgres-odb-production.herokuapp.com/ws'

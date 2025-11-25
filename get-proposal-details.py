#!/usr/bin/env python3
import argparse
import json
import requests
import sys
from gpp import GPP_KEY, ODB_URL
__version__ = '2025-Sep-16'


def main(args):
    headers = {'Authorization': f'Bearer {GPP_KEY}'}
    variables = {'proposalReference': args.proposal}
    r = requests.post(ODB_URL, json={'query': QUERY, 'variables': variables}, headers=headers)
    if r.status_code == 200:
        print(json.dumps(r.json(), indent=2))
    else:
        raise Exception(f"Query failed: {r.status_code}.")


QUERY = """
query variable_types($proposalReference: String!) {
    program(proposalReference: $proposalReference) {
        name
        description
        type
        active {
            start
            end
        }
        pi { ...ProgramUser }
        users { ...ProgramUser }
        goa {
            proprietaryMonths
            shouldNotify
            privateHeader
        }
    }
}
fragment ProgramUser on ProgramUser {
    displayName
    email
    user { orcidId }
}
"""


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description='Query GPP for proposal details.',
        epilog='examples:\n' +
               '  get-proposal-details.py G-2026A-0001   # DEV \n' +
               '  get-proposal-details.py G-2026A-0001   # STG \n' +
               '  get-proposal-details.py G-2025B-0430   # PRD \n' +
               '\nversion:\n  ' + __version__)
    parser.add_argument('proposal', action='store', type=str)
    main(parser.parse_args(None if sys.argv[1:] else ['--help']))

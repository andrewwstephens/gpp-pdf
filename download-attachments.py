#!/usr/bin/env python3
import argparse
import logging
import re
import requests
import sys
from pyexplore import GPP_KEY, ATT_URL
__version__ = '2025-Nov-24'


def main(args):
    logging.basicConfig(format='%(asctime)s %(name)-15s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S', level=getattr(logging, args.loglevel.upper()))
    logger = logging.getLogger('main')

    for attachment_id in args.ids:
        logger.debug('Downloading %s', attachment_id)
        validate(attachment_id, 'attachment')
        url = ATT_URL + '/' + attachment_id
        logger.debug('URL %s', url)
        response = requests.get(url, headers={'Authorization': 'bearer ' + GPP_KEY})
        if response.status_code == 200:
            filename = get_filename(attachment_id)
            with open(filename, 'wb') as f:
                f.write(response.content)
                print('File downloaded and saved as', filename)
        else:
            print('Failed to download the attachment: ', response.status_code)


def get_filename(attachment_id):
        """Get the attachment file name."""
        logger = logging.getLogger('get_filename')
        url = ATT_URL + '/url/' + attachment_id
        logger.debug('URL %s', url)
        response = requests.get(url, headers={'Authorization': 'bearer ' + GPP_KEY})
        logger.debug('Response.text %s', response.text)
        # logger.debug('Response.headers %s', response.headers)
        # Response.text will look something like this:
        # https://s3.amazonaws.com/cloud-cube-us2/xyzynd4dwgta/p-d55/7b3a80ea-2d74-46a8-a15b-3d6a56a86b76/G504_optical_test13.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250909T195811Z&X-Amz-SignedHeaders=host&X-Amz-Credential=AKIA37SVVXBHWCA2CWPS%2F20250909%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Expires=7200&X-Amz-Signature=6bb8993944d9c0605d8fa10b041c39a15f448a23e1b964cbb71a92681982f2a6
        original_filename = re.split(r'[/?]', response.text)[7]
        logger.debug('original_filename: %s', original_filename)
        return original_filename


def validate(identifier: str, kind: str):
    """
    Check that the supplied ID has a valid format.
    kind = {attachment, observation, program, status, target}
    """
    if kind == 'status':
        if identifier not in ['ACTIVE', 'INACTIVE']:
            raise SystemExit(f'{identifier} is not a valid status')
    elif kind in ['attachment', 'cfp', 'dataset', 'observation', 'program', 'target', 'user']:
        if not re.match(f'{kind[0]}-(0|[1-9a-f][0-9a-f]*)', identifier):
            raise SystemExit(f'{identifier} is not a valid {kind} ID')
    else:
        raise SystemExit('Unknown kind')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description='Get attachments associated with a program.',
        epilog='examples:\n' +
        '  download-attachments.py a-2a4\n' +
        '\nversion:\n  ' + __version__)
    parser.add_argument('ids', action='store', nargs='+', metavar='ATTACHMENT_ID')
    parser.add_argument('--loglevel', type=str, default='info', metavar='LEVEL',
                        choices=['debug', 'info', 'warning', 'error'],
                        help='set the log level (debug, [info], warning, error)')
    main(parser.parse_args(None if sys.argv[1:] else ['--help']))

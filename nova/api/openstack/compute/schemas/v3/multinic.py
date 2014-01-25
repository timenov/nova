#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

add_fixed_ip = {
    'type': 'object',
    'properties': {
        'add_fixed_ip': {
            'type': 'object',
            'properties': {
                # The maxLength is from the column 'uuid' of the
                # table 'networks'
                'network_id': {
                    'type': ['string', 'number'],
                    'minLength': 1, 'maxLength': 36,
                },
            },
            'required': ['network_id'],
            'additionalProperties': False,
        },
    },
    'required': ['add_fixed_ip'],
    'additionalProperties': False,
}


remove_fixed_ip = {
    'type': 'object',
    'properties': {
        'remove_fixed_ip': {
            'type': 'object',
            'properties': {
                'address': {
                    'type': 'string',
                    'oneOf': [
                        {'format': 'ipv4'},
                        {'format': 'ipv6'}
                    ],
                },
            },
            'required': ['address'],
            'additionalProperties': False,
        },
    },
    'required': ['remove_fixed_ip'],
    'additionalProperties': False,
}

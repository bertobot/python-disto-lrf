#!/usr/bin/env python3

import asyncio
import struct
from bleak import BleakClient


RANGE = 0.0
characteristic_read_range = '3ab10101-f831-4395-b29d-570977d5bf94'


def notification_read_range(sender, data):
    RANGE = struct.unpack('f', data)[0]
    print(f'range: {RANGE}')


async def main(address):
    async with BleakClient(address) as client:
        await client.start_notify(characteristic_read_range, notification_read_range)
        await asyncio.sleep(10)

def init(address):
    asyncio.run(main(address))


if __name__ == '__main__':
    init('E9:8C:FF:A6:DC:60')

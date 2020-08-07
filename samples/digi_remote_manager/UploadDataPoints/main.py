# Copyright 2020, Digi International Inc.
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from digidevice import datapoint
import random
import time

TEMPERATURE_FILE = "/sys/class/thermal/thermal_zone0/temp"
DATA_STREAM_TEMP = "deviceTemperature"
INTERVAL_S = 10


def main():
    print(" +---------------------------+")
    print(" | Upload Data Points Sample |")
    print(" +---------------------------+\n")

    while True:
        try:
            # Get the internal temperature of the device.
            temp_value = get_internal_temp()

            # Notify about the Data Point upload.
            print("- Uploading '%2.3f' to stream '%s'" % (temp_value,
                                                          DATA_STREAM_TEMP))

            # Upload the temperature to Digi Remote Manager.
            datapoint.upload(DATA_STREAM_TEMP, temp_value, units="C",
                             data_type=datapoint.DataType.DOUBLE)

            # Sleep until the next upload.
            time.sleep(INTERVAL_S)
        except Exception as e:
            print(e)


def get_internal_temp():
    """
    Reads and returns the internal temperature parameter of the device.

    Returns:
        Float: the internal temperature of the Digi device or an emulated one
            if it could not be read.
    """
    try:
        with open(TEMPERATURE_FILE) as f:
            return float(f.readline()) / 1000
    except Exception:
        return float(random.randint(40000, 45000)) / 1000


if __name__ == "__main__":
    main()

import machine

class MPUSimple():
    def __init__(self, i2c, address=0x69):
        self._i2c = i2c
        self._addr = address
        self._i2c.start()
        self._i2c.writeto(self._addr, bytearray([107, 0]))
        self._i2c.stop()

    def _get_raw_values(self):
        self._i2c.start()
        raw_data = self._i2c.readfrom_mem(self._addr, 0x3B, 14)
        self._i2c.stop()
        return raw_data

    def _bytes2Int(self, firstbyte, secondbyte):
        if not firstbyte & 0x80:
            return firstbyte << 8 | secondbyte
        return - (((firstbyte ^ 255) << 8) | (secondbyte ^ 255) + 1)

    def getSensors(self):
        raw_data = self._get_raw_values()
        vals = {}
        vals["AcX"] = self._bytes2Int(raw_data[0], raw_data[1])
        vals["AcY"] = self._bytes2Int(raw_data[2], raw_data[3])
        vals["AcZ"] = self._bytes2Int(raw_data[4], raw_data[5])
        vals["Tmp"] = self._bytes2Int(raw_data[6], raw_data[7]) / 340.00 + 36.53
        vals["GyX"] = self._bytes2Int(raw_data[8], raw_data[9])
        vals["GyY"] = self._bytes2Int(raw_data[10], raw_data[11])
        vals["GyZ"] = self._bytes2Int(raw_data[12], raw_data[13])
        return vals # returned in range of Int16


class GPSParser:
    
    @staticmethod
    def convert_dms_to_dd(dms, ref):

        try:
            degrees = float(dms[0])
            minutes = float(dms[1])
            seconds = float(dms[2])
            
            dd = degrees + (minutes / 60.0) + (seconds / 3600.0)
            
            if ref in ['S', 'W']:
                dd *= -1
            
            return dd
        except (TypeError, ValueError, IndexError):
            return None
    
    @staticmethod
    def parse(gps_data, gps_tags):

        gps_info = {}
        
        for tag, value in gps_data.items():
            decoded = gps_tags.get(tag, tag)
            gps_info[decoded] = value
        
        lat = None
        lon = None
        
        if 'GPSLatitude' in gps_info and 'GPSLatitudeRef' in gps_info:
            lat = GPSParser.convert_dms_to_dd(
                gps_info['GPSLatitude'],
                gps_info['GPSLatitudeRef']
            )
        
        if 'GPSLongitude' in gps_info and 'GPSLongitudeRef' in gps_info:
            lon = GPSParser.convert_dms_to_dd(
                gps_info['GPSLongitude'],
                gps_info['GPSLongitudeRef']
            )
        
        return gps_info, lat, lon
    
    @staticmethod
    def get_maps_link(lat, lon):

        if lat is not None and lon is not None:
            return f"https://www.google.com/maps?q={lat},{lon}"
        return None

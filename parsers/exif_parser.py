class ExifParser:    
    CAMERA_TAGS = ['Make', 'Model', 'LensMake', 'LensModel', 'Software']
    
    SETTINGS_TAGS = [
        'DateTime', 'DateTimeOriginal', 'DateTimeDigitized',
        'ExposureTime', 'FNumber', 'ISO', 'ISOSpeedRatings',
        'FocalLength', 'Flash', 'WhiteBalance', 'ExposureMode',
        'MeteringMode', 'ExposureProgram'
    ]
    
    @staticmethod
    def categorize_tags(exif_dict):
        camera_info = {}
        settings_info = {}
        other_tags = {}
        
        for key, value in exif_dict.items():
            if key in ExifParser.CAMERA_TAGS:
                camera_info[key] = value
            elif key in ExifParser.SETTINGS_TAGS:
                settings_info[key] = value
            else:
                other_tags[key] = value
        
        return camera_info, settings_info, other_tags
    
    @staticmethod
    def format_value(key, value):
        if key == 'ExposureTime' and isinstance(value, tuple) and len(value) == 2:
            return f"{value[0]}/{value[1]} sec"
        
        if key == 'FNumber' and isinstance(value, tuple) and len(value) == 2:
            if value[1] != 0:
                return f"f/{value[0]/value[1]:.1f}"
        
        if key == 'FocalLength' and isinstance(value, tuple) and len(value) == 2:
            if value[1] != 0:
                return f"{value[0]/value[1]:.1f} mm"
        
        if isinstance(value, bytes):
            try:
                return value.decode('utf-8', errors='ignore')
            except:
                return f"<binary data: {len(value)} bytes>"
        
        if isinstance(value, (tuple, list, dict)):
            value_str = str(value)
            if len(value_str) > 100:
                return value_str[:97] + "..."
            return value_str
        
        value_str = str(value)
        if len(value_str) > 100:
            return value_str[:97] + "..."
        
        return value_str

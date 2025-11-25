from PyPDF2 import PdfReader
from pathlib import Path

from utils import format_file_size, format_pdf_date


class PDFExtractor:
    
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.reader = None
    
    def extract(self):
        try:
            self.reader = PdfReader(self.file_path)
            
            metadata = {
                'basic_info': self._get_basic_info(),
                'pdf_metadata': self._get_pdf_metadata()
            }
            
            return metadata
            
        except Exception as e:
            raise Exception(f"Error extracting PDF metadata: {e}")
    
    def _get_basic_info(self):
        return {
            'file_name': self.file_path.name,
            'file_size': format_file_size(self.file_path.stat().st_size),
            'num_pages': len(self.reader.pages)
        }
    
    def _get_pdf_metadata(self):
        pdf_meta = self.reader.metadata
        
        if not pdf_meta:
            return {}
        
        common_fields = {
            '/Title': 'Title',
            '/Author': 'Author',
            '/Subject': 'Subject',
            '/Creator': 'Creator',
            '/Producer': 'Producer',
            '/CreationDate': 'Creation Date',
            '/ModDate': 'Modification Date',
            '/Keywords': 'Keywords'
        }
        
        metadata = {}
        
        for key, label in common_fields.items():
            if key in pdf_meta:
                value = pdf_meta[key]
                
                if 'Date' in label:
                    value = format_pdf_date(value)
                
                metadata[label] = value
        
        for key, value in pdf_meta.items():
            if key not in common_fields:
                metadata[key] = str(value)
        
        return metadata

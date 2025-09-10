#!/usr/bin/env python3
"""
Simple Markdown to DOCX converter
Converts the Handglove requirements document from MD to DOCX format
"""

import re
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
import os

def create_docx_from_text(text_content, output_path):
    """Create a basic DOCX file from text content."""
    
    # Create the basic DOCX structure
    document_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
    <w:body>
        {content}
    </w:body>
</w:document>'''
    
    # Convert markdown-style content to Word paragraphs
    paragraphs = []
    lines = text_content.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:  # Empty line
            continue
            
        # Handle headers
        if line.startswith('# '):
            title = line[2:].strip()
            paragraphs.append(f'''<w:p>
                <w:pPr><w:pStyle w:val="Heading1"/></w:pPr>
                <w:r><w:t>{title}</w:t></w:r>
            </w:p>''')
        elif line.startswith('## '):
            title = line[3:].strip()
            paragraphs.append(f'''<w:p>
                <w:pPr><w:pStyle w:val="Heading2"/></w:pPr>
                <w:r><w:t>{title}</w:t></w:r>
            </w:p>''')
        elif line.startswith('### '):
            title = line[4:].strip()
            paragraphs.append(f'''<w:p>
                <w:pPr><w:pStyle w:val="Heading3"/></w:pPr>
                <w:r><w:t>{title}</w:t></w:r>
            </w:p>''')
        elif line.startswith('- '):
            # Bullet point
            content = line[2:].strip()
            content = re.sub(r'\*\*(.*?)\*\*', r'\1', content)  # Remove markdown bold
            paragraphs.append(f'''<w:p>
                <w:pPr>
                    <w:numPr>
                        <w:ilvl w:val="0"/>
                        <w:numId w:val="1"/>
                    </w:numPr>
                </w:pPr>
                <w:r><w:t>{content}</w:t></w:r>
            </w:p>''')
        elif line.startswith('```'):
            # Skip code block markers
            continue
        elif line == '---':
            # Skip horizontal rules
            continue
        else:
            # Regular paragraph
            if line:
                # Remove markdown formatting
                content = re.sub(r'\*\*(.*?)\*\*', r'\1', line)  # Bold
                content = re.sub(r'\*(.*?)\*', r'\1', content)   # Italic
                content = re.sub(r'`(.*?)`', r'\1', content)     # Code
                
                paragraphs.append(f'''<w:p>
                    <w:r><w:t>{content}</w:t></w:r>
                </w:p>''')
    
    # Combine all paragraphs
    content = '\n'.join(paragraphs)
    document_content = document_xml.format(content=content)
    
    # Create the DOCX file structure
    create_docx_zip(document_content, output_path)

def create_docx_zip(document_content, output_path):
    """Create the DOCX zip file with required structure."""
    
    # Content Types
    content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
    <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
    <Default Extension="xml" ContentType="application/xml"/>
    <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>'''
    
    # Main relationships
    main_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
    <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>'''
    
    # Document relationships
    doc_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
</Relationships>'''
    
    # Create the DOCX file
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as docx:
        docx.writestr('[Content_Types].xml', content_types)
        docx.writestr('_rels/.rels', main_rels)
        docx.writestr('word/document.xml', document_content)
        docx.writestr('word/_rels/document.xml.rels', doc_rels)

def main():
    # Read the markdown file
    md_file = Path("D:/DEV/Handglove/docs/HANDGLOVE_PAYROLL_SYSTEM_REQUIREMENTS.md")
    output_file = Path("D:/DEV/Handglove/docs/HANDGLOVE_PAYROLL_SYSTEM_REQUIREMENTS.docx")
    
    if not md_file.exists():
        print(f"Error: Markdown file not found: {md_file}")
        return
    
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("Converting markdown to DOCX...")
        create_docx_from_text(content, output_file)
        print(f"Successfully created: {output_file}")
        
    except Exception as e:
        print(f"Error converting file: {e}")

if __name__ == "__main__":
    main()

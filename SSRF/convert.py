from docx import Document
import os

def extract_images_from_docx(docx_path, output_folder):
    doc = Document(docx_path)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, rel in enumerate(doc.part.rels.values()):
        if "image" in rel.reltype:
            image_data = rel.target_part.blob
            ext = rel.target_part.content_type.split("/")[-1]
            with open(f"{output_folder}/image_{i}.{ext}", "wb") as img_file:
                img_file.write(image_data)
    
    print(f"Đã trích xuất ảnh vào thư mục: {output_folder}")

# Sử dụng
extract_images_from_docx("SSRF.docx", "image")

import os, shutil
import json

def gen():
    doc_folder = os.path.join(__file__, "../../docs")
    path_to_levels = os.path.join(doc_folder, 'english_new_concept/levels')
    level_folders = os.listdir(path_to_levels)
    html = ""

    col = {}

    for level_folder in level_folders:
        full_level_folder = os.path.join(path_to_levels, level_folder)
        files = os.listdir(full_level_folder)
        for file in files:
            dot = file.rindex('.')
            prefix = file[0:dot]
            rel_path = file # os.path.relpath(os.path.join(full_level_folder, file), path_to_levels)
            col[prefix] = rel_path

        str_rep = json.dumps(col, indent = 2)

        data_file = os.path.join(path_to_levels, level_folder, "data.js")
        with open(data_file, 'w') as fp:
            fp.write("// *AUTO* generated, please do not modify manually !!!\r\n")
            fp.write(f"var data={str_rep};")

        shutil.copyfile(os.path.join(doc_folder, 'template.html'), os.path.join(path_to_levels, level_folder, "index.html"))

gen()
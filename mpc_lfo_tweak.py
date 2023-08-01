import os
import sys
import xml.etree.ElementTree as ET
import shutil

LFO_ELEMENTS = ["LfoPitch", "LfoCutoff", "LfoVolume", "LfoPan"]


def update_elements(element):
    updated = False
    if element.tag in LFO_ELEMENTS:
        element.text = '0'
        updated = True
    for child in element:
        if update_elements(child):
            updated = True
    return updated


def clean_xpm_files(directory_path):

    for root, _, files in os.walk(directory_path):
        for filename in files:
            if filename.endswith(".xpm"):
                xml_file_path = os.path.join(root, filename)

                # Check if the XML file has already been backed up
                backup_file_path = xml_file_path + ".backup"
                if os.path.exists(backup_file_path):
                    print(filename, " - Skipped, was fixed previously.")
                    continue

                # Parse the XML file
                tree = ET.parse(xml_file_path)
                root_element = tree.getroot()

                # Check if the XML structure was changed
                is_updated = update_elements(root_element)
                if is_updated:
                    print(filename, " - Has been fixed.")
                    # Create a backup of the original file if it doesn't exist
                    shutil.copy(xml_file_path, backup_file_path)

                    # Save the updated XML file, overwriting the original one
                    tree.write(xml_file_path)


def restore_xpm_files(directory_path):

    for root, _, files in os.walk(directory_path):
        for filename in files:
            if filename.endswith(".xpm.backup"):
                backup_file_path = os.path.join(root, filename)
                xml_file_path = backup_file_path[:-len(".backup")]

                # Delete the original XML file
                if os.path.exists(xml_file_path):
                    os.remove(xml_file_path)

                # Restore the backup file by renaming it to the original file name
                os.rename(backup_file_path, xml_file_path)
                print(filename, " - Has been restored.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mpc_lfo_tweak.py <directory_path> <mode>")
        sys.exit(1)

    directory_path = sys.argv[1]
    mode = ""
    if len(sys.argv) >= 3:
        mode = sys.argv[2]

    if mode not in ["CLEAN_LFOS", "RESTORE_LFOS"]:
        print("Invalid mode. Please choose 'CLEAN_LFOS' or 'RESTORE_LFOS'.")
        sys.exit(1)

    if mode == "CLEAN_LFOS":
        clean_xpm_files(directory_path)
    elif mode == "RESTORE_LFOS":
        restore_xpm_files(directory_path)

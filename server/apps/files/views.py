from flask import Blueprint, send_file
from zipfile import ZipFile
import os

base_path = "bucket/reports"

bp = Blueprint('files', __name__, url_prefix='/files')

@bp.route('/<report_id>', methods=['GET'])
def download_report(report_id):
    report = os.path.join(base_path, report_id)
    zip_name = os.path.join(report, f"Report-{report_id}.zip")
    
    files = os.listdir(report)
    
    try:
        with ZipFile(zip_name, mode="a") as archive:
            for file in files:
                archive.write(os.path.join(report, file))
        return send_file(zip_name)
    except Exception as error:
        return error, 500
    finally:
        os.remove(zip_name)
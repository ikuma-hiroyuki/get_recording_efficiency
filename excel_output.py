import os
from pathlib import Path
import openpyxl


class ExcelWriter:
    """動画撮影日、作業時間、完成動画時間、作業効率をExcelに出力するクラス"""
    FILE_PATH = 'video_create_efficiency.xlsx'

    def __init__(self, date, worktime, total_completed_video_duration, efficiency):
        self.date = date
        self.worktime = worktime
        self.total_completed_video_duration = total_completed_video_duration
        self.efficiency = efficiency

    def open_workbook(self):
        """エクセルを開く"""
        if os.name == "nt":
            # windows
            os.system(f"start {self.FILE_PATH}")
        elif os.name == "posix":
            # mac
            os.system(f"open {self.FILE_PATH}")

    def write_excel(self):
        if not Path(self.FILE_PATH).exists():
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = 'video_create_efficiency'
            ws.append(['動画撮影日', '作業時間(分)', '完成動画時間(分)', '作業効率'])
        else:
            wb = openpyxl.load_workbook(self.FILE_PATH)
            ws = wb.active

        ws.append([
            self.date,
            self.worktime,
            round(self.total_completed_video_duration, 2),
            round(self.efficiency, 2)
        ])
        wb.save(self.FILE_PATH)
        wb.close()

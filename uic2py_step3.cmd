@echo off
REM This script is used to convert .ui files to .py files using the pyside6-uic tool.
REM Make sure you have PySide6 installed and the pyside6-uic tool available in your PATH.
pyside6-uic Designer/navigation_panel.ui -o ui/widgets/navigation_panel_ui.py
pyside6-uic designer/main_window.ui -o ui/main_window_ui.py
pyside6-uic designer/step1_load_extract.ui -o ui/steps/step1_load_extract_ui.py
pyside6-uic designer/step2_normalize.ui -o ui/steps/step2_normalize_ui.py
pyside6-uic Designer/step3_write_output.ui -o ui/steps/step3_write_output_ui.py
echo Conversion complete: navigation_panel.ui has been converted to ui/widgetsnavigation_panel_ui.py
echo Conversion complete: main_window.ui has been converted to ui/main_window_ui.py
echo Conversion complete: step1_load_extract.ui has been converted to ui/steps/step1_load_extract_ui.py
echo Conversion complete: step2_normalize.ui has been converted to ui/steps/step2_normalize_ui.py
echo Conversion complete: step3_write_output.ui has been converted to ui/steps/step3_write_output_ui.py
pause

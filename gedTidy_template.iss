; ------------------------------------------------------------
; GedTidy – Installer Script (Template)
; ------------------------------------------------------------

[Setup]
AppName=GedTidy
AppVersion=@@VERSION@@
AppPublisher=Dieter
DefaultDirName={commonpf}\GedTidy
DefaultGroupName=GedTidy
DisableProgramGroupPage=yes
OutputDir=installer
OutputBaseFilename=GedTidy_Setup_@@VERSION@@
Compression=lzma
SolidCompression=yes
LicenseFile=LICENSE
ArchitecturesInstallIn64BitMode=x64compatible
WizardStyle=modern
SetupIconFile=assets\gedtidy.ico
UninstallDisplayIcon={app}\GedTidy.exe


[Files]
Source: "dist\GedTidy.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\GedTidy"; Filename: "{app}\GedTidy.exe"
Name: "{commondesktop}\GedTidy"; Filename: "{app}\GedTidy.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Desktop-Verknüpfung erstellen"; GroupDescription: "Zusätzliche Aufgaben"

[Run]
Filename: "{app}\GedTidy.exe"; Description: "GedTidy jetzt starten"; Flags: nowait postinstall skipifsilent
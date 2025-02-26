[Setup]
AppName=Registro de Atividades
AppVersion=1.0
DefaultDirName={pf}\RegistroAtividades
DefaultGroupName=Registro de Atividades
OutputDir=.
OutputBaseFilename=RegistroAtividadesSetup
SetupIconFile=icone.ico
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\script.exe"; DestDir: "{app}"

[Icons]
Name: "{group}\Registro de Atividades"; Filename: "{app}\script.exe"
Name: "{commondesktop}\Registro de Atividades"; Filename: "{app}\script.exe"

[Run]
Filename: "{app}\script.exe"; Description: "Executar Registro de Atividades"; Flags: nowait postinstall

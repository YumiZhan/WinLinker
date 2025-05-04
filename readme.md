# WinLinker

## Features

WinLinker provides user-friendly GUI on Microsoft Windows, allowing users to create hard/symbolic/junction links via the context menu of the File Explorer or the Desktop.

## Usage

1. Right-click the mouse on
   * a selected file
   * a selected folder
   * the background of the File Explorer or the Desktop
2. Select "Show more options" (only on the Windows 11)
3. Select "Create Link"
4. Select "Create Here"[^1] or "Link Here"[^2] (only if you have right-clicked the mouse on the background in step 1)
5. Edit path to the destination of the link (under the label "Destination")
6. Edit properties of the entrance of the link (under the label "Entrance")
   - Edit name of the link (under the label "Name")
   - Select the type of the link
     - hard[^3]
     - symbolic[^4]
     - junction[^5]
   - Edit path to the folder where the link is placed (under the label "Folder")
7. Click "Create" button

## Build

### Executable File

A python interpreter is required. To download and install a python interpreter, refer to [Downloading Python](https://wiki.python.org/moin/BeginnersGuide/Download#Windows).

Run the following command to install the relevant packages:

```cmd
pip install -r requirements.txt
```

Run the following command to generate the executable file:

```cmd
pyinstaller --workpath build/pyinstaller_workpath --distpath build --clean -y build/winlinker.spec
```

The executable file and the other relevant files will be placed in directory `build/WinLinker`.

### Installer

Run the following command to install WiX Toolset:

```cmd
winget install --id WiXToolset.WiXCLI -i
```

Run the following command to get ui extension for WiX Toolset:

```cmd
wix extension add WixToolset.UI.wixext
```

Run the following command to generate the machine-wide installer and per-user installer:

```cmd
wix build -arch x64 -bindpath "ToBeHarvested=../WinLinker" -d "LicensePath=build/installer/license.rtf" -ext WixToolset.UI.wixext build/installer/winlinker_machine.wxs -out build/installer/WinLinkerSetup_<version>.msi
wix build -arch x64 -bindpath "ToBeHarvested=../WinLinker" -d "LicensePath=build/installer/license.rtf" -ext WixToolset.UI.wixext build/installer/winlinker_user.wxs -out build/installer/WinLinkerUserSetup_<version>.msi
```

> Replace `<version>` with actual version, such as `v1.0.0`

The installer will be placed in directory `build/installer`.

## License Notice

WinLinker is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

WinLinker is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/).

[^1]: Create a link on the current folder by default

[^2]: Create a link to the current folder by default

[^3]: Create a hard link, available only if the destination of the link is a file

[^4]: Create a symbolic link

[^5]: Create a junction point, available only if the destination of the link is a folder

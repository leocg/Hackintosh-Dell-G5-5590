# Hackintosh Dell G5 5590 OpenCore Changelog



**JULY 20 2022** (v3.3)

- Updated to OpenCore 0.8.2 and corresponding kexts.
- Updated to macOS Monterey 12.5 using software updater without issues with OpenCore 0.8.2.
- Added **ResetNvramEntry.efi** allowing resetting NVRAM from OpenCore 0.8.2 boot picker
- Added **ToggleSipEntry.efi** allowing enabling/disabling System Integrity Protection (SIP) from OpenCore boot picker

**APRIL 04 2022** (v3.2)

- Updated to OpenCore 0.7.9 and corresponding kexts.
- Updated to macOS Monterey 12.3.1 from 12.1 using software updater without issues with OpenCore 0.7.9.

**DECEMBER 16 2021** (v3.1)

- Updated to OpenCore 0.7.6 and corresponding kexts (https://dortania.github.io/hackintosh/updates/2021/12/07/acidanthera-december.html).
- Updated to macOS Monterey 12.1 using software updater without issues with OpenCore 0.7.6.

**NOVEMBER 02 2021** (v3.0)

- Updated to OpenCore 0.7.5 and corresponding kexts (https://dortania.github.io/hackintosh/updates/2021/11/01/acidanthera-november.html).
- Supporting macOS Monterey without issues. You can use software updater from Big Sur to upgrade your machine using [latest EFI](https://github.com/leocg/Hackintosh-Dell-G5-5590/releases).

**OCTOBER 26 2021**

- Updated to macOS Monterey 12.0.1 using software update and latest EFI ([Dell G5 5590 OpenCore 0.7.4](https://github.com/leocg/Hackintosh-Dell-G5-5590/releases/tag/v2.11-OC-0.7.4)).

**OCTOBER 06 2021** (v2.11)

- Updated to OpenCore 0.7.4 and corresponding kexts (https://dortania.github.io/hackintosh/updates/2021/10/07/acidanthera-october.html).
- Updated HfsPlus.efi from OcBinaryData repository
- Remade USB mapping with [USBMap](https://github.com/corpnewt/USBMap)

**SEPTEMBER 23 2021**

- Updated guide with new information and screenshots.

**SEPTEMBER 22 2021** (v2.10)

- Updated to OpenCore 0.7.3 and corresponding kexts (https://dortania.github.io/hackintosh/updates/2021/09/06/acidanthera-september.html).
- Updated macOS from 11.4 to 11.6 without issues using Apple Software Update and OpenCore 0.7.3 EFI.

**SEPTEMBER 22 2021** (v2.9)

- Updated to OpenCore 0.7.2 and corresponding kexts (https://dortania.github.io/hackintosh/updates/2021/08/02/acidanthera-august.html).

**SEPTEMBER 22 2021** (v2.8)

- Updated to OpenCore 0.7.1 and corresponding kexts (https://dortania.github.io/hackintosh/updates/2021/07/05/acidanthera-july.html).
- Added VoltageShift (https://github.com/sicreative/VoltageShift) to undervolt CPU. Read **Undervolting** section if you want to undervolt your CPU.

**JUNE 14 2021** (v2.7)

- Updated to OpenCore 0.7.0 and corresponding kexts (https://dortania.github.io/hackintosh/updates/2021/06/07/acidanthera-june.html).
- Found out the cause regarding freeze issues removing power chord, read KNOWN ISSUES for more information.

**May 03 2021** (v2.6)

- Updated to OpenCore 0.6.9 and corresponding kexts (https://dortania.github.io/hackintosh/updates/2021/05/03/acidanthera-may.html).
- Removed BOOTx64.efi from EFI folder. I put a "legacy" EFI folder with BOOT available
- Cleaned up some unnecessary framebuffer patches
- Kexts_Extra folder (containing CPUFriendFriend profiles) inside OC moved to UTIL folder. If you want a different profile, just replace CPUFriendDataProvider.kext inside OC/Kexts
- Removed some unnecessary old stuff in UTIL folder
- Removed some unnecessary kexts
- Made some changes on ACPI patches
- Add information about upgrade OC and run without BOOTx64.efi
- Updated USBPorts.kext with Thunderbolt 3 ports
- Add BIOS setup options

**April 28 2021** (v2.5.3)

- Fixed audio not playing on boot issue. You may need to reset NVRAM the first time booting with AudioDxe EFI in order to set the correct volume.
- Added OpenCore 0.6.8 DEBUG version

**April 28 2021** (v2.5.2)

- Added AudioDxe to play boot chime
- Split EFI into 3 versions: Verbose (text boot picker), OpenCanopy (GUI boot picker) and OpenCanopy + AudioDxe (GUI boot picker and play boot chime like a real mac)
- Download for each version is avaliable on [Releases](https://github.com/leocg/Hackintosh-Dell-G5-5590/releases/) tab

**April 27 2021** (v2.5.1)

- Updated VoodooI2C, VoodooInput and VoodooPS2Controller to latest version
- Added OpenCanopy to render visual boot picker
- Updated macOS from 11.1 (20C69) to 11.3 (20E232) without issues using Apple Software Update and OpenCore 0.6.8 EFI.

**April 27 2021** (v2.5)

- Updated to OpenCore 0.6.8 and corresponding kexts (https://dortania.github.io/hackintosh/updates/2021/04/05/acidanthera-april.html).
- Updated CPUFriend to 1.2.3
- Kept Voodoo files (VoodooI2C, VoodooInput and VoodooPS2Controller) on older versions cause newer one is causing issues with trackpad. I'll update the repo when I solve the problem.

**April 27 2021** (v2.4)

- Updated to OpenCore 0.6.7 and corresponding kexts (https://dortania.github.io/hackintosh/updates/2021/03/01/acidanthera-march.html).

**April 27 2021** (v2.3)

- Updated to OpenCore 0.6.6 and corresponding kexts (https://dortania.github.io/hackintosh/updates/2021/02/01/acidanthera-february.html).

**April 27 2021** (v2.2)

- Updated to OpenCore 0.6.5 and corresponding kexts (https://dortania.github.io/hackintosh/updates/2021/01/04/acidanthera-january.html).
- Added enable-backlight-registers-fix property to fix backlight issues with new WhateverGreen
- Updated broken links from instructions (Thanks [@rafaeldgoliveira](https://github.com/rafaeldgoliveira)))

**December 09 2020** (v2.1)

- Updated to OpenCore 0.6.4 and kexts to latest version.
- Fixed native brightness control (Thanks [@caiomascarin](https://github.com/caiomascarin))
- Added SSDT-Swap-CommandOption.aml because VoodooInput removed this quirk in latest version
- Added HibernationFixup.kext because I'm testing some issues waking up on battery (sometimes CPU fixes on max clock)

**November 19 2020** (v2.0)

- Updated to OpenCore 0.6.3 and kexts to latest version. Tested with Big Sur for 2 weeks without issues.

**September 12 2020** (v1.7.0)

- Fixed dGPU issues after wake, keeping it disabled at all times
- Fixed video out using USB-C to HDMI adapter changing SMBIOS to MacBookPro15,2
- Added custom CPU profile tuned for high performance (there's another kext with CPU profile focused on power savings inside Kexts_Extra folder. Replace the version you want with original CPUFriendDataProvider.kext, remember to rename)
- Removed OpenCore bootpicker. After Dell logo go directly to Apple logo. Change Misc->Boot->ShowPicker to YES if you need the bootpicker.
- Updated VoodooI2C (2.4.4) and VoodooPS2Controller (2.1.6)
- Updated Kexts:
  - VoodooPS2Controller-2.1.6-RELEASE
  - VoodooI2C-2.4.4

**September 07 2020** (v1.6)

- Updated OpenCore to version 0.6.1 RELEASE
- Updated Kexts:
  - WhateverGreen-1.4.2-RELEASE
  - Lilu-1.4.7-RELEASE
  - VirtualSMC-1.1.6-RELEASE
  - AppleALC-1.5.2-RELEASE

**September 04 2020** (v1.5)

- Working Ethernet using RealtekRTL8111.kext (Changed OSBundleRequired from Network-Root to Root inside kext's Info.plist)
- Some kexts are development version instead of release cause resolved some issues. Next week I'll put release version when Acidanthera commit.
- I'm not using current Voodol2C/VoodooPS2Controller kext because latest version broken multitouch support with this laptop.

**August 03 2020** (v1.4)

- Removed NullEthernet.kext (don't need anymore cause installed Fenvi Wi-Fi card)
- Updated OpenCore to version 0.6.0
- Updated Kexts:
  - NoTouchID-1.0.4-RELEASE
  - WhateverGreen-1.4.1-RELEASE
  - Lilu-1.4.6-RELEASE
  - VirtualSMC-1.1.5-RELEASE
  - AppleALC-1.5.1-RELEASE
  - VoodooPS2Controller-2.1.6-RELEASE
  - NVMeFix-1.0.3-RELEASE

**August 02 2020** (v1.3)

- Made some tweaks all around. Laptop is stable, good battery life and performance.

**July 31 2020** (v1.2)

- Switched stock wifi card with Fenvi BCM94360NG, worked OOB with Catalina 10.15.6.

**July 23 2020** (v1.2)

- Added Dell Sensors combatibility with VirtualSMC (using compiled version, not release). Use with HWMonitorSMC2 to view all sensors and fan speed. iStat Menus don't display any information.

**July 19 2020** (v1.2)

- Minor adjustments

**July 17 2020** (v1.1)

- Fixed USB mapping with USBInjectAll.kext + SSDT-UIAC.dsl generated by Hackintool

**July 16 2020** (v1.1)

- USB mapped
- Fixed error that disconnecting device from USB-C port cause high usage of kernel_task. USB-C is not working with USB3 for now.
- I think dGPU is turning on after sleep cause of temperature changes and estimated battery. Before sleep idles between 45-50. After wake idles at 55-60 degrees.

**July 14 2020** (v1.0) - STABLE

- Disabled dGPU using [Optimus Method](https://dortania.github.io/Getting-Started-With-ACPI/Laptops/laptop-disable.html#optimus-method)
- Fixed double call for VoodooInput
- Removed SSDT-AWAC, DSDT already had variable and errors were shown on boot
- Removed -wegnoegpu in order to utilize Optimus Method. Battery life up from 50m to 3h.
- Removed NVMeFix.kext. Trying to run as vanilla as possible.
- Remapped all FN keys using Karabiner Elements
- Testing different CPU Friend configs. So far the Vanilla one is the best option
- Removed -v argument and disable all OpenCore debug tools
- Linked Windows bootloader cause already lost windows EFI twice during hackintosh tweaks.

**July 13 2020** (v0.4)

CFG Lock disabled in bios and removed Quirks from config.plist

**July 13 2020** (v0.3)

Fixed trackpad issues. Preparing machine for disabling CFG Lock and USB Mapping.

**July 09 2020** (v0.2)

Fake ethernet to make iCloud work, fixed battery status.

**July 09 2020**

First version fast and functional. AML files fixed to match notebook specs. Still working with drivers, need to bring back battery status.

**July 07 2020**

Initial working version.
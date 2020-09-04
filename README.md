# Hackintosh-Dell-G5-5590

## :computer: ​Laptop Specs

### Dell G5 5590 a80p 

Processor: Core i7-9750H 6C/12T (Coffee Lake Plus / Coffee Lake Refresh) 
iGPU: Intel UHD 630 Graphics (Video Out using a **USB Type-C to DisplayPort adapter** into the USB 3.1 Gen 2 Type-C/DisplayPort 1.2/Thunderbolt 3 port)  
~~dGPU: nVidia GeForce RTX 2060~~ ~~(HDMI 2.0b port /mini DisplayPort 1.4)~~  
Display: 15.6 1080p (1920x1080) 144hz  
Memory: 16GB DDR4 2666MHz (8GBx2)  
Storage: 512GB Intel NVMe SSD + 1tb SSD (Crucial BX500)  
Audio: Realtek ALC3204-CG (ALC236)  
Wifi/Bluetooth: ~~Qualcomm QCA61x4A (DW1820)~~ Fenvi BCM94360NG (ordered m2 card at aliexpress from Fenvi Store)  
Ethernet: Killer GB E2500V2 10/100/1000 Mbps  
USB 3.1  
Thunderbolt    
Webcam + Microphone  

## About

This is my "Hackintosh Diary", will be using it to maintain a triple boot Dell G5 5590 a80p between macOS, Arch Linux and Windows.  

Don't directly use my EFI folder, your computer won't boot cause it has CFG Lock disabled and other post install stuff.

Vanilla Boot could be accomplished using OPENCORE USB BOOT folder. Use this folder to make a bootable USB disk with macOS Catalina (tested with 10.5.5).

Used [Vanilla Laptop Guide](https://dortania.github.io/vanilla-laptop-guide/) from [Dortania](https://dortania.github.io/), but laptop and desktop guide was merged into [OpenCore Install Guide](https://dortania.github.io/OpenCore-Install-Guide/).

Most work is done post installation, be prepared to read a lot. CFG Lock is difficult to understand but very simple to execute. Disabling CFG Lock and dGPU using [Optimus Method](https://dortania.github.io/Getting-Started-With-ACPI/Laptops/laptop-disable.html#optimus-method) has major impact on battery life.

If you like this guide and can help with any value, please buy me a coffee :coffee:

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=N7EY58HHR9RUQ)



## INSTALLATION

Follow [Vanilla Laptop Guide](https://dortania.github.io/vanilla-laptop-guide/) and use MacBookPro16,1 SMBIOS (remember to insert your generated data at platform info section). Setup config.plist using [Coffee Lake Plus](https://dortania.github.io/vanilla-laptop-guide/OpenCore/config-laptop.plist/coffee-lake-plus.html). Read every guide very carefully BEFORE start and know what you're going to do beforehand.

**ACPI changes:**

- SSNC-PLUG - CPU0 into PP00 -> Processor ID on this machine is PP00

**DELL SPECIFICS config.plist:**

- UpdateSMBIOSMode = Custom
- CustomSMBIOSGuid = True
- Audio layout-id = 15 (other channels worked, but 15 offered better stability and sound quality overall)

**Patching CFG Lock**

- Download BIOS from Dell website (version must be the same, variable can change after updates). 
- Dump bios with DecompNewDell.py (used Python3)
- Open dumped bios with UEFITool
- Search for "CFG Lock, VarStoreInfo (VarOffset/VarName)". Variable name come just after (in my case, using BIOS 1.13.2, was 0x5C4)

`One Of: CFG Lock, VarStoreInfo (VarOffset/VarName): 0x5C4, VarStore: 0x1 [...]

The steps above I followed to find the correct CFG Lock variable name. After that, simply boot into Modified GRUB Shell and change variable from 0x5C4 to 0x00:

- Prepare EFI Boot Disk using [Disabling CFG Lock](https://dortania.github.io/OpenCore-Desktop-Guide/extras/msr-lock#disabling-cfg-lock) instructions and patch using **setup_var_3 0x5C4 0x00**

## KNOWN ISSUES

- Battery drain after wake from sleep. Already tried different methods without success (Optimus Method, Bumblebee Method, GPU Spoof, Flag device in config.plist... None of then worked). I'm searching for solutions but for now I'm shutting down laptop instead of putting to sleep.
- Quicktime and iTunes show artifacts while full screen. IINA runs fine, tested .mp4, .mkv and .ts movies
- Sometimes unplugging/replugging power adaptor causes keyboard lag and I have to reboot in order to resolve the issue.
- Sometimes unplugging/replugging quickly causes laptop to crash. I'm testing SSDT-XOSI.aml, found somewhere that it would fix the problem, but didn't resolve it yet.
- Headphone port don't work with mic. I'm researching how to make a custom layout for AppleALC in order to fix it.

## WORKING / NOT WORKING

- [x] iGPU Acceleration 
- [x] Backlight 
- [x] 144hz display 
- [x] Apple Services
- [x] Keyboard
- [x] Keyboard backlight (RGB backlight works, but had to setup at Windows 10 Alienware Command Center. When boot at macOS the config remais, including color. Cannot turn off keyboard backlight in macOS for now. I found some information regarding sending information via USB to keyboard backlight, looking for a solution to inject colors)
- [x] Trackpad
- [x] Audio
- [x] Microphone
- [x] Webcam
- [x] USB3 ports 
- [x] Card reader
- [x] CFG Lock disabled
- [x] NVRAM - Verified using [this](https://dortania.github.io/OpenCore-Desktop-Guide/post-install/nvram.html#verifying-if-you-have-working-nvram) method
- [x] Bluetooth - Using Fenvi BCM94360NG (Original card worked with bluetooth out of box too)
- [x] Apple Communications (Continuity, airdrop, airplay, etc) - Using Fenvi BCM94360NG (Original card didn't provide support)
- [x] Wi-Fi - Using Fenvi BCM94360NG (Original card don't work on macOS)
- [ ] Thunderbolt 3 video out (Don't have a Thunderbolt->DisplayPort adapter to test)
- [x] Ethernet (Thanks [@radaelilucca](https://github.com/radaelilucca))

## Future reading

- [ ] Share Bluetooth pairing between windows and mac: follow [this](https://www.reddit.com/r/hackintosh/comments/hjwu43/howto_share_a_bluetooth_pairing_headphones_etc/)
- [ ] Thunderbolt 3 Video out fix: follow [this](https://www.tonymacx86.com/threads/dell-g5-5590-thunderbolt-display-need-help.293776/)

## CHANGELOG

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

**July 07 2020 - Initial**
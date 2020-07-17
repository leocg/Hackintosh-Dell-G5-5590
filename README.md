# Hackintosh-Dell-G5-5590

## Laptop Specs

### Dell G5 5590 a80p 

Processor: Core i7-9750H 6C/12T (Coffee Lake Plus / Coffee Lake Refresh) 
iGPU: Intel UHD 630 Graphics (Video Out using a **USB Type-C to DisplayPort adapter** into the USB 3.1 Gen 2 Type-C/DisplayPort 1.2/Thunderbolt 3 port)  
~~dGPU: nVidia GeForce RTX 2060~~ ~~(HDMI 2.0b port /mini DisplayPort 1.4)~~  
Display: 15.6 1080p (1920x1080) 144hz  
Memory: 16GB DDR4 2666MHz (8GBx2)  
Storage: 512GB Intel NVMe SSD + 1tb SSD (Crucial BX500)  
Audio: Realtek ALC3204-CG  
Wifi/Bluetooth: ~~Qualcomm QCA61x4A (DW1820)~~ Fenvi BCM94360NG (waiting for arrival)  
Ethernet: Killer GB E2500V2 10/100/1000 Mbps  
USB 3.1  
Thunderbolt    
Webcam + Microphone  

## About

This is my "Hackintosh Diary", will be using it to maintain a triple boot Dell G5 5590 a80p between macOS, Arch Linux and Windows.  

Don't directly use my EFI folder, your computer won't boot cause it has CFG Lock disabled and other post install stuff.

Vanilla Boot could be accomplished using OPENCORE USB BOOT folder.

Using [Vanilla Laptop Guide](https://dortania.github.io/vanilla-laptop-guide/) from [Dortania](https://dortania.github.io/)

Most work is done post installation, be prepared to read a lot. CFG Lock is difficult to understand but very simple to execute. Disabling CFG Lock and dGPU using [Optimus Method](https://dortania.github.io/Getting-Started-With-ACPI/Laptops/laptop-disable.html#optimus-method) has major impact on battery life.

I'm investigating some issues with freeze when plugging in and out more than once and quickly and some kernel panic using Intel Power Gadget.

Bought this laptop to replace my MacBook Pro 2011 17". So far is great! Using primary for web development.

## INSTALLATION

Follow [Vanilla Laptop Guide](https://dortania.github.io/vanilla-laptop-guide/) and use MacBookPro16,1 SMBIOS (remember to insert your generated data at platform info section). Setup config.plist using [Coffee Lake Plus](https://dortania.github.io/vanilla-laptop-guide/OpenCore/config-laptop.plist/coffee-lake-plus.html). Read every guide very carefully BEFORE start and know what you're going to do beforehand.

**ACPI changes:**

- SSNC-PLUG - CPU0 into PP00 -> Processor ID on this machine is PP00

**DELL SPECIFICS config.plist:**

- RebuildAppleMemoryMap = False
- UpdateSMBIOSMode = Custom
- CustomSMBIOSGuid = True
- Audio layout-id = 15 (other channels worked, but 15 offered better stability and sound quality overall)

**Patching CFG Lock**

- Download BIOS from Dell website (version must be the same, variable can change after updates). 
- Dump bios with DecompNewDell.py (used Python3)
- Open dumped bios with UEFITool
- Search for "CFG Lock, VarStoreInfo (VarOffset/VarName)". Variable name come just after (in my case, using BIOS 1.13.2, was 0x5C4)

`One Of: CFG Lock, VarStoreInfo (VarOffset/VarName): 0x5C4, VarStore: 0x1, QuestionId: 0x361, Size: 1, Min: 0x0, Max 0x1, Step: 0x0 {05 91 98 03 99 03 61 03 01 00 C4 05 10 10 00 01 00}`
	`One Of Option: Disabled, Value (8 bit): 0x0 {09 07 04 00 00 00 00}`
	`One Of Option: Enabled, Value (8 bit): 0x1 (default) {09 07 03 00 30 00 01}`
`End One Of {29 02}`

- Prepare EFI Boot Disk using [Disabling CFG Lock](https://dortania.github.io/OpenCore-Desktop-Guide/extras/msr-lock#disabling-cfg-lock) instructions and patch using **setup_var_3 0x5C4 0x00**
- After applying patch chech in Hackintool -> Utilities -> GetAppleIntelInfo
- Inside IA32_MISC_ENABLES  (0x1A0) : 0x850089: **CFG Lock  : 0 (MSR not locked)**

## TODO

- ~~Proper port mapping - Fix USB3 ports not delivering more power than 500. Only Thunderbolt3/USB-C port delivers full power.~~
- Install Fenvi BCM94360NG Wi-Fi/Bluetooth card (waiting for arrival, using TP Link USB dongle for now)
- ~~Review CPU frequencies.~~
- ~~Remap brightness to F11 and F12 (currently Fn+S Fn+B)~~ 
- Quicktime and iTunes show artifacts while full screen. IINA runs fine, tested .mp4, .mkv and .ts movies

## WORKING / NOT WORKING

- [x] iGPU Acceleration 
- [x] Backlight 
- [x] 144hz display 
- [x] Bluetooth
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
- [x] Apple bootloader (OpenCanopy) - **Removed until it gets more stable, sometimes it boots slow and I can't select any partition other than default**
- [ ] Thunderbolt 3 video out (Don't have a Thunderbolt->DisplayPort adapter yet)
- [ ] Ethernet (no drivers yet for Killer GB E2500V2)
- [ ] Apple Communications (Continuity, airdrop, airplay, etc) - Waiting for Airport Card
- [ ] Wi-Fi - Waiting for Airport Card

## Future reading

Some features need improvement. I'm waiting for Fenvi BCM94360NG airport adapter to unlock remaining features.

- [ ] Share Bluetooth pairing between windows and mac: follow [this](https://www.reddit.com/r/hackintosh/comments/hjwu43/howto_share_a_bluetooth_pairing_headphones_etc/)
- [ ] Thunderbolt 3 Video out fix: follow [this](https://www.tonymacx86.com/threads/dell-g5-5590-thunderbolt-display-need-help.293776/)

## TOOLS

- [OpenCore 0.5.9](https://github.com/acidanthera/OpenCorePkg)
- [gibMacOS](https://github.com/corpnewt/gibMacOS) - Download macOS vanilla install
- [MountEFI](https://github.com/corpnewt/MountEFI) - Mount EFI partitions
- [ProperTree](https://github.com/corpnewt/ProperTree) - Generate config.plist based on OC folder
- [GenSMBIOS](https://github.com/corpnewt/GenSMBIOS) - Generate Mac serials

## File History

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

### Recovery operating system 

- macOS Catalina 10.5.5 (full install)

### KEXTs

- AppleALC.kext ([1.5.0](https://github.com/acidanthera/AppleALC/releases))
- Lilu.kext ([1.4.5](https://github.com/acidanthera/Lilu/releases))
- NoTouchID.kext ([1.0.3](https://github.com/al3xtjames/NoTouchID/releases))
- VirtualSMC.kext ([1.1.4](https://github.com/acidanthera/virtualsmc/releases))
  - SMCBatteryManager.kext (1.0)
  - SMCLightSensor.kext (1.0)
  - SMCProcessor.kext (1.1.4)
  - SMCSuperIO.kext (1.1.4)
- VoodooI2C.kext ([2.4.3](https://github.com/VoodooI2C/VoodooI2C/releases))
  - VoodooI2CHID.kext (1.0)
- VoodooPS2Controller.kext ([2.1.5](https://github.com/acidanthera/VoodooPS2/releases))
- WhateverGreen.kext ([1.4.0](https://github.com/acidanthera/whatevergreen/releases))

### ACPI

- ~~SSDT-AWAC.aml~~
- SSDT-EC-USBX.aml [SSDT-EC-USBX.dsl](https://github.com/acidanthera/OpenCorePkg/blob/master/Docs/AcpiSamples/SSDT-EC-USBX.dsl)
- SSDT-GPI0.aml [SSDT-GPI0.dsl](https://github.com/dortania/Getting-Started-With-ACPI/blob/master/extra-files/decompiled/SSDT-GPI0.dsl)
- SSDT-PLUG.aml [SSDT-PLUG.dsl](https://github.com/acidanthera/OpenCorePkg/blob/master/Docs/AcpiSamples/SSDT-PLUG.dsl)
- SSDT-PNLF-CFL.aml [SSDT-PNLF-CFL.dsl](https://github.com/dortania/Getting-Started-With-ACPI/blob/master/extra-files/decompiled/SSDT-PNLF-CFL.dsl)

All dsl files downloaded and compiled 07 07 2020. 

